import os
import googleapiclient.discovery
from google.auth.transport.requests import Request

from ...core.config import settings

# Scopes will be passed dynamically per API

API_CONFIG = {
    "youtube": {
        "service_name": "youtube",
        "version": "v3",
        "scopes": settings.SCOPES,
    }
}

from google.oauth2.credentials import Credentials

def load_credentials(scopes):
    return Credentials(
        token=settings.GOOGLE_ACCESS_TOKEN,
        refresh_token=settings.GOOGLE_REFRESH_TOKEN,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=settings.GOOGLE_CLIENT_ID,
        client_secret=settings.GOOGLE_CLIENT_SECRET,
        scopes=scopes,
    )

def get_client(api_name: str):
    if api_name not in API_CONFIG:
        raise ValueError(f"Unsupported API: {api_name}")

    config = API_CONFIG[api_name]

    credentials = load_credentials(config["scopes"])

    client = googleapiclient.discovery.build(
        config["service_name"],
        config["version"],
        credentials=credentials
    )

    return client


def scrape_youtube():
    youtube = get_client("youtube")

    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q="football"
    )

    response = request.execute()
    print(response)

if __name__ == "__main__":
    scrape_youtube()