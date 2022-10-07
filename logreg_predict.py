import numpy as np
import pandas as pd
import argparse
import os
from utils.dataframe_manip import *
from utils.logistic_regression import *
from utils.logistic_scores import *
from utils.array_manip import *
from utils.one_vs_all import *

if __name__ == '__main__':

	# Check arguments given by user

	parser = argparse.ArgumentParser("Sorting Hat Prediction - Program description")
	parser.add_argument("dataset", type=str, help="File path of students informations to predict houses (with valid reading permission)")
	# parser.add_argument("weights", type=str, help="File path of file containing algorithm weights (with valid reading permission)")
	args = parser.parse_args()
	filename = args.dataset.split("/")[-1]
	if filename != 'dataset_test.csv':
		print("\033[91mOops, this program is only for testing dataset (dataset_test.csv).\033[0m")
		print("Exiting...")
		exit()
	# TODO uncomment
	# if not isinstance(args.dataset, str) or not os.path.isfile(args.dataset) \
	# 	or not isinstance(args.weights,str) or not os.path.isfile(args.weights):
	# 	parser.print_help()
	# 	exit(1)

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

	# TODO scale
	x = np.asarray(df)

	# No need to set over options because we won't train our model
	# We recuperate value from npz file
	algo = OneVsAll(x.shape[1], max_y_val=4)
	algo.get_values_npz()

	# Prediction
	prediction = algo.predict(x)

	# Check houses.csv file
	if os.path.isfile('houses.csv'):
		os.remove('houses.csv')
	df = pd.DataFrame(prediction, columns=['Index', 'Hogwarts House'])
	df.to_csv('houses.csv')
