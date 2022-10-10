import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_classif
from utils.dataframe_manip import *
import warnings
import sys
import time
import argparse
import os

# Data engineering and feature selection
# https://medium.com/nerd-for-tech/data-engineering-a-feature-selection-example-with-the-iris-dataset-11f0554e4b00
# https://www.kaggle.com/code/bbloggsbott/feature-selection-correlation-and-p-value/notebook

def scrollText(text, sec=0.04):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(sec)

def drawFeatureHistogram(df: pd.DataFrame, feature: str, houses: list, \
		colors: list, ax: plt.axes, bins: int) -> None:
	for house, color in zip(houses, colors):
		house_df = df.loc[df['Hogwarts House'] == house]
		house_array = house_df[feature].dropna().values
		ax.hist(house_array, bins=bins, color=color, alpha=0.5, label=house, edgecolor='black')

def drawNonOverlappingFeatureHistogram(df: pd.DataFrame, feature: str, houses: list, \
		colors: list, ax: plt.axes, bins: int) -> None:
	houses_array = []
	for house in houses:
		house_df = df.loc[df['Hogwarts House'] == house]
		houses_array.append(house_df[feature].dropna().values)
	ax.hist(houses_array, bins=bins, color=colors, alpha=0.5, label=houses, edgecolor='black')

def drawScatterPlotCorrelation(df: pd.DataFrame, feat1: str, feat2: str, \
		houses: list, colors: list, ax: plt.axes) -> None:
	for house, color in zip(houses, colors):
		house_df = df.loc[df['Hogwarts House'] == house]
		x_house_array = house_df[feat1].values
		y_house_array = house_df[feat2].values
		ax.scatter(x_house_array, y_house_array, color=color, alpha=0.1, label=house)

def explanation1():
	scrollText("You continue your data visualization journey.\n\n")
	scrollText("\033[03m << To select model, pair plot can be pretty informative. Let's draw one ! >>\033[0m\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")

def explanation2():
	scrollText("As you precise to McGonagall that she can only look at one of the lower or upper triangle \nof the pair plot (because they're reflection of each other for different \nx and y axis), she asks you :\n\n")
	scrollText("\033[03m<< What is the use of that pair plot exactly ? >>\033[0m\n\n")
	scrollText("You answer that it's a pratical way to visualize what you saw before in one go.\n")
	scrollText("It can help to gain some knowledge on our features, and to see if some are \nuseless and can be left out for training our model.\n")
	scrollText("Like we saw with histograms, for classification, we can left out feature with \nhomogeneous distribution among all our classes as it won't help us discriminate.\n")
	scrollText("\nWe also saw with scatter plots that when multiple features are correlated, we can \nkeep only one of them.\n")
	scrollText("\nHere, we can see that some scatter plot pairs don't separate the four classes \nvery well in a 2D representation. But it doesn't means they're not significant.\n")
	scrollText("We could also check the covariance matrix, for each pair of Hogwarts houses, \non each subject.\n\n")
	scrollText("\033[03m<< Let's confirm our observations with sklearn program to select best \nfeatures. >>\033[0m you propose as an experiment.\n\n")
	scrollText("\033[03m<< By the way, here I'll replace missing values by mean of each feature. It may not \nalways be the more adapted solution. >>\033[0m you say as you're coding.\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")

def explanation3():
	input("Press enter to continue ...\n")
	os.system("clear")
	scrollText("\033[03m<< A low score for a high pvalue is a sign that a feature can be dropped. >>\033[0m \nyou explain.\n\n")
	scrollText("You summarize to her that you'll be dropping Arithmancy, Care of Magical Creatures, \nand either Defense Against the Dark Arts or Astronomy.\n")
	scrollText("But you'll be using the rest !\n\n")
	scrollText("\033[03m<< We also have categorical data and date in our dataset: Best Hand and Birthday. >>\033[0m \nyou continue your explanations.\n\n")
	scrollText("\033[03m<< We can modify them in numerical usable data. For example, best hand could be put to \n0=right and 1=left.\n")
	scrollText("And birthday can be cut into 3 field: Day of birth, month of birth, year of birth.\n")
	scrollText("Are those data useful for house attribution ? Let's do a pair plot of them to know. >>\033[0m\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")

def explanation4():
	scrollText("After displaying them, you say that those late scatter plots are not very informatives.\n")
	scrollText("No correlation can be found, for example.\n")
	scrollText("But histograms show that there's an homogeneous distribution of our 4 classes on \nthose features, with small local differences.\n")
	scrollText("It means they have little or none influence on the Hogwarts House attribution. \nYou declare you also can drop them for your model.\n\n")

if __name__ == '__main__':
	# Just to shut up a deprecation warning from numpy which appeared in the middle of my project
	warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

	# seaborn library has a pair plot function, but at 42 school there not a lot
	# of space allowed to each user, so let's use matplotlib which is alreay present

	parser = argparse.ArgumentParser("Hogwarts Students Histogram - Program description")
	parser.add_argument("-expl", help="Display explanation", action="store_true")
	args = parser.parse_args()

	if args.expl == True:
		explanation1()

	df = get_dataframe('./datasets/dataset_train.csv')
	df = df.drop('Index', axis=1)
	numerics_df = get_numerics(df)
	houses = get_houses_list(df)
	colors = ['red', 'yellow', 'blue', 'green']
	fig, axs = plt.subplots(13, 13, figsize=(30, 20))
	fig.suptitle('Pair plot for numerical data')
	for i, column_i in enumerate(numerics_df.columns):
		for j, column_j in enumerate(numerics_df.columns):
			axs[i, j].set_xticks([])
			axs[i, j].set_yticks([])
			if i == j:
				drawFeatureHistogram(df, column_i, houses, colors, axs[i, j], 20)
			else:
				drawScatterPlotCorrelation(df, column_i, \
					column_j, houses, colors, axs[i, j])
			if j == 0:
				label = column_i
				if len(label) > 15:
					label = label[:15] + '\n' + label[15:]
				axs[i, j].set_ylabel(label, fontsize=6, labelpad=-1)
			if i == 12:
				label = column_j
				if len(label) > 15:
					label = label[:15] + '\n' + label[15:]
				axs[i, j].set_xlabel(label, fontsize=6, labelpad=-1)

	handles, labels = axs[0, 0].get_legend_handles_labels()
	fig.legend(handles, labels, bbox_to_anchor=[0.9, 0.99], ncol=4)
	plt.subplots_adjust(top=0.945, bottom=0.03, left=0.025, right=0.985, \
		hspace=0.2, wspace=0.2)
	plt.show()

	if args.expl == True:
		explanation2()

	non_nan = df.select_dtypes(include=np.number)
	non_nan = non_nan.fillna(non_nan.mean())
	house_data = df['Hogwarts House'].copy()
	house_data.replace(houses, [0, 1, 2, 3], inplace=True)
	bestfeatures = SelectKBest(score_func=f_classif, k=13)
	houses_trim = bestfeatures.fit_transform(non_nan, house_data)
	for idx in range(len(non_nan.columns)):
		print('Subject: ', non_nan.columns.values[idx])
		print('score: ', bestfeatures.scores_[idx])
		print('pvalue:' , bestfeatures.pvalues_[idx], '\n')

	if args.expl == True:
		explanation3()

	df['Best Hand'] = df['Best Hand'].map({'Right': 0, 'Left': 1})
	df['Birthday'] = pd.to_datetime(df['Birthday'])
	df['Birth Day'] = df['Birthday'].dt.day
	df['Birth Month'] = df['Birthday'].dt.month
	df['Birth Year'] = df['Birthday'].dt.year
	non_num_df = df[['Hogwarts House', 'Best Hand', 'Birth Day', 'Birth Month', 'Birth Year']]

	fig, axs = plt.subplots(4, 4, figsize=(30, 20))
	fig.suptitle('Pair plot for categorical data')
	for i, column_i in enumerate(non_num_df.columns[1:]):
		for j, column_j in enumerate(non_num_df.columns[1:]):
			if i == j:
				drawNonOverlappingFeatureHistogram(non_num_df, column_i, houses, colors, axs[i, j], 31)
			else:
				drawScatterPlotCorrelation(non_num_df, column_i, \
					column_j, houses, colors, axs[i, j])
			if j == 0:
				label = column_i
				if len(label) > 15:
					label = label[:15] + '\n' + label[15:]
				axs[i, j].set_ylabel(label, fontsize=12)
			if i == 3:
				label = column_j
				if len(label) > 15:
					label = label[:15] + '\n' + label[15:]
				axs[i, j].set_xlabel(label, fontsize=12)
	handles, labels = axs[0, 0].get_legend_handles_labels()
	fig.legend(handles, labels, bbox_to_anchor=[0.9, 0.99], ncol=4)
	plt.subplots_adjust(top=0.945, bottom=0.07, left=0.05, right=0.985, \
		hspace=0.2, wspace=0.2)
	plt.show()

	if args.expl == True:
		explanation4()
