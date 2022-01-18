import math
import requests

matchesListAPILink = "https://hs-consumer-api.espncricinfo.com/v1/pages/matches/current?lang=en&latest=true"
response = requests.get(matchesListAPILink);

matches = response.json()['matches']

isLive = []

for match in matches:
    if match['status']=="Live":
        isLive += [match]


currentLive = isLive[0];

matchId = currentLive['objectId']
seriesId = currentLive['scribeId']


firstLiveMatchAPILink = "https://hs-consumer-api.espncricinfo.com/v1/pages/match/details?lang=en&seriesId=" + str(seriesId) + "&matchId=" + str(matchId) + "&latest=true";

def getText():
    newResponse = requests.get(firstLiveMatchAPILink);
    lastBallComment = newResponse.json()['recentBallCommentary']['ballComments'][0]
    ballTitle = lastBallComment['title']
    ballRuns = lastBallComment['totalRuns']
    ballNumber = lastBallComment['oversActual']
    finalOutput = str(ballNumber) + " - " + ballTitle + ", " + str(ballRuns) + " runs";
    return finalOutput
