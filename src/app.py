import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  

load_dotenv()

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


client_id = os.environ.get("CLIENT_ID")  
client_secret = os.environ.get("CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)


artist_id = '49qiE8dj4JuNdpYGRPdKbF'
top_tracks = sp.artist_top_tracks(artist_id, country='US')  

data = []


if top_tracks and 'tracks' in top_tracks:
    for track in top_tracks['tracks']:
        nombre = track["name"]
        popularidad = track["popularity"]
        duracion_ms = track["duration_ms"]
        duracion_s = duracion_ms / 1000  

     
        data.append({"Nombre": nombre, "Popularidad/100": popularidad, "Duración(s)": duracion_s})


for item in data:
    print(item)


tracks_df = pd.DataFrame.from_records(data)


ds_top3 = tracks_df.head(n=3)


scatter_plot = sns.scatterplot(data=ds_top3, x="Popularidad/100", y="Duración(s)")


scatter_plot.set_title("Top 3 Tracks: Popularity vs Duration")
scatter_plot.set_xlabel("Popularity")
scatter_plot.set_ylabel("Duration (seconds)")


plt.show()