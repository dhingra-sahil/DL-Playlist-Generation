### This script access data from the Phish.net API
### https://docs.phish.net
### Warning! limit use of this api to download and cache data locally
### too many or too large API calls and the app will be shutdown by API admin

import json
import pandas as pd
import requests
from tqdm import tqdm

print("Getting Setlist Data...")
# songNetwork API Key - get one for free on: https://phish.net/api
apiKey = '1512F21F881B46EA6528' 

# get song data
songLink = 'https://api.phish.net/v5/songs.json?apikey='+apiKey
songFile = requests.get(songLink)
songData = json.loads(songFile.text)['data']
songDF = pd.DataFrame({
    'songid': [ int(s['songid']) for s in songData ],
    'artist': [ s['artist'] for s in songData ],
    'times_played': [ int(s['times_played']) for s in songData ],
    'last_played': [ s['last_played'] for s in songData ],
    'debut': [ s['debut'] for s in songData ]
})

# get show data
showLink = 'https://api.phish.net/v5/shows.json?apikey='+apiKey
showFile = requests.get(showLink)
showDict = json.loads(showFile.text)['data']
allPhishShows = [ int(sh['showid']) for sh in showDict if sh['artistid']=='1' ]

# get setlist data
setLink = 'https://api.phish.net/v5/setlists.json?apikey='+apiKey
setFile = requests.get(setLink)
setDict = json.loads(setFile.text)['data']

# subset of desired keys from the setlist data, and datatypes
setKeys = {
    'showdate':str,   # date of the concert
    'set':str,        # set of the show (1,2,3 or encore)
    'position':int,   # relative position in the show
    'songid':int,     # song id number
    'slug':str,       # song name
    'trans_mark':str, # song transition marker
    'gap':int,        # number of shows since the song last played
    'isjam':str,      # categorical - "jam" song
    'city':str,       # venue city
    'state':str,      # venue state
    'country':str,    # venue country
    'venueid':int,    # venue id number
    'tourid':int,     # which tour the show was part of
    'showlength':int  # number of songs in the show max(position)
}

print('Parsing setlist data...')

# this parses the setlists into a dataframe indexed by song
# setlist withs missing keys/values are excluded
allPhishSets = { k:[] for k in setKeys.keys() }
for showid in tqdm(allPhishShows):
    fullSet = {}
    setlist = [
        d for d in setDict if 'showid' in d and int(d['showid'])==showid
    ]
    for k,v in setKeys.items():
        if k=='showlength': fullSet[k] = [len(setlist)]*len(setlist)
        else: fullSet[k] = [ v(d.get(k)) for d in setlist ]
    if any(None in v for v in fullSet.values()):
        continue  #skips sets with incomplete information
    else:
        allPhishSets = {
            k: allPhishSets.get(k, []) + fullSet.get(k, []) for k in setKeys
        }

allPhishDF = pd.DataFrame(data=allPhishSets).merge(songDF,on='songid',how='left')

with open('../data/allphishsets.json', 'w') as file:
    file.write(json.dumps(allPhishDF.to_dict(orient='list')))

print("Complete!")
