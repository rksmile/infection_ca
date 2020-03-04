import pandas as pd 
import numpy as np 
import random 

individual_dict = {"id": [], "name": [], "born_immunity_integrity": [], "attained_immunity_debuff": [], "healthy_eater": [], "smoker": [], "drinker": [], "infected": [], "quarantined": [], "dead": []}

alphalist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def id_generation():
	id_num = len(individual_dict["name"])
	return id_num 


def name_generation():
	name = "%s. %s" % (alphalist[random.randint(25)], alphalist[random.randint(0, 25)])
	return name


def immune_def_born():
	random_neg = random.randint(0, 100)
	extreme_neg = random.randint(0, 100)
	integrity = 100

	if random_neg <= 15:
		integrity -= random_neg
	elif extreme_neg <= 3:
		integrity -= random.randint(34, 50)

	return integrity


def eating_habits_generator():
	randbool = random.randint(0, 2)
	h_eater = False
	if randbool == 0:
		h_eater = True

	return h_eater


def smoking_habit_generator():
	randbool = random.randint(1, 10)
	smoker = False
	if randbool < 2:
		smoker = True;

	return smoker


def drinking_habit_generator():
	randbool = random.randit(1, 100)
	drinker = False
	if randbool < 56: # based on the NSDUH 2015 stats, im not very rigorous rn 
		drinker = True

	return drinker


# other parameters are determined during the "simulation"

