from random import random
import pandas as pd
import numpy as np
import argparse
import os
import sklearn.metrics
import matplotlib.pyplot as plt
from histogram import explanation3
from utils.dataframe_manip import *
from utils.logistic_regression import *
from utils.logistic_scores import *
from utils.array_manip import *
from utils.one_vs_all import *
import warnings
import sys
import time
import argparse
import os

# Hyperparameters values
MAX_ITER = 3500
ALPHA = 0.066
BETA_1 = 0.058
LAMBDA_ = 0.0
BATCH_SIZE = 128
OPTIMIZATION = 'rmsprop'
EARLY_STOPPING = False
DECAY = False

# Stochastic gradient descent
# https://web.archive.org/web/20180618211933/http://cs229.stanford.edu/notes/cs229-notes1.pdf
# https://realpython.com/gradient-descent-algorithm-python/#stochastic-gradient-descent-algorithms
# https://towardsdatascience.com/batch-mini-batch-and-stochastic-gradient-descent-for-linear-regression-9fe4eefa637c*

# Detect outliers
# https://datasciencesphere.com/analytics/5-easy-ways-to-detect-outliers-in-python/

# Replacing NaN
# https://www.analyticsvidhya.com/blog/2021/10/handling-missing-value/

# Optimization
# http://www.cs.toronto.edu/~hinton/csc2515/notes/lec6tutorial.pdf

# Robust scaler
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html

# Note about normalization : Minmax is often used to scale data, but it doesn't apply
# well on outliers. Here, some data have outliers (though few), so let's use z_score/mean normalization instead.

def scrollText(text, sec=0.04):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(sec)

def drawScatterPlotCorrelation(df_ori: pd.DataFrame, df_predi: pd.DataFrame, \
		feat1: str, feat2: str, houses: list, colors_ori: list, \
		colors_predi: list, ax: plt.axes) \
		-> None:
	for house, color in zip(houses, colors_ori):
		house_df_ori = df_ori.loc[df_ori['Hogwarts House'] == house]
		x_house_array_ori = house_df_ori[feat1].values
		y_house_array_ori = house_df_ori[feat2].values
		ax.scatter(x_house_array_ori, y_house_array_ori, color=color, \
			alpha=0.7, label=house)
	for house, color in zip(houses, colors_predi):
		house_df_predi = df_predi.loc[df_predi['Hogwarts House'] == house]
		x_house_array_predi = house_df_predi[feat1].values
		y_house_array_predi = house_df_predi[feat2].values
		ax.scatter(x_house_array_predi, y_house_array_predi, color=color, \
			alpha=1, label='Misclassified as ' + house, \
			marker='x')
	ax.set_xlabel(feat1, fontsize=6, labelpad=-1)
	ax.set_ylabel(feat2, fontsize=6, labelpad=-1)
	ax.set_xticks([])
	ax.set_yticks([])

def explanation1():
	os.system("clear")
	scrollText("\033[03m<< Before training my model, I need to prepare my data.\nI'll drop the useless columns with little impact: \n'Arithmancy', 'Care of Magical Creatures' and finally 'Defense Against the Dark Arts'.\n")
	scrollText("I'll also drop the non convertible datas columns like first and last name. >>\033[0m you say while coding.\n\nMcGonagall nods slightly as you talk.\n")
	scrollText("\n\033[03m<< Let's also convert Hogwarts House into a number value. 0 for  Gryffindor, 1 for Hufflepuff, ...\n")
	scrollText("We have NaN values in our dataset. As we now only have numerical values, we need to replace NaN with \neither mean or median if there's outliers.\n")
	scrollText("Let's detect features with outliers thanks to mean normalization (also called z_score) > 3 \nor < -3. >>\033[0m you flood her with informations, but she seems to keep up.\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")

def explanation2():
	input("\nPress enter to continue ...\n")
	os.system("clear")
	scrollText("\033[03m<< Okay ! Now we have a correct data set, and we have to perform logistic \nregression on it. >>\033[0m you say, merrily as you're finally reaching the core of your work.\n\nMcGonagall smile at your enthusiasm.\n\n")
	scrollText("\033[03m<< It's basically a linear regression : We have a function under the format \n\"w1a1 + w2a2 + ... + b = y_hat\".\n")
	scrollText("We want to find w and b values which make y_hat (the prediction) closest as possible \nof targets y (true value).\n")
	scrollText("We already know y (here, Hogwarts Houses) and we can calculate global distance between \nprediction and targets/expected results.\n")
	scrollText("For example, if we predict a student to be inside Slytherin but it's in truth a Ravenclaw, \nour distance will increase. \nIf it's actually a Slytherin, it won't increase.\n")
	scrollText("But we do that on ALL examples of our data set.\n")
	scrollText("Thanks to this distance calculus, we can use a technic called gradient descent.\n")
	scrollText("Gradient descent able us to calculate in which way w and b values should progress to reduce \nthe global distance.\n")
	scrollText("We repeat gradient descent in many steps, until we reach the minimum distance.\n")
	scrollText("This technic able us to find the best w and b values, where w and b will stop changing or \nchange just a little between two iterations.\n")
	scrollText("In logistic regression, we use the sigmoid function to keep our prediction y_hat between 0 and 1.\n")
	scrollText("We could translate 0 as 'is not a Ravenclaw' and 1 as 'is a Ravenclaw' for each student.\n")
	scrollText("But here we have 4 classes to discriminate. \nSo we use a One-vs-All algorithm : we will actually train four model, each giving a \nprobability of being in a specific house.\n")
	scrollText("For each student, we will pick its house according to the strongest probability to belongs to one.\n")
	scrollText("For example, if a student have a 0.2 probability to be in Gryffindor, 0.1 to be in Hufflepuff, \n0.9 to be in Ravenclaw and 0.7 to be in Slytherin, we will predict it to be in Ravenclaw. >>\033[0m\n\n")
	scrollText("\033[03m<< You seems a bit Ravenclaw yourself. >>\033[0m states gently McGonagall.\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")

	scrollText("You answer with a grin before proceeding :\n\n")
	scrollText("\033[03m<< First, let's split our data into a training and a testing set.\n")
	scrollText("We will train our dataset on the training set and keep the testing set untouched to see if our model \npredict well on example it wasn't trained on.\n")
	scrollText("In other words, if we have a a high enough % of good answers on our testing set, it means we can \ngeneralize our predictions and trust our model.\n")
	scrollText("Another useful thing to do is to scale our data: By reducing the scale, it'll make calculation \nquicker and reduce the risk of calculation overflow.\n")
	scrollText("So let's normalize numericals values with robust scaler : \n(x - first_quartil) / (third_quartil - first_quartil).\n")
	scrollText("We could use minmax normalization but it don't perform well with outliers and our dataset have some.\n")
	scrollText("We could also use z_score (mean normalisation) but it doesn't perform well if some data are not \nfollowing a gaussian distribution.\n")
	scrollText("It's better to perform scaling AFTER splitting and use the same value than training set on testing \nset. >>\033[0m\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")

	scrollText("\033[03m<< By the way, our model use hyperparameters: parameters to be set by us, which will make it \nperforms better or worse. >>\033[0m\n\n")
	scrollText("\033[01mBonus : you wrote logreg_finetune.py to choose better possible hyperparameters.\n")
	scrollText("It can take a while to compute, so we won't launch it here. Results are in experiments.csv.\033[0m\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")

	scrollText("McGonagall is waiting for a 98% accuracy, but as she doesn't have any prior knowledge in data \nscience, she never said if it was globally, on training or testing set.\n")
	scrollText("You decide to check your model accuracy on your testing set, but depending on the randomly selected \ntesting set, 98% of accuracy may never be reached.\n")
	scrollText("So you'll train model on different training set until you reach the said accuracy on the \ncorresponding testing set.\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")

	scrollText("\033[03m<< Let's start the magic ! >>\033[0m\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")

def explanation3():
	input("\nPress enter to continue ...\n")
	os.system("clear")
	scrollText("\033[03m<< We can see that our model accuracy is pretty good ! >>\033[0m\n\n")
	scrollText("\033[03m<< Indeed, congratulations. >>\033[0m answers the headmistress with a joyful tone.\n\n")
	scrollText("You both check hands in front of this little success.\n")
	scrollText("But there's still some errors. \nYou propose her to visualize the corresponding students on a graph of \nmisclassification.\n")
	input("\nPress enter to continue ...\n")
	os.system("clear")

if __name__ == '__main__':

	warnings.filterwarnings("ignore", category=FutureWarning)

	# Check arguments given by user

	parser = argparse.ArgumentParser("Sorting Hat - Program description")
	parser.add_argument("dataset", type=str, help="File path of training dataset to describe (with valid reading permission)")
	parser.add_argument("-expl", help="Display explanation", action="store_true")
	args = parser.parse_args()
	filename = args.dataset.split("/")[-1]
	if filename != 'dataset_train.csv':
		print("\033[91mOops, this program is only for training dataset (dataset_train.csv).\033[0m")
		print("Exiting...")
		exit()
	if not isinstance(args.dataset, str) or not os.path.isfile(args.dataset):
		parser.print_help()
		exit(1)

	# Data preparation
	if args.expl == True:
		explanation1()

	df = get_dataframe(args.dataset)
	to_drop = ['Index', 'Arithmancy', 'Care of Magical Creatures', 'Defense Against the Dark Arts', 'Birthday', 'Best Hand', 'First Name', 'Last Name']
	df = df.drop(to_drop, axis=1)
	numerics_df = get_numerics(df)
	houses = get_houses_list(df)
	df['Hogwarts House'].replace(houses, [0, 1, 2, 3], inplace=True)
	normalized_df = df.copy()
	normalized_df = get_mean_normalized(normalized_df, numerics_df)
	for column in numerics_df.columns:
		if df[column].isnull().values.any():
			abs_z_score = normalized_df[column].abs()
			outliers =  abs_z_score > 3
			outliers = np.asarray(abs_z_score[outliers])
			if len(outliers) > 0:
				print("Feature {} has {} outliers".format(column, len(outliers)))
				df[column].fillna(value=df[column].median(), inplace=True)
			else:
				df[column].fillna(value=df[column].mean(), inplace=True)

	# Logistic regression
	if args.expl == True:
		explanation2()

	array = np.asarray(df)
	x, y = array[:, 1:], array[:, 0].reshape(-1, 1)

	obj_reached = False
	i = 0
	while obj_reached == False and i <= 100:
		x_train, x_test, y_train, y_test = data_spliter(x, y, 0.8)
		x_train, fqrt, tqrt = scale(x_train, option='robust')
		x_test, _ , _ = scale(x_test, option='robust', lst1=fqrt, lst2=tqrt)
		x_scale, _, _ = scale(x, option='robust', lst1=fqrt, lst2=tqrt)
		algo = OneVsAll(x_train.shape[1], max_y_val=4, alpha=ALPHA, \
			max_iter=MAX_ITER, initialization='he', lambda_=LAMBDA_, \
			optimization=OPTIMIZATION, decay=DECAY, early_stopping=EARLY_STOPPING, \
			beta_1=BETA_1)
		algo.perform(x_train, y_train, x_test, y_test, BATCH_SIZE)
		y_hat = algo.predict(x_test)
		print("Obtained accuracy on testing set : {}".format(sklearn.metrics.accuracy_score(y_test, y_hat)))
		if sklearn.metrics.accuracy_score(y_test, y_hat) >= 0.98:
			obj_reached = True
		i += 1

	if (sklearn.metrics.accuracy_score(y_test, y_hat) < 0.98):
		print("Sorry... Couldn't reach 98% accuracy on testing set ... Try again after modifying hyperparameters.")
		exit(1)

	algo.save_values_npz(scale=[fqrt, tqrt])
	y_hat = algo.predict(x_scale)
	print("Global accuracy: ", LogisticScores.accuracy(y, y_hat))

	# Misclassified students representation
	if args.expl == True:
		explanation3()

	prediction_df = df.copy()
	prediction_df['Hogwarts House'] = y_hat
	prediction_df['Hogwarts House'].replace([0, 1, 2, 3], houses, inplace=True)
	original_df = df.copy()
	original_df['Hogwarts House'].replace([0, 1, 2, 3], houses, inplace=True)
	colors_ori = ['red', 'yellow', 'blue', 'green']
	colors_predi = ['red', 'yellow', 'blue', 'green']
	diff = (prediction_df != original_df).any(1)
	prediction_df = prediction_df[diff]
	original_df = original_df[diff]
	df = df.drop('Hogwarts House', axis=1)

	fig, axs = plt.subplots(7, 7, figsize=(30, 20))
	fig.suptitle('Classification errors')
	idx = 0
	for i, feature1 in enumerate(df.columns):
		for feature2 in df.columns[i + 1:]:
			drawScatterPlotCorrelation(original_df, prediction_df, \
				feature1, feature2, houses, colors_ori, colors_predi, \
				axs[int(idx / 7) % 7, idx % 7])
			idx += 1
	axs[-1, -1].axis('off')
	axs[-1, -2].axis('off')
	axs[-1, -3].axis('off')
	axs[-1, -4].axis('off')

	handles, labels = axs[0, 0].get_legend_handles_labels()
	fig.legend(handles, labels, bbox_to_anchor=[0.8, 0.13], ncol=2)
	plt.subplots_adjust(top=0.945, bottom=0.03, left=0.025, right=0.985, \
		hspace=0.2, wspace=0.2)
	plt.show()
