from src.create_playlist import check_playlist_exists_by_name, create_playlist, delete_playlist, init_conn


def test_connection() -> None:
    sp = init_conn()
    track = sp.track("1BLOVHYYlH4JUHQGcpt75R")
    assert track["name"] == "Ode To The Mets"


def test_create_playlist() -> None:
    sp = init_conn()
    playlist_id = create_playlist(sp, name="test playlist")
    assert check_playlist_exists_by_name(sp, "test playlist")
    delete_playlist(sp, playlist_id)
