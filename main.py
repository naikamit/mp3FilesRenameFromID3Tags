import eyed3
import os
from os import listdir
from os.path import isfile, join

song_list = []  # it will contain all the song names
# directory which will contain songs
loading_dir = '/home/admin/Desktop/HPHI to rename mp3 files/'

# it'll make an array of files present in a directory
allfiles = [f for f in listdir(loading_dir) if isfile(join(loading_dir, f))]

for song in allfiles:
    if (song.endswith('mp3') and
        not song.endswith('bass.mp3') and
        not song.endswith('drums.mp3') and
        not song.endswith('other.mp3') and
        not song.endswith('piano.mp3') and
        not song.endswith('vocals.mp3') and
            not song.endswith('recombined.mp3')):

        song_list.append(song)

for song in song_list:
    try:
        audiofile = eyed3.load(f'{loading_dir}{song}')  # load song's metadata

        song_title = audiofile.tag.title
        song_artist = audiofile.tag.artist

        if song_artist != None:
            os.rename(f'{loading_dir}{song}',
                      f'{loading_dir}{song_title} - {song_artist}.mp3')

    except Exception as e:
        print(e)
        continue