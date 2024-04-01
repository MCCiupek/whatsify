import os
from typing import Any, Optional

import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID: Optional[str] = os.environ.get("SPOTIPY_CLIENT_ID")
CLIENT_SECRET: Optional[str] = os.environ.get("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI: Optional[str] = os.environ.get("SPOTIPY_REDIRECT_URI")


def init_conn(
    client_id: Optional[str] = CLIENT_ID,
    client_secret: Optional[str] = CLIENT_SECRET,
    redirect_uri: Optional[str] = REDIRECT_URI,
) -> Any:
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
        )
    )
    return sp


def check_playlist_exists_by_name(sp: Any, name: str) -> Any:
    playlists = sp.current_user_playlists()["items"]
    for playlist in playlists:
        if playlist["name"] == name:
            print(f'📀 {playlist["name"]} alredy exists (id: {playlist["id"]})')
            return playlist["id"]
    return


def create_playlist(
    sp: Any,
    name: str = "WhatsApp Test Playlist",
    public: bool = True,
    collaborative: bool = False,
    description: str = "Created from Whatsapp",
) -> Any:
    user_id = sp.current_user()["id"]
    playlist = sp.user_playlist_create(
        user_id, name, public=public, collaborative=collaborative, description=description
    )
    print(f"✨ Successfully created playlist {name} with ID {playlist['id']}")
    return playlist["id"]


def song_in_playlist(sp: Any, playlist_id: str, track_id: str) -> Any:
    results = sp.playlist_tracks(playlist_id)
    return any(item["track"]["id"] == track_id for item in results["items"])


def add_songs(sp: Any, playlist_id: str, spotify_links: list[str]) -> Any:
    for link in spotify_links:
        track = sp.track(link)
        if not song_in_playlist(sp, playlist_id, track["id"]):
            sp.playlist_add_items(playlist_id, [track["id"]])
            print(f"Song '{track['name']}' added to playlist.")
        else:
            print(f"Song '{track['name']}' already in playlist.")


def delete_playlist(sp: Any, playlist_id: str) -> None:
    try:
        sp.current_user_unfollow_playlist(playlist_id)
        print(f"Successfully deleted the playlist with ID {playlist_id}")
    except Exception as e:
        print(f"Error occurred while trying to delete the playlist: {e}")
