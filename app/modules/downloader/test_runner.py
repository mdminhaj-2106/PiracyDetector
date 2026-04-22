from downloader import VideoDownloader

TEST_LINKS = [
    "https://youtu.be/hKHdedtnDU0?si=FS4voXEdRhoWmCuR",
    
    "https://www.reddit.com/r/ipl/comments/1lw96t5/compilation_of_firstball_sixes_on_ipl_debut/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button",
    "https://x.com/IPL/status/1929940761551966315?s=20",
    
    "https://www.instagram.com/reel/DSCoB93jFiY/?utm_source=ig_web_button_share_sheet",
    "https://dai.ly/x9htd4q",
    
    "https://youtu.be/hKHdedtnjnsdjndjnsnDU0?si=FS4iudsfbfbelfnekfnewfjbhufvgvoXEdRhoWmjsbdffsCuR"
]

def main():
    print("Startting Downloader \n")
    engine = VideoDownloader()

    for url in TEST_LINKS:
        print(f"[*] Processing URL: {url}")

        saved_path = engine.download_video(url)

        if saved_path:
            print(f"[+] Success! Video saved ready for Hashing Engine at: {saved_path}\n")
        else:
            print(f"[-] Failed. Moving to next item in queue...\n")
        

if __name__ == "__main__":
    main()