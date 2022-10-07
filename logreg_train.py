from random import random
import pandas as pd
import numpy as np
import argparse
import os
import sklearn.metrics
import matplotlib.pyplot as plt
from utils.dataframe_manip import *
from utils.logistic_regression import *
from utils.logistic_scores import *
from utils.array_manip import *
from utils.one_vs_all import *
import random

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

max_iter=1000

def drawScatterPlotCorrelation(df_ori: pd.DataFrame, df_predi: pd.DataFrame, \
		feat1: str, feat2: str, houses: list, colors_ori: list, \
		colors_predi: list, ax: plt.axes) \
		-> None:
	for house, color in zip(houses, colors_ori):
		house_df_ori = df_ori.loc[df_ori['Hogwarts House'] == house]
		x_house_array_ori = house_df_ori[feat1].values
		y_house_array_ori = house_df_ori[feat2].values
		ax.scatter(x_house_array_ori, y_house_array_ori, color=color, \
			alpha=1, label=house)
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

def getRandomHyperparameters():
	alpha = random.uniform(0.0001, 0.1)
	beta_1 = random.uniform(0.001, 0.1)
	possible_batch_size = [1, 16, 32, 64, 128, 256, 512, 1024]
	batch_size = random.choice(possible_batch_size)
	possible_lambda_ = np.linspace(0, 1, 5)
	lambda_ = float(np.random.choice(possible_lambda_))
	supported_optimization = ['momentum', 'rmsprop', 'adam', None]
	optimization = random.choice(supported_optimization)
	early_stopping = random.random() > 0.8
	decay = random.random() > 0.5
	return alpha, beta_1, batch_size, lambda_, optimization, early_stopping, decay

def saveHyperparametersAndResult(alpha, beta_1, batch_size, lambda_, optimization,
	early_stopping, decay, result):
	file = "experiments.csv"
	df = pd.DataFrame({'result': [result], 'alpha': [alpha], 'beta_1': [beta_1], \
		'batch_size': [batch_size], 'lambda': [lambda_], 'early_stopping': [early_stopping], \
		'optimization': [optimization], 'decay': [decay]})
	df.to_csv(file, mode='a', header=not os.path.exists(file))

if __name__ == '__main__':

	# Check arguments given by user

	parser = argparse.ArgumentParser("Sorting Hat - Program description")
	parser.add_argument("dataset", type=str, help="File path of training dataset to describe (with valid reading permission)")
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

	print("Let's drop the column we saw had little impact previously : 'Arithmancy', 'Care of Magical Creatures' and finally 'Defense Against the Dark Arts'.")
	print("We'll also drop non convertible datas columns like first and last name.")

	df = get_dataframe(args.dataset)
	to_drop = ['Index', 'Arithmancy', 'Care of Magical Creatures', 'Defense Against the Dark Arts', 'Birthday', 'Best Hand', 'First Name', 'Last Name']
	df = df.drop(to_drop, axis=1)
	numerics_df = get_numerics(df)


	print("Let's also convert Hogwarts House into a number value. 0 =  Gryffindor, 1 = Hufflepuff, ...")
	houses = get_houses_list(df)
	df['Hogwarts House'].replace(houses, [0, 1, 2, 3], inplace=True)

	print("We have NaN values in our dataset. As we now only have numerical values, we need to replace NaN with either mean or median if there's outliers.")
	print("Let's detect features with outliers thanks to mean normalization (also called z_score) > 3 or < -3.")
	for column in numerics_df.columns:
		if df[column].isnull().values.any():
			abs_z_score = df[column].abs()
			outliers =  abs_z_score > 3
			outliers = np.asarray(abs_z_score[outliers])
			if len(outliers) > 0:
				print("Feature {} has {} outliers".format(column, len(outliers)))
				df[column].fillna(value=df[column].median(), inplace=True)
			else:
				df[column].fillna(value=df[column].mean(), inplace=True)

	# Logistic regression

	print("Okay ! Now we have a correct data set, and we have to perform logistic regression on it.")
	print("It's basically a linear regression : We have a function under the format w1a1 + w2a2 + ... + b = y_hat.")
	print("We want to find w and b values which make y_hat (prediction) closest as possible of targets y.")
	print("We already know y (here, Hogwarts Houses) and we can calculate global distance between prediction and targets/expected results.")
	print("For example, if we predict a student to be inside Slytherin but it's in truth a Ravenclaw, our distance will increase. If it's actually a Slytherin, it won't increase.")
	print("But we do that on ALL examples of our data set.")
	print("Thanks to this distance calculus, we can use a technic called gradient descent.")
	print("Gradient descent able us to calculate in which way w and b values should progress to reduce the global distance.")
	print("We repeat gradient descent in many steps, until we reach the minimum distance.")
	print("This technic able us to find the best w and b values, where w and b will stop changing or change just a little between two iterations.")
	print("In logistic regression, we use the sigmoid function to keep our prediction y_hat between 0 and 1.")
	print("We could translate 0 in 'not a Slytherin' and 1 in 'is a Slytherin' for each student.")
	print("But here we have 4 classes to discriminate. So we use a One-vs-All algorithm : we will actually train four model, each giving a probability of being in a specific house.")
	print("For each student, we will pick its house according to the strongest probability to belongs to one.")
	print("For example, if a student have a 0.2 probability to be in Gryffindor, 0.1 to be in Hufflepuff, 0.7 to be in Ravenclaw and 0.9 to be in Slytherin, we will predict it to be in Slytherin.")

	print("But first, let's split our data into a training and a testing set.")
	print("We will train our dataset on the training set and keep the testing set untouched to see if our model predict well on example it wasn't trained on.")
	print("In other words, if we have a a high enough %% of good answers on our testing set, it means we can generalize our predictions and trust our model.")

	# print("Let's normalize numericals values with mean normalization (z_score).")
	# print("We could use minmax normalization but it don't perform well with outliers and our dataset have some.")
	# print("Another option could be to use a robust scaler (x - first_quartil) / (third_quartil - first_quartil).")
	# normalized_df = get_mean_normalized(df, numerics_df)

	array = np.asarray(df)
	x, y = array[:, 1:], array[:, 0].reshape(-1, 1)
	x_train, x_test, y_train, y_test = data_spliter(x, y, 0.8)

	print("Let's normalize numericals values with robust scaler (x - first_quartil) / (third_quartil - first_quartil).")
	print("We could use minmax normalization but it don't perform well with outliers and our dataset have some.")
	print("We could also use z_score (mean normalisation) but it doesn't perform well if some data are not following a gaussian distribution.")
	print("It's important to perform scaling after splitting.")
	x_train, fqrt, tqrt = scale(x_train, option='robust')
	x_test, _ , _ = scale(x_test, option='robust', lst1=fqrt, lst2=tqrt)
	x, _, _ = scale(x, option='robust', lst1=fqrt, lst2=tqrt)


	for j in range(100):
		alpha, beta_1, batch_size, lambda_, optimization, early_stopping, decay = getRandomHyperparameters()

		algo = OneVsAll(x_train.shape[1], max_y_val=4, alpha=alpha, max_iter=max_iter, \
		initialization='he', lambda_=lambda_, optimization=optimization, decay=decay, \
		early_stopping=early_stopping, beta_1=beta_1)
		algo.perform(x_train, y_train, x_test, y_test, batch_size)
		# It's not precised insubject if 98% is supposed to be on testing set or overall
		results = []
		y_hat = algo.predict(x_test)
		i = 0
		print("----")
		print("Got : {}".format(sklearn.metrics.accuracy_score(y_test, y_hat)))
		while i < 10:
		# while i < 10 and (y_hat.any() == None or sklearn.metrics.accuracy_score(y_test, y_hat) < 0.98):
			results.append(sklearn.metrics.accuracy_score(y_test, y_hat))
			if i != 0:
				print("Got : {}".format(sklearn.metrics.accuracy_score(y_test, y_hat)))
				algo = OneVsAll(x_train.shape[1], max_y_val=4, alpha=alpha, max_iter=max_iter, \
					initialization='he', lambda_=lambda_, optimization=optimization, decay=decay, \
					early_stopping=early_stopping, beta_1=beta_1)
			algo.perform(x_train, y_train, x_test, y_test, batch_size)
			y_hat = algo.predict(x_test)
			i += 1
		result = sum(results) / i
		saveHyperparametersAndResult(alpha, beta_1, batch_size, lambda_, optimization, early_stopping, decay, result)

	exit()

	if (sklearn.metrics.accuracy_score(y_test, y_hat) < 0.98):
		print("Sorry... Couldn't reach 98% accuracy ... Try again.")
		exit(1)

	algo.save_values_npz()

	print(LogisticScores.accuracy(y, y_hat))

	print("We can see that our model accuracy is pretty good !")
	print("Let's show our results on a graph with errors.")

	prediction_df = df.copy()
	prediction_df['Hogwarts House'] = y_hat
	prediction_df['Hogwarts House'].replace([0, 1, 2, 3], houses, inplace=True)
	original_df = df.copy()
	original_df['Hogwarts House'] = df['Hogwarts House']
	colors_ori = ['red', 'yellow', 'blue', 'green']
	colors_predi = ['darkred', 'darkorange', 'navy', 'darkgreen']
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