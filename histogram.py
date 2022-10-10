import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from utils.dataframe_manip import *
import warnings
import sys
import time
import argparse
import os

# https://stats.stackexchange.com/questions/562203/normalizing-and-scaling-are-different
# https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0

# How to check for homogeneity ?
# https://www.statisticshowto.com/homogeneity-homogeneous/

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
		ax.set_title(feature)

def drawErrorHistogram(df: pd.DataFrame, feature: str, houses: list, \
		colors: list, ax: plt.axes) -> None:
	houses_mean = []
	houses_std = []
	x_pos = np.arange(len(houses))
	ax.grid()
	for house in houses :
		house_df = df.loc[df['Hogwarts House'] == house]
		house_array = house_df[feature].dropna().values
		houses_mean.append(np.mean(house_array))
		houses_std.append(np.std(house_array))
	ax.bar(x_pos, houses_mean, yerr=houses_std, align='center', alpha=1, ecolor='black', capsize=10, color=colors)
	ax.set_xticks(x_pos)
	ax.set_xticklabels(houses)
	ax.set_title(feature)

def drawBoxPlot(df: pd.DataFrame, feature: str, houses: list, \
		colors: list, ax: plt.axes) -> None:
	houses_array = []
	ax.grid()
	for house in houses:
		house_df = df.loc[df['Hogwarts House'] == house]
		house_array = house_df[feature].dropna().values
		houses_array.append(house_array)
	bp = ax.boxplot(houses_array, patch_artist=True, showmeans=True, labels=houses, vert=0, notch=True)
	for patch, color in zip(bp['boxes'], colors):
		patch.set_facecolor(color)
	ax.set_title(feature)

def explanation1():
	scrollText("You install a chair for McGonagall next to you and invite her to sit.\n")
	scrollText("She accepts your offer with a little smile and put her glasses on her nose.\nShe's looking at your screen with a puzzled face as you code.\n")
	scrollText("\n\033[03m<< Ok, so here, I'm asking myself if there is any course where students' marks \nare homogeneously distributed. >>\033[0m you start.\n\n")
	scrollText("\033[03m<< Why are you doing so ? Are those marks important to determine the house ? >>\033[0m \nshe asks in return.\n\n")
	scrollText("\033[03m<< Quite the contrary. I want to discriminate students by their houses. \nSo, if a lesson, which is a feature, don't output differences between the \nfour houses, it's useless. \nI'll drop it and it'll make us win some time training our model. >>\033[0m\n\n")
	scrollText("As you finish writing your program, you explain her that histograms, a kind \nof stastical representation, are useful to observe a feature distribution.\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")

def explanation2():
	scrollText("\n\033[03m<< Ahah ! Seems like Arithmancy and Care of Magical Creatures are both \n homogeneously distributed ! Let's see it more clearly... >>\033[0m you say out loud.\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")


def explanation3():
	scrollText("\n\033[03m<< Interesting >>\033[0m McGonagall whispers.\n")
	scrollText("\n\033[03m<< I wonder if those professors have specials ways of teaching >>\033[0m she continues.\n\n")
	scrollText("As she seems interested, you propose her to visualize the mean and standard deviation \nfor those subjects.\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")


def explanation4():
	scrollText("You also decide to output a boxplot of it, as it's a representation useful to \nvisualize homogeneity.\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")


if __name__ == "__main__":
	# Just to shut up a deprecation warning from numpy which appeared in the middle of my project
	warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

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

	fig, axs = plt.subplots(3, 5, figsize=(30, 20))
	fig.suptitle('Mark\'s distribution between houses by subject')

	for idx, column in enumerate(numerics_df.columns):
		drawFeatureHistogram(df, column, houses, colors, axs[int((idx / 5) % 3), idx % 5], 15)
	axs[-1, -1].axis('off')
	axs[-1, -2].axis('off')

	handles, labels = axs[0, 0].get_legend_handles_labels()
	fig.legend(handles, labels, loc='lower right')
	plt.show()

	if args.expl == True:
		explanation2()

	features=['Arithmancy', 'Care of Magical Creatures']
	fig, axs = plt.subplots(2, figsize=(30, 20))
	fig.suptitle('Mark\'s distribution between houses by subject')

	for idx, feature in enumerate(features):
		drawFeatureHistogram(df, feature, houses, colors, axs[idx], 60)

	handles, labels = axs[0].get_legend_handles_labels()
	fig.legend(handles, labels, loc='lower right')
	plt.show()

	if args.expl == True:
		explanation3()

	normalized_df = get_mean_normalized(df, numerics_df)
	features=['Arithmancy', 'Care of Magical Creatures']
	fig, axs = plt.subplots(2, figsize=(30, 20))
	fig.suptitle('Mark\'s mean and standard deviation for each house by subject')

	for idx, feature in enumerate(features):
		drawErrorHistogram(normalized_df, feature, houses, colors, axs[idx])

	handles, labels = axs[0].get_legend_handles_labels()
	fig.legend(handles, labels, loc='lower right')
	plt.show()

	if args.expl == True:
		explanation4()

	features=['Arithmancy', 'Care of Magical Creatures']
	fig, axs = plt.subplots(2, figsize=(30, 20))
	fig.suptitle('Mark\'s mean and standard deviation for each house by subject')

	for idx, feature in enumerate(features):
		drawBoxPlot(df, feature, houses, colors, axs[idx])

	handles, labels = axs[0].get_legend_handles_labels()
	fig.legend(handles, labels, loc='lower right')
	plt.show()
