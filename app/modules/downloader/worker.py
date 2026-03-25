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
