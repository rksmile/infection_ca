import pandas as pd 
import numpy as np 
import random 
import sys
from coordinate_generator import get_pixels
import datetime

start = datetime.datetime.now()

filename = sys.argv[1]
size = int(sys.argv[2])

individual_dict = {"id": [], "coord" : [],"name": [], "population_density60": [], "population_density25": [], "population_density15": [], "born_immunity_integrity": [], "attained_immunity_debuff": [], "healthy_eater": [], "smoker": [], "drinker": [], "infected": [], "quarantined": [], "dead": []}

alphalist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

sixtypercent = False
twentyfpercent = False
fifteenpercent = False

scounter = 0
tcounter = 0
fcounter = 0


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


def coordinate_gen(s, t, f, size):
	sixty_used = []
	twentyf_used = []
	fifteen_used = []
	s_done = False
	t_done = False
	f_done = False
	s_counter = 0
	t_counter = 0
	f_counter = 0

	while not s_done:
		for x in range(size):
			rand = random.randint(0, len(s)-1)
			'''
			Lots of optimisation was needed here and I have gone through many itterations but I have found this to be the fastest method.
			Rearranging the conditions might yield different results but I doubt there is a noticable difference. The NONE checking is done
			because we don't want it iterating over the already assigned ones and then replacing their values. pop() I used to just lower 
			the amount of data to be sorted, this also sped it up significantly. This(outdated) configuration yielded 500k population with a time of
			3hr 11min 30sec. Current config yields 500k at a time of 1hr 44min 01sec
			'''
			if individual_dict["coord"][x] == None and individual_dict["population_density60"][x] == True and s[rand] not in sixty_used:
				sixty_used.append(s[rand])
				individual_dict["coord"][x] = s[rand]
				s.pop(rand)
				s_counter += 1
				print('\r' + str(s_counter) + "/" + str(size*.6)),


			if len(sixty_used) >= (size * .6):
				s_done = True
				break


	while not t_done:
		for i in range(size):
			rand = random.randint(0, len(t)-1)
			if individual_dict["coord"][i] == None and individual_dict["population_density25"][i] == True and t[rand] not in twentyf_used:
				twentyf_used.append(t[rand])
				individual_dict["coord"][i] = t[rand]
				t.pop(rand)
				t_counter += 1
				print('\r' + str(t_counter) + "/" + str(size*.25)),

			if len(twentyf_used) >= (size * .25):
				t_done = True
				break


	while not f_done:
		for j in range(size):
			rand = random.randint(0, len(f)-1)
			if individual_dict["coord"][j] == None and individual_dict["population_density15"][j] == True and f[rand] not in fifteen_used and individual_dict["population_density15"][j] == True:
				fifteen_used.append(f[rand])
				individual_dict["coord"][j] = f[rand]
				f.pop(rand)
				f_counter += 1
				print('\r' + str(f_counter) + "/" + str(size*.15)),

			if len(fifteen_used) >= (size * .15):
				f_done = True
				break


# other parameters are determined during the "simulation"

for x in range(size):
	individual_dict["name"].append(name_generation())
	individual_dict["id"].append(id_generation())
	individual_dict["coord"].append(None)
	individual_dict["population_density60"].append(False)
	individual_dict["population_density25"].append(False)
	individual_dict["population_density15"].append(False)
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


while not sixtypercent:
	for i in range(size):
		if individual_dict["population_density60"][i] != True:
			if random.randint(1, 100) <= 25:
				#print("here")
				individual_dict["population_density60"][i] = True
				scounter += 1

		if scounter >= (size * .6):
			sixtypercent = True
			break


while not twentyfpercent:
	for i in range(size):
		if individual_dict["population_density60"][i] != True and individual_dict["population_density25"][i] !=True:
			if random.randint(1, 100) <= 25:
				#print("here")
				individual_dict["population_density25"][i] = True
				tcounter += 1

		if tcounter >= (size * .25):
			twentyfpercent = True
			break 


while not fifteenpercent:
	for i in range(size):
		if individual_dict["population_density15"][i] != True and individual_dict["population_density25"][i] !=True and individual_dict["population_density60"][i] != True:
			if random.randint(1, 100) <= 25:
				individual_dict["population_density15"][i] = True
				fcounter += 1

		if fcounter >= (size * .15):
			fifteenpercent = True
			break


f_p, t_p, s_p = get_pixels(size)


coordinate_gen(s_p, t_p, f_p, size)

individual_df = pd.DataFrame(individual_dict, columns=["id", "coord", "name", "population_density60", "population_density25", "population_density15", "born_immunity_integrity", "attained_immunity_debuff", "healthy_eater", "smoker", "drinker", "infected", "quarantined", "dead"])

individual_df.to_csv("E:/PythonScripts/CellularAutomata/code/population_data/%s.csv" % filename)

end = datetime.datetime.now()
elapsed = end - start

print("\n")

print("Time elsapsed: {0}".format(elapsed))
