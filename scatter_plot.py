import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from utils.dataframe_manip import *
import warnings
import argparse
import os
import sys
import time

# https://stats.stackexchange.com/questions/562203/normalizing-and-scaling-are-different
# https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0

# How to check for homogeneity ?
# https://www.statisticshowto.com/homogeneity-homogeneous/

# Scatter plot and correlation
# https://www.westga.edu/academics/research/vrc/assets/docs/scatterplots_and_correlation_notes.pdf

# Outliers detection
# https://datasciencesphere.com/analytics/5-easy-ways-to-detect-outliers-in-python/

def drawScatterPlotCorrelation(df: pd.DataFrame, feat1: str, feat2: str, \
		houses: list, colors: list, ax: plt.axes) -> None:
	for house, color in zip(houses, colors):
		house_df = df.loc[df['Hogwarts House'] == house]
		x_house_array = house_df[feat1].values
		y_house_array = house_df[feat2].values
		ax.scatter(x_house_array, y_house_array, color=color, alpha=0.15, label=house)
	if (len(feat1) > 15):
		feat1 = feat1[:15] + '\n' + feat1[15:]
	if (len(feat2) > 15):
		feat2 = feat2[:15] + '\n' + feat2[15:]
	ax.set_xlabel(feat1, fontsize=6, labelpad=-1)
	ax.set_ylabel(feat2, fontsize=6, labelpad=-1)
	ax.set_xticks([])
	ax.set_yticks([])

def drawStrongCorrelation(df: pd.DataFrame, features: list, \
		houses: list, colors: list, ax: plt.axes) -> None:
	for house, color in zip(houses, colors):
		house_df = df.loc[df['Hogwarts House'] == house]
		x_house_array = house_df[features[0]].values
		y_house_array = house_df[features[1]].values
		ax.scatter(x_house_array, y_house_array, color=color, alpha=0.5, label=house, s=100)
	if (len(features[0]) > 15):
		features[0] = features[0][:15] + '\n' + features[0][15:]
	if (len(features[1]) > 15):
		features[1] = features[1][:15] + '\n' + features[1][15:]
	ax.set_xlabel(features[0])
	ax.set_ylabel(features[1])
	ax.legend()

def scrollText(text, sec=0.04):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(sec)

def explanation1():
	scrollText("\033[03m<< Now, I'll try to find correlated or similars features between houses. >>\033[0m you declare.\n\n")
	scrollText("\n\033[03m<< I guess it's still to make us win time later ? >>\033[0m suppose McGonagall.\n\n")
	scrollText("\n\033[03m<< Indeed. If a feature is correlated to another, it won't brings new informations. \nWe can keep only one of them. >>\033[0m you say to confirm her suspicion.\n\n")
	scrollText("While she readjust her glasses on her nose, with a pleased smile, you explains to her \nthat you are going to use a scatter plot.\n")
	scrollText("You detail to her that scatter plots are useful to display relationship of \nquantitative features.\n")
	scrollText("It helps to point out overall pattern between two features. Each scatter plot can \nbe describe by the direction, form and strength/slope of the relation.\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")

def explanation2():
	scrollText("You show a particular scatter plot to McGonagall.\n")
	scrollText("\n\033[03m<< Look ! Defense Against the Dark Arts and Astronomy have a linear \ncorrelation !\n")
	scrollText("It's a linear negative correlation with a strong slope. In others words : a \nstrong association.\n")
	scrollText("It also means that the more you are good at Astronomy, the less you are good \nat Defense Against the Dark Arts. The contrary is also true. >>\033\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")

def explanation3():
	scrollText("\033[03m<< I guess some students prefers having their gaze to the stars, while \nothers prefers dueling. >>\033[0m mutters McGonagall.\n\n")
	scrollText("To distract her, you explain to her that another advantage of scatter plots is \nthat it can help detects outliers in multivariate settings.\n\n")
	input("Press enter to continue ...\n")
	os.system("clear")

if __name__ == '__main__':
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

	fig, axs = plt.subplots(10, 8, figsize=(30, 20))
	fig.suptitle('Relationship between marks\' subjects')
	idx = 0
	for i, feature1 in enumerate(numerics_df.columns):
		for feature2 in numerics_df.columns[i + 1:]:
			drawScatterPlotCorrelation(df, feature1, feature2, houses, colors, axs[int(idx / 8) % 10, idx % 8])
			idx += 1
	axs[-1, -1].axis('off')
	axs[-1, -2].axis('off')

	handles, labels = axs[0, 0].get_legend_handles_labels()
	fig.legend(handles, labels, bbox_to_anchor=[0.9, 0.11])
	plt.subplots_adjust(top=0.945, bottom=0.03, left=0.025, right=0.985, \
		hspace=0.2, wspace=0.2)
	plt.show()

	if args.expl == True:
		explanation2()

	features=['Defense Against the Dark Arts', 'Astronomy']
	fig, axs = plt.subplots(1, figsize=(30, 20))
	fig.suptitle('Strongest marks subjects correlation')
	drawStrongCorrelation(df, features, houses, colors, axs)
	plt.show()


	if args.expl == True:
		explanation3()
