import webbrowser
from ytmusicapi import YTMusic


def play_music(name: str):
    ytmusic = YTMusic()
    url = "https://music.youtube.com/watch?v="
    id = ytmusic.search(name)[1]["videoId"]
    # print(url + id)
    webbrowser.open(url + id)


if __name__ == "__main__":
    name = input("Song name: ")
    play_music(name)
    exit(0)
