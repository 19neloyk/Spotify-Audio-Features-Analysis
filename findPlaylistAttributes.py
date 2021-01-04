import json
import spotipy
import statistics



def getPlaylistAudioAttributes(developerToken,playlistID): #Based on the first 100 tracks of a playlist (spotipy does not cover more than that)

  sp = spotipy.Spotify(auth = developerToken) #Defines the level of authorization I want to use

  playlistSongs = sp.playlist_tracks(playlistID)
  songIDList = []
  for song in playlistSongs["items"]:
    songIDList.append(song["track"]["id"])
  print(songIDList)
  playlistFeatures = sp.audio_features(songIDList)
  
  features_dict = {}
  for key in playlistFeatures[0]: #Add the numeric features to features_dict
    curValue = playlistFeatures[0][key]
    if (type(curValue) == int or type(curValue) == float):
      features_dict[key] = []

  for obj in playlistFeatures:  
    for key in features_dict: #gathering all the numerical traits for this song into the features_dict arrays
      features_dict[key].append(obj[key])
  print(features_dict)

  for key in features_dict:
    curArr = features_dict[key]
    curAverage = statistics.mean(curArr)
    curStDev = statistics.stdev(curArr)
    print("%16s         %9.2f" %(key, curAverage) + "    %9.2f" %(curStDev))

print("What is your developer token?")
token = input()
print("What is your playlist id? You get this from visiting your playlist in the browser and then typing the string of letters and numbers at the end...")
id = input()
print("Great! Let's look at audio features of the tracks in this playlist!")
print("%16s         %9s" %("Feature", "mean") + "    %9s" %("std_dev"))

getPlaylistAudioAttributes(token, id)
