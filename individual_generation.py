import pandas as pd 
import numpy as np 
import random 
import sys

filename = sys.argv[1]
size = int(sys.argv[2])

individual_dict = {"id": [], "name": [], "born_immunity_integrity": [], "attained_immunity_debuff": [], "healthy_eater": [], "smoker": [], "drinker": [], "infected": [], "quarantined": [], "dead": []}

alphalist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def id_generation():
	id_num = len(individual_dict["name"])
	return id_num 


def name_generation():
	name = "%s. %s" % (alphalist[random.randint(0, 25)], alphalist[random.randint(0, 25)])
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
	randbool = random.randint(1, 100)
	drinker = False
	if randbool < 56: # based on the NSDUH 2015 stats, im not very rigorous rn 
		drinker = True

	return drinker


# other parameters are determined during the "simulation"

for x in range(size):
	individual_dict["name"].append(name_generation())
	individual_dict["id"].append(id_generation())
	individual_dict["born_immunity_integrity"].append(immune_def_born())
	individual_dict["attained_immunity_debuff"].append(0)
	individual_dict["healthy_eater"].append(eating_habits_generator())
	individual_dict["smoker"].append(smoking_habit_generator())
	individual_dict["drinker"].append(drinking_habit_generator())
	individual_dict["infected"].append(0)
	individual_dict["quarantined"].append(0)
	individual_dict["dead"].append(0)

ind = individual_dict["born_immunity_integrity"].index(min(individual_dict["born_immunity_integrity"]))
individual_dict["infected"][ind] = 1


individual_df = pd.DataFrame(individual_dict, columns=["id", "name", "born_immunity_integrity", "attained_immunity_debuff", "healthy_eater", "smoker", "drinker", "infected", "quarantined", "dead"])

# debug wall 
# print(individual_dict["id"][:10])
# print(individual_dict["name"][:10])
# print(individual_dict["born_immunity_integrity"][:10])
# print(individual_dict["attained_immunity_debuff"][:10])
# print(individual_dict["healthy_eater"][:10])
# print(individual_dict["smoker"][:10])
# print(individual_dict["drinker"][:10])
# print(individual_dict["infected"][:10])
# print(individual_dict["quarantined"][:10])
# print(individual_dict["dead"][:10])
# print(individual_df.head(10))

individual_df.to_csv("E:/PythonScripts/CellularAutomata/code/%s.csv" % filename)
