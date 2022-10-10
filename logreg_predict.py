import numpy as np
import pandas as pd
import argparse
import os
from utils.dataframe_manip import *
from utils.logistic_regression import *
from utils.logistic_scores import *
from utils.array_manip import *
from utils.one_vs_all import *
import sys
import time
import argparse
import os

def scrollText(text, sec=0.04):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(sec)

def explanation1():
	os.system("clear")
	scrollText("\033[03m<< Now, we can predict the corresponding houses for each student with our model.\nLet me try it on the testing set you gave me. >>\033[0m you say.\n\n")
	scrollText("\033[03m<< Go ahead. >>\033[0m replies McGonagall with restlessness in her voice.\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")

def explanation2():
	print("Prediction:")
	os.system("cat houses.csv")
	input("\nPress enter to continue ...\n")
	os.system("clear")
	scrollText("\033[03m<< Tadam ! Now all our predictions are stored inside houses.csv file !\n")
	scrollText("My work here is now done. You'll just have to use digitalis on new students informations \nto make it works. >>\033[0m you finally got up from your chair.\n\n")
	scrollText("\033[03m<< Well, thanks for everything. Hogwarts and the whole magical world is now indebted to you.\n")
	scrollText("And I may add that you showed me a new kind of magic today. >>\033[0m \nfinishes McGonagall while solemnly shaking your hand.\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")
	scrollText("\033[03m<< McGonagall, may I ask you a question ? >>\033[0m you asks.\n\n")
	scrollText("\033[03m<< Of course. What is it ? >>\033[0m\n\n")
	scrollText("\033[03m<< How are you going to access marks of students who're \nnot enrolled in Hogwarts yet ? >>\033[0m\n\n")
	scrollText("\033[03m<< ... Oh damn ... As always, I'll find a solution... >>\033[0m\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")

if __name__ == '__main__':

	# Check arguments given by user
	parser = argparse.ArgumentParser("Sorting Hat Prediction - Program description")
	parser.add_argument("dataset", type=str, help="File path of students informations to predict houses (with valid reading permission)")
	parser.add_argument("weights", type=str, help="File path of file containing algorithm weights (with valid reading permission)")
	parser.add_argument("-expl", help="Display explanation", action="store_true")
	args = parser.parse_args()
	filename = args.dataset.split("/")[-1]
	if filename != 'dataset_test.csv':
		print("\033[91mOops, this program is only for testing dataset (dataset_test.csv).\033[0m")
		print("Exiting...")
		exit()
	if not isinstance(args.dataset, str) or not os.path.isfile(args.dataset) \
		or not isinstance(args.weights,str) or not os.path.isfile(args.weights):
		parser.print_help()
		exit(1)

	if args.expl == True:
		explanation1()

	# Prepare/pre-process data for prediction
	df = get_dataframe(args.dataset)
	to_drop = ['Index', 'Hogwarts House', 'Arithmancy', 'Care of Magical Creatures', 'Defense Against the Dark Arts', 'Birthday', 'Best Hand', 'First Name', 'Last Name']
	df = df.drop(to_drop, axis=1)
	numerics_df = get_numerics(df)
	for column in numerics_df.columns:
		if df[column].isnull().values.any():
			abs_z_score = df[column].abs()
			outliers =  abs_z_score > 3
			outliers = np.asarray(abs_z_score[outliers])
			if len(outliers) > 0:
				df[column].fillna(value=df[column].median(), inplace=True)
			else:
				df[column].fillna(value=df[column].mean(), inplace=True)

	x = np.asarray(df)

	# No need to set over options because we won't train our model
	# We recuperate value from npz file
	algo = OneVsAll(x.shape[1], max_y_val=4)
	scale_values = algo.get_values_npz(filepath=args.weights)
	if scale_values is None:
		print("\033[91mOops, weight file was corrupted.\033[0m")
		print("Exiting...")
		exit()

	fqrt = scale_values[0]
	tqrt = scale_values[1]

	x_scale, _, _ = scale(x, option='robust', lst1=fqrt, lst2=tqrt)

	# Prediction
	prediction = algo.predict(x_scale)

	# Houses.csv
	if os.path.isfile('houses.csv'):
		os.remove('houses.csv')
	df = pd.DataFrame(prediction, columns=['Hogwarts House'])
	df.index.name = 'Index'
	df['Hogwarts House'].replace([0, 1, 2, 3], ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'],inplace=True)
	df.to_csv('houses.csv')

	if args.expl == True:
		explanation2()
