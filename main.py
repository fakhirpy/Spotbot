import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Informações de autenticação
client_id = 'seu_client_id'
client_secret = 'seu_client_secret'
redirect_uri = 'http://localhost:8888/callback'
scope = 'user-library-read playlist-modify-public'

# Criação do objeto de autenticação
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

# Criar uma nova playlist
playlist_name = 'Minhas músicas curtidas'
playlist_description = 'Todas as músicas curtidas por mim'
playlist = sp.user_playlist_create(user=sp.current_user()['id'], name=playlist_name, public=True, description=playlist_description)

# Adicionar todas as músicas curtidas à playlist
limit = 50 # definir o número de músicas a serem retornadas em cada chamada da API
offset = 0 # definir o ponto de partida da primeira chamada da API

while True:
    results = sp.current_user_saved_tracks(limit=limit, offset=offset)
    tracks = []
    for item in results['items']:
        track = item['track']['uri']
        tracks.append(track)
    sp.user_playlist_add_tracks(user=sp.current_user()['id'], playlist_id=playlist['id'], tracks=tracks)
    offset += limit
    if len(tracks) < limit:
        break
