import tkinter as tk
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
CLIENT_ID = 'af457717a70945edbe2e5689885fb29f'
CLIENT_SECRET = 'eeef4c9cfe934471abe67f790cd53e83'
REDIRECT_URI = 'http://localhost:8888/callback'

# Spotify authentication
sp = Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                       client_secret=CLIENT_SECRET,
                                       redirect_uri=REDIRECT_URI,
                                       scope="user-read-playback-state,user-modify-playback-state,playlist-read-private,user-read-recently-played"))

# Tkinter setup
root = tk.Tk()
root.title("Spotify API App")
root.geometry("600x300")

def get_active_device():
    devices = sp.devices()
    if devices['devices']:
        return devices['devices'][0]['id']
    else:
        return None

def play():
    device_id = get_active_device()
    if device_id:
        sp.start_playback(device_id=device_id)
    else:
        print("No active device found")

def pause():
    device_id = get_active_device()
    if device_id:
        sp.pause_playback(device_id=device_id)
    else:
        print("No active device found")

def next_track():
    device_id = get_active_device()
    if device_id:
        sp.next_track(device_id=device_id)
    else:
        print("No active device found")

def previous_track():
    device_id = get_active_device()
    if device_id:
        sp.previous_track(device_id=device_id)
    else:
        print("No active device found")

def get_recent_playlists():
    playlists = sp.current_user_playlists(limit=10)
    playlist_data = []
    for playlist in playlists['items']:
        playlist_data.append((playlist['name'], playlist['uri']))
    return playlist_data

def get_recent_songs():
    recent_tracks = sp.current_user_recently_played(limit=25)
    songs = []
    for item in recent_tracks['items']:
        track = item['track']
        song_info = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'uri': track['uri']
        }
        songs.append(song_info)
    return songs

def play_playlist(uri):
    device_id = get_active_device()
    if device_id:
        sp.start_playback(device_id=device_id, context_uri=uri)
    else:
        print("No active device found")

def play_song(uri):
    device_id = get_active_device()
    if device_id:
        sp.start_playback(device_id=device_id, uris=[uri])
    else:
        print("No active device found")        

def on_playlist_select(event):
    selected_index = playlist_listbox.curselection()
    if selected_index:
        selected_uri = playlist_uris[selected_index[0]]
        play_playlist(selected_uri)

def on_song_select(event):
    selected_index = recent_song_listbox.curselection()
    if selected_index:
        selected_uri = song_uris[selected_index[0]]
        play_song(selected_uri)       

# Fetch recent playlists
playlists = get_recent_playlists()
playlist_names = [playlist[0] for playlist in playlists]
playlist_uris = [playlist[1] for playlist in playlists]

recent_songs = get_recent_songs()
song_names = [song['name'] + ' - ' + song['artist'] for song in recent_songs]
song_uris = [song['uri'] for song in recent_songs]

# Create Tkinter widgets
play_button = tk.Button(root, text="Play", command=play)
play_button.grid(row=0, column=2, pady=10, padx=10)

pause_button = tk.Button(root, text="Pause", command=pause)
pause_button.grid(row=0, column=1, pady=10, padx=10)

next_button = tk.Button(root, text="Next", command=next_track)
next_button.grid(row=1, column=2, pady=10, padx=10)

prev_button = tk.Button(root, text="Previous", command=previous_track)
prev_button.grid(row=1, column=1, pady=10, padx=10)

playlist_listbox = tk.Listbox(root, width=30)
playlist_listbox.grid(row=0,rowspan=2, column=0, pady=10, padx=10)
for name in playlist_names:
    playlist_listbox.insert(tk.END, name)

playlist_listbox.bind('<<ListboxSelect>>', on_playlist_select)

recent_song_listbox = tk.Listbox(root, width=30)
recent_song_listbox.grid(row= 0, rowspan=2, column=3, pady=10, padx=10)
for name in song_names:
    recent_song_listbox.insert(tk.END, name)

recent_song_listbox.bind('<<ListboxSelect>>', on_song_select)

root.mainloop()