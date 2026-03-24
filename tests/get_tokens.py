from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

flow = InstalledAppFlow.from_client_secrets_file(
    "../PiracyDetector/client-secret.json",
    SCOPES
)

# This automatically handles redirect URI and browser flow
credentials = flow.run_local_server(
    port=8080,
    access_type="offline",   # ensures refresh token
    prompt="consent"         # forces refresh token every time
)

print("\n=== TOKENS GENERATED SUCCESSFULLY ===")
print("ACCESS TOKEN:", credentials.token)
print("REFRESH TOKEN:", credentials.refresh_token)