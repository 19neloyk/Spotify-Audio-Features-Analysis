# Spotify-Audio-Features-Analysis
Python script(s) that allows user to search for the audio attributes of a particular song using the Spotify API and more. 

![Example of using first function](https://github.com/19neloyk/Search-Song_Attributes/blob/main/Screen%20Shot%202021-01-01%20at%201.11.47%20AM.png)


# Instructions for `searchsongattributes.py`
Run this file by navigating to the directory it is located in and running `python searchsongattributes.py`.
Type in the Spotify developer token and enter.
Then, type the name of a song. The entered song's name does not have to be written exactly correctly.
In order to exit, type `exit`.

# Instructions for `findPlaylistAttributes.py`
Run this file by navigating to the directory it is located in and running `python findPlaylistAttributes.py`.
Type in the Spotify developer token and then enter the playlist id (which shows up when looking at the playlist on a browser; the id is the combination of letters and numbers at the end of the URL).
You then get the mean and standard deviation values for each numerical audio feature of the playlist (only considering the first 100 songs by the way).
The program automatically exits after one iteration.

# Getting a developer token from spotify
**You need a spotify developer token in order to run this script, in order to get one, go to https://developer.spotify.com/console/get-search-item/?q=abba&type=track&market=US and go click "Get Token"**

<img src="https://github.com/19neloyk/Search-Song_Attributes/blob/main/Screen%20Shot%202021-01-01%20at%201.10.45%20AM.png" width="700" height="400" />
