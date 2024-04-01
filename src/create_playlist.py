import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.environ.get("SPOTIFY_REDIRECT_URI")


def init_conn(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
):
    assert client_id, "client_id is null. Check SPOTIFY_CLIENT_ID in your .env."  # noqa: S101
    assert client_secret, "client_secret is null. Check SPOTIFY_CLIENT_SECRET in your .env."  # noqa: S101
    assert redirect_uri, "redirect_uri is null. Check SPOTIFY_REDIRECT_URI in your .env."  # noqa: S101
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
        )
    )
    return sp


def check_playlist_exists_by_name(sp, name):
    playlists = sp.current_user_playlists()["items"]
    for playlist in playlists:
        if playlist["name"] == name:
            print(f'📀 {playlist["name"]} alredy exists (id: {playlist["id"]})')
            return playlist["id"]
    return


def create_playlist(
    sp, name="WhatsApp Test Playlist", public=True, collaborative=False, description="Created from Whatsapp"
):
    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(
        user_id, name, public=public, collaborative=collaborative, description=description
    )
    print(f"✨ Successfully created playlist {name} with ID {playlist['id']}")
    return playlist["id"]


def song_in_playlist(sp, playlist_id, track_id):
    results = sp.playlist_tracks(playlist_id)
    return any(item["track"]["id"] == track_id for item in results["items"])


def add_songs(sp, playlist_id, spotify_links):
    for link in spotify_links:
        track = sp.track(link)
        if not song_in_playlist(sp, playlist_id, track["id"]):
            sp.playlist_add_items(playlist_id, [track["id"]])
            print(f"Song '{track['name']}' added to playlist.")
        else:
            print(f"Song '{track['name']}' already in playlist.")


def delete_playlist(sp, playlist_id):
    try:
        sp.current_user_unfollow_playlist(playlist_id)
        print(f"Successfully deleted the playlist with ID {playlist_id}")
    except Exception as e:
        print(f"Error occurred while trying to delete the playlist: {e}")
