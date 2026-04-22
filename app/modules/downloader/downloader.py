import os
import yt_dlp

class VideoDownloader:
    def __init__(self):
        self.download_dir = os.path.join(os.path.dirname(__file__), 'downloads')
        os.makedirs(self.download_dir, exist_ok=True)

        self.ydl_opts = {
            # Force mp4 format for consistency before sending to nxt step
            
            #'format': 'bestvideo[ext=mp4]/mp4', 
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'outtmpl': os.path.join(self.download_dir, '%(extractor)s_%(id)s.%(ext)s'),
            'quiet': False, # Keep this False while testing so you can see the terminal output
            'no_warnings': False,
            'ignoreerrors': False, # We want it to raise errors so we can catch them
        }
    
    def download_video(self, url):
    
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as yld:
                info_dict = yld.extract_info(url, download = True)
                
                expected_filename = f"{info_dict['extractor']}_{info_dict['id']}.mp4"
                file_path = os.path.join(self.download_dir, expected_filename)

                return file_path
            
        except yt_dlp.utils.DownloadError as e:
            print(f"[-] yt-dlp failed to download {url}. Reason: {e}") # invalid URLs, deleted videos, geo-block..etc
            return None
        
        except Exception as e:
            
            print(f"[-] An unexpected error occurred with {url}: {e}") # Catch-all for unexpected system errors
            return None

