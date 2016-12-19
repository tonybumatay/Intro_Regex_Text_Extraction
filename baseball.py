#!/usr/bin/python

import re
import sys, getopt, os

#Define a class for players
class Player:
	#constructor here
	def __init__(self, name):
		self.name=name
		self.num_at_bats=0
		self.numHits=0
		self.numRuns=0

	#Batting Average: (total hits)/(at bats)	
	def get_battingAverage(self):
		return float(self.numHits)/self.num_at_bats

	def get_name(self):
		return self.name

	def add_at_bat(self, at_bat):
		self.num_at_bats += at_bat

	def add_hit(self, hit):
		self.numHits += hit

	def add_run(self, run):
		self.numRuns += run

#Usage Message: We expect exactly one argument (the path to the input file)
#if less than one argument
if len(sys.argv) <2:
	sys.exit("Usage: python '%s' Filename" %sys.argv[0])

inputFile=sys.argv[1]

#if more than one argument
if len(sys.argv) >2:
	sys.exit("Too many arguments. Please provide the path to the input file as the only argument.")

#if file path is incorrect
if not os.path.exists(inputFile):
	sys.exit("Error! File '%s' was not found." %inputFile)

#Regex expessions to extract data
player_regex = re.compile("(^\w*\s\w*)")
bats_regex = re.compile("batted\s(\d)\stimes")
hits_regex = re.compile("with\s(\d)\shits")
runs_regex = re.compile("and\s(\d)\sruns")

#find and open the input file
fileName = str(sys.argv[1])
open_file = open(fileName)

#make a dictionary of players
allPlayers = dict()

#Add players to the dictionary and track their stats
for line in open_file:
	strip_line = line.rstrip()
	#locate the player's name
	player = player_regex.findall(strip_line)

	#If the line has a player, record their stats
	if player:
		numHits = hits_regex.findall(strip_line)
		num_at_bats = bats_regex.findall(strip_line)
		numRuns = runs_regex.findall(strip_line)
		

		#If a player has already been recorded, updat the stats
		if player[0] in allPlayers.keys():
			allPlayers[player[0]].add_at_bat(int(num_at_bats[0]))
			allPlayers[player[0]].add_hit(int(numHits[0]))
			allPlayers[player[0]].add_run(int(numRuns[0]))

		#If it is a new player, add a new player
		else:
			new = Player(player[0])
			new.add_hit(int(numHits[0]))
			new.add_at_bat(int(num_at_bats[0]))
			new.add_run(int(numRuns[0]))
			allPlayers[player[0]] = new

#Sort the averages for each player and print
sortedAverages	= dict()
for i in allPlayers.iterkeys():
	sortedAverages[i]= allPlayers[i].get_battingAverage()

for j in sorted(sortedAverages, key=sortedAverages.get, reverse=True):
	print (j) + ": " + "{0:.3f}".format(round(sortedAverages[j], 3))

#Close the file
open_file.close()
