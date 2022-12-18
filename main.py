import ctypes
import tkinter as tk
from tkinter import ttk
import random
from ytmusic import play_music
from spotify import Spotify

ctypes.windll.shcore.SetProcessDpiAwareness(True)


class App:
    def __init__(self):
        # * Default Config
        self.root = tk.Tk()
        self.root.geometry("1500x1200+500+50")
        self.root.title("Top Songs on Spotify")
        self.root.iconbitmap("spotify-logo.ico")
        self.root.tk.call("tk", "scaling", 3.0)

        # * Custom Variables
        self.font = ("Roboto", 12)
        self.spotify = Spotify()

        # * Created Tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")

        self.todays_top_hits_tab = ttk.Frame(self.notebook)
        self.top_50_global_tab = ttk.Frame(self.notebook)
        self.top_50_usa_tab = ttk.Frame(self.notebook)
        self.top_50_india_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.todays_top_hits_tab, text="Today's Top Hits")
        self.notebook.add(self.top_50_global_tab, text="Top 50 - Global")
        self.notebook.add(self.top_50_usa_tab, text="Top 50 - USA")
        self.notebook.add(self.top_50_india_tab, text="Top 50 - India")

        # * Adding Content in Today's Top Hits Tab
        self.todays_top_hits(self.todays_top_hits_tab, self.font)

        # * Adding Content in Top 50 Global Tab
        self.top_50_global(self.top_50_global_tab, self.font)

        # * Adding Content in Top 50 USA Tab
        self.top_50_usa(self.top_50_usa_tab, self.font)

        # * Adding Content in Top 50 India Tab
        self.top_50_india(self.top_50_india_tab, self.font)

        self.root.mainloop()
        return

    def todays_top_hits(self, tab, font):
        self.todays_top_hits_list_frame = ttk.Frame(tab)
        self.todays_top_hits_list_frame.pack(side="top", fill="both", expand=True)
        self.todays_top_hits_lbx = tk.Listbox(
            self.todays_top_hits_list_frame,
            font=font,
            activestyle="dotbox",
        )
        self.todays_top_hits_lbx.pack(side="left", fill="both", expand=True)

        for item in self.spotify.get_todays_top_hits():
            self.todays_top_hits_lbx.insert(
                random.randint(1, 1000),
                f"{item['track']['name']} by {item['track']['artists'][0]['name']}",
            )

        self.todays_top_hits_sbr = ttk.Scrollbar(self.todays_top_hits_list_frame)
        self.todays_top_hits_sbr.pack(side="right", fill="y")
        self.todays_top_hits_sbr.config(command=self.todays_top_hits_lbx.yview)
        self.todays_top_hits_lbx.config(yscrollcommand=self.todays_top_hits_sbr.set)

        self.play_btn = ttk.Button(
            tab, text="Play", command=self.playing_todays_top_hits
        )
        self.play_btn.pack(side="bottom", padx=10, pady=10)

    def top_50_global(self, tab, font):
        self.top_50_global_list_frame = ttk.Frame(tab)
        self.top_50_global_list_frame.pack(side="top", fill="both", expand=True)
        self.top_50_global_lbx = tk.Listbox(
            self.top_50_global_list_frame,
            font=font,
            activestyle="dotbox",
        )
        self.top_50_global_lbx.pack(side="left", fill="both", expand=True)

        for item in self.spotify.get_top_50_global():
            self.top_50_global_lbx.insert(
                random.randint(1, 1000),
                f"{item['track']['name']} by {item['track']['artists'][0]['name']}",
            )

        self.top_50_global_sbr = ttk.Scrollbar(self.top_50_global_list_frame)
        self.top_50_global_sbr.pack(side="right", fill="y")
        self.top_50_global_sbr.config(command=self.top_50_global_lbx.yview)
        self.top_50_global_lbx.config(yscrollcommand=self.top_50_global_sbr.set)

        self.play_btn = ttk.Button(tab, text="Play", command=self.playing_top_50_global)
        self.play_btn.pack(side="bottom", padx=10, pady=10)

    def top_50_usa(self, tab, font):
        self.top_50_usa_list_frame = ttk.Frame(tab)
        self.top_50_usa_list_frame.pack(side="top", fill="both", expand=True)
        self.top_50_usa_lbx = tk.Listbox(
            self.top_50_usa_list_frame,
            font=font,
            activestyle="dotbox",
        )
        self.top_50_usa_lbx.pack(side="left", fill="both", expand=True)

        for item in self.spotify.get_top_50_usa():
            self.top_50_usa_lbx.insert(
                random.randint(1, 1000),
                f"{item['track']['name']} by {item['track']['artists'][0]['name']}",
            )

        self.top_50_usa_sbr = ttk.Scrollbar(self.top_50_usa_list_frame)
        self.top_50_usa_sbr.pack(side="right", fill="y")
        self.top_50_usa_sbr.config(command=self.top_50_usa_lbx.yview)
        self.top_50_usa_lbx.config(yscrollcommand=self.top_50_usa_sbr.set)

        self.play_btn = ttk.Button(tab, text="Play", command=self.playing_top_50_usa)
        self.play_btn.pack(side="bottom", padx=10, pady=10)

    def top_50_india(self, tab, font):
        self.top_50_india_list_frame = ttk.Frame(tab)
        self.top_50_india_list_frame.pack(side="top", fill="both", expand=True)
        self.top_50_india_lbx = tk.Listbox(
            self.top_50_india_list_frame,
            font=font,
            activestyle="dotbox",
        )
        self.top_50_india_lbx.pack(side="left", fill="both", expand=True)

        for item in self.spotify.get_top_50_india():
            self.top_50_india_lbx.insert(
                random.randint(1, 1000),
                f"{item['track']['name']} by {item['track']['artists'][0]['name']}",
            )

        self.top_50_india_sbr = ttk.Scrollbar(self.top_50_india_list_frame)
        self.top_50_india_sbr.pack(side="right", fill="y")
        self.top_50_india_sbr.config(command=self.top_50_india_lbx.yview)
        self.top_50_india_lbx.config(yscrollcommand=self.top_50_india_sbr.set)

        self.play_btn = ttk.Button(tab, text="Play", command=self.playing_top_50_india)
        self.play_btn.pack(side="bottom", padx=10, pady=10)

    def playing_todays_top_hits(self):
        for i in self.todays_top_hits_lbx.curselection():
            print("Playing,", self.todays_top_hits_lbx.get(i))
            play_music(self.todays_top_hits_lbx.get(i))

    def playing_top_50_global(self):
        for i in self.top_50_global_lbx.curselection():
            print("Playing,", self.top_50_global_lbx.get(i))
            play_music(self.top_50_global_lbx.get(i))

    def playing_top_50_usa(self):
        for i in self.top_50_usa_lbx.curselection():
            print("Playing,", self.top_50_usa_lbx.get(i))
            play_music(self.top_50_usa_lbx.get(i))

    def playing_top_50_india(self):
        for i in self.top_50_india_lbx.curselection():
            print("Playing,", self.top_50_india_lbx.get(i))
            play_music(self.top_50_india_lbx.get(i))


if __name__ == "__main__":
    App()
