# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 01:10:54 2018
This program calculates winning percentages in Black Jack, based on what value the dealer and player chooses to stand at.
@author: Anton
"""
import random
from time import time
from matplotlib import pyplot

def createDeck(noOfDecks): 
    # Used for creating a deck and also for shuffling it
    deck=[1]*noOfDecks*52
    valueArray=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    for i in range(1,noOfDecks*4+1):
        for j in range (0,13):
            deck[j+(i-1)*13]=valueArray[j]
    return deck
        
def drawCard(deck): 
    # Returns a random card and removes it from the deck
    nbrOfAces=0
    cardVal=deck.pop(random.randint(0,len(deck)-1))
    if cardVal==11:
        nbrOfAces+=1
    return[deck, cardVal, nbrOfAces]

def runGame(noOfDecks,standAt): 
    # Runs a game specified by the number of decks and where the player chooses to stand
    deck=createDeck(noOfDecks)
    handValue=0
    aces=0
    while handValue<standAt:
        if len(deck)<noOfDecks*52/2:
            deck=createDeck(noOfDecks)
        card=drawCard(deck)
        deck=card[0]
        handValue+=card[1]
        aces+=card[2]
    while aces>0 and (handValue != 21 or handValue != 20): 
        # Keep going as long as there are aces and you have not scored 20 or 21
        handValue-=10
        aces-=1
        while handValue<standAt:
            if len(deck)<noOfDecks*52/2:
              deck=createDeck(noOfDecks)
            card=drawCard(deck)
            deck=card[0]
            handValue+=card[1]
    return(handValue)
  
def checkIfWon(noOfDecks,dealerStand,playerStand): 
    # This creates a game for the dealer and player and checks who wins
    dealerResult=runGame(noOfDecks,dealerStand)
    playerResult=runGame(noOfDecks,playerStand)
    if playerResult>dealerResult and playerResult<22:
        return "Win"
    elif playerResult==dealerResult:
        return "Tie"
    else:
        return "Loss"

nbrOfGames=10
results=[1]*nbrOfGames

startTime=time()
playerStandsAt=16
for match in range (0,nbrOfGames):
  results[match]=checkIfWon(8,16,playerStandsAt)

wins=results.count("Win")
losses=results.count("Loss")
ties=results.count("Tie")
print("Player stands at: " +str(playerStandsAt))
print("Winning percentage: " +str(wins/nbrOfGames*100))
print("Losing percentage: " +str(losses/nbrOfGames*100))
print("Tie percentage: " +str(ties/nbrOfGames*100))
print("Win/loss ratio: " +str(wins/losses))
endTime=time()
print("Evaluation time: " +str(endTime-startTime) +" seconds.")

standsAt=range(16,22)

pyplot.xlabel("Player stands at")
pyplot.ylabel("Win/loss ratio")
winLossRatio=[0.38,0.42,0.41,0.36,0.26,0.11]
pyplot.plot(standsAt,winLossRatio,'*')
wins=[0.24,0.27,0.26,0.24,0.19,0.09]
pyplot.xlabel("Player stands at")
pyplot.ylabel("Ratio")
pyplot.plot(standsAt,wins,'*')
pyplot.legend(["Win/loss ratio","Win ratio"])

