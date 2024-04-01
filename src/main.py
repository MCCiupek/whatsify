import sys

from create_playlist import add_songs, check_playlist_exists_by_name, create_playlist, init_conn
from extract_links import extract_spotify_urls


def main(filename="/data/brillo.txt", name="### test ###"):
    spotify_urls = extract_spotify_urls(filename)
    sp = init_conn()
    playlist_id = check_playlist_exists_by_name(sp, name)
    if playlist_id is None:
        playlist_id = create_playlist(sp, name)
    add_songs(sp, playlist_id, spotify_urls)


if __name__ == "__main__":
    assert len(sys.argv) == 3, "Usage: python main.py path/to/extract.txt playlist_name"  # noqa: S101
    main(sys.argv[1], sys.argv[2])
