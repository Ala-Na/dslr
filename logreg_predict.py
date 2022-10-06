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
	parser.add_argument("weights", type=str, help="File path of file containing algorithm weights (with valid reading permission)")
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

	# Prepare/pre-process data for prediction

	df = get_dataframe(args.dataset)
	to_drop = ['Index', 'Arithmancy', 'Care of Magical Creatures', 'Defense Against the Dark Arts', 'Birthday', 'Best Hand', 'First Name', 'Last Name']
	df = df.drop(to_drop, axis=1)


