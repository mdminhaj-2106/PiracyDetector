import time
import sqlite3
from concurrent.futures import ThreadPoolExecutor, as_completed
from downloader import VideoDownloader

QUEUE_DB = "queue.db"
MAX_CONCURRENT_DOWNLOADS = 3 # I didnt used large value as it increase the chance of getting blocked

class QueueWorker:
    def __init__(self):
        self.downloader = VideoDownloader()
        self.setup_databases()

    def setup_databases(self):
        """Ensures the SQLite queue table exists."""
        with sqlite3.connect(QUEUE_DB) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS links (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT UNIQUE,
                    status TEXT DEFAULT 'PENDING'
                )
            """)
            conn.commit()

    def fetch_batch(self, limit):

        with sqlite3.connect(QUEUE_DB) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, url FROM links Where status = 'PENDING' LIMIT ?", (limit,))
            rows = cursor.fetchall()

            for row in rows:
                cursor.execute("UPDATE line SET status = 'PROCESSING' WHERE id = ?", (row[0],))
            conn.commit()
            return rows
        
    def mark_completed(self, task_id, success):
        
        with sqlite3.connect(QUEUE_DB) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE links SET status = ? WHERE id = ?", (status, task_id))
            conn.commit()

    def process_task(self,task_id, url):

        print(f"[*] Thread started: {url}")
        saved_path = self.downloader.download_video(url)

        if saved_path:
            print(f"[+] Thread success: Saved to {saved_path}")
            self.mark_completed(task_id, success=True)
        else:
            print(f"[-] Thread failed: {url}")
            self.mark_completed(task_id, success=False)
    
    def start(self):

        print(f"Worker Online. Listening for tasks (Max Threads: {MAX_CONCURRENT_DOWNLOADS})")
        with ThreadPoolExecutor(max_workers=MAX_CONCURRENT_DOWNLOADS) as executor:
            while True:
                batch = self.fetch_batch(MAX_CONCURRENT_DOWNLOADS)

                if not batch:
                    # Database is empty. Sleep for 2 seconds to avoid frying the CPU.
                    time.sleep(2)
                    continue
                print(f"\n[Queue] Found {len(batch)} tasks. Dispatching to threads...")
                
                # Assign tasks to the thread pool
                futures = [executor.submit(self.process_task, row[0], row[1]) for row in batch]
                
                # Wait for the current batch to finish before polling the database again
                for future in as_completed(futures):
                    future.result()

if __name__ == "__main__":
    worker = QueueWorker()
    worker.start()