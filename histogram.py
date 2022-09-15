import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from typing import Tuple
from utils.dataframe_manip import *

# https://stats.stackexchange.com/questions/562203/normalizing-and-scaling-are-different
# https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0

# How to check for homogeneity ?
# https://www.statisticshowto.com/homogeneity-homogeneous/

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

if __name__ == "__main__":
	print("Which lesson at Hogwarts has a homogeneous mark's distribution between all four houses ?\n")

	df = get_dataframe('./datasets/dataset_train.csv')
	df = df.drop('Index', axis=1)
	numerics_df = get_numerics(df)
	normalized_df = get_mean_normalized(df, numerics_df)
	houses = get_houses_list(df)
	colors = ['red', 'yellow', 'blue', 'green']

	fig, axs = plt.subplots(3, 5, figsize=(30, 20))
	fig.suptitle('Mark\'s distribution between houses by subject')

	for idx, column in enumerate(numerics_df.columns):
		drawFeatureHistogram(normalized_df, column, houses, colors, axs[int((idx / 5) % 3), idx % 5], 15)
	axs[-1, -1].axis('off')
	axs[-1, -2].axis('off')

	handles, labels = axs[0, 0].get_legend_handles_labels()
	fig.legend(handles, labels, loc='lower right')
	plt.show()

	print("Seems like Arithmancy and Care of Magical Creatures are good candidates.")

	features=['Arithmancy', 'Care of Magical Creatures']
	fig, axs = plt.subplots(2, figsize=(30, 20))
	fig.suptitle('Mark\'s distribution between houses by subject')

	for idx, feature in enumerate(features):
		drawFeatureHistogram(normalized_df, feature, houses, colors, axs[idx], 60)

	handles, labels = axs[0].get_legend_handles_labels()
	fig.legend(handles, labels, loc='lower right')
	plt.show()

	print('More graphics to see ')

	print("Let's visualize mean and standard deviation on those two 'most' homogeneous features.")

	features=['Arithmancy', 'Care of Magical Creatures']
	fig, axs = plt.subplots(2, figsize=(30, 20))
	fig.suptitle('Mark\'s mean and standard deviation for each house by subject')

	for idx, feature in enumerate(features):
		drawErrorHistogram(normalized_df, feature, houses, colors, axs[idx])

	handles, labels = axs[0].get_legend_handles_labels()
	fig.legend(handles, labels, loc='lower right')
	plt.show()

	print("For homogeneity, boxplots are a more adapted visualization tool.")

	features=['Arithmancy', 'Care of Magical Creatures']
	fig, axs = plt.subplots(2, figsize=(30, 20))
	fig.suptitle('Mark\'s mean and standard deviation for each house by subject')

	for idx, feature in enumerate(features):
		drawBoxPlot(normalized_df, feature, houses, colors, axs[idx])

	handles, labels = axs[0].get_legend_handles_labels()
	fig.legend(handles, labels, loc='lower right')
	plt.show()

	print("What could it mean for our Sorting Hate algorithm ?")
	print("If we have an homogeneous distribution of a feature for the four groups, this feature may be not useful to discriminate between those groups.")
	print("We will take off the two features which seems homogeneous: Arithmancy and Care of Magical Creatures for training our model.")
