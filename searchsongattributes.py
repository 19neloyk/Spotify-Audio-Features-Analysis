import requests
import urllib
import json

#For prettifying json: "print json.dumps(<your_json_string>, indent=4)"

def songSearchAttributes(devToken, search):
  headers = {"Authorization": "Bearer "+devToken}


  #Apply spotify item search
  itemSearchURL = "https://api.spotify.com/v1/search"
  itemSearchParams = {
      'q' : search,
      'type' : 'track',
      'market' : 'US',
      'limit' : '1'
  }
  
  itemSearchResponse = requests.get(itemSearchURL, headers = headers, params = itemSearchParams)
  #json.dumps(itemSearchResponse.json(), indent=4)

  songName = itemSearchResponse.json()["tracks"]["items"][0]["name"]
  songArtist = itemSearchResponse.json()["tracks"]["items"][0]["artists"][0]["name"]
  print("Showing attributes for "+songName+ " by "+songArtist)
  trackID = itemSearchResponse.json()["tracks"]["items"][0]["id"]

  #Get the actual item id for this track 
  getTrackAttributesURL = "https://api.spotify.com/v1/audio-features/" + trackID
  trackAttributesResponse = requests.get(getTrackAttributesURL, headers = headers)
  print(json.dumps(trackAttributesResponse.json(), indent=4))

searchQuery = ""

print("Give a spotify developer token:")
developerToken = input()
while (True):
  print("What song's traits would you like to see?")
  searchQuery = input()
  if (searchQuery == "exit"):
    break
  songSearchAttributes(developerToken, searchQuery)
