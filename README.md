# playlist-metrics
Metrics for a Spotify collaborative playlist.

## Setting up

To use playlist-metrics, you need to install the `spotipy` module with `pip install setuptools`.

The first step is to set up a 
[Spotify API Client](https://beta.developer.spotify.com/dashboard/applications).

`playlist-metrics` also expects a file named usernames.txt alongside the python files 
containing lines mapping spotify usernames to human-friendly names, for all collaborators 
of the playlist. One entry per line of the form: `username:Real Name`.

