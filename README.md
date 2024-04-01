# whatsify

[![Release](https://img.shields.io/github/v/release/MCCiupek/whatsify)](https://img.shields.io/github/v/release/MCCiupek/whatsify)
[![Build status](https://img.shields.io/github/actions/workflow/status/MCCiupek/whatsify/main.yml?branch=main)](https://github.com/MCCiupek/whatsify/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/MCCiupek/whatsify/branch/main/graph/badge.svg)](https://codecov.io/gh/MCCiupek/whatsify)
[![Commit activity](https://img.shields.io/github/commit-activity/m/MCCiupek/whatsify)](https://img.shields.io/github/commit-activity/m/MCCiupek/whatsify)
[![License](https://img.shields.io/github/license/MCCiupek/whatsify)](https://img.shields.io/github/license/MCCiupek/whatsify)

Create Spotify playlist from Whatsapp chats.

- **Github repository**: <https://github.com/MCCiupek/whatsify/>
- **Documentation** <https://MCCiupek.github.io/whatsify/>

## usage

### Repo and Auth set-up (to do once)

1. Clone this directory

```bash
gcl git@github.com:MCCiupek/whatsify.git
cd whatsify
```

2. Create an app in [Spotify Devlopers](https://developer.spotify.com/dashboard)
3. Save your credentials in a `.env` file

```python
SPOTIFY_CLIENT_ID='<YOUR_SPOTIFY_CLIENT_ID>'
SPOTIFY_CLIENT_SECRET='<YOUR_SPOTIFY_CLIENT_SECRET>'
SPOTIFY_REDIRECT_URI='http://localhost:8000'
```

### Create/update a playlist

1. Make sure that the repo is correctly set-up (cf. instructions above)
2. Export your Whatsapp chat in `txt` file.
3. Run:

```bash
poetry install
poetry shell
poetry run python path/to/your/extract.txt playlist_name
```

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
