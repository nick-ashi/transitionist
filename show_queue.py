from spotipy_client import get_spotify_client

def show_queue():
    """
    Fetches & prints user's current Spotify queue and what's playing.
    This shit unfortunately reqs Premium ;; make sure user-read-playback-state scope is enabled.
    """
    sp = get_spotify_client()

    # dictionary with two pairs::
    # 1. currently_playing
    # 2. queue
    resp = sp._get("me/player/queue")

    # currently playing
    curr = resp.get("currently_playing")
    if curr:
        artists = ", ".join(a["name"] for a in curr["artists"])
        print("Currently playing:")
        print(f" → {curr['name']} by {artists}\n")
    else:
        print("No track is currently playing.\n")

    # upcoming queue
    queue = resp.get("queue", [])
    if queue:
        print("Upcoming queue:")
        for i, t in enumerate(queue, 1):
            artists = ", ".join(a["name"] for a in t["artists"])
            print(f"{i}. {t['name']} by {artists}")
    else:
        print("Your queue is empty.")
