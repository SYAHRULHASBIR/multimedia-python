from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('/workspaces/multimedia-python/audio.jpg.mp3')

# Menyimpan file audio
audio.export('result.mp3', format='mp3')