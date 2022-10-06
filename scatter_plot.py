import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from utils.dataframe_manip import *
import warnings

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

if __name__ == '__main__':
	# Just to shut up a deprecation warning from numpy which appeared in the middle of my project
	warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

	print("Which subjects/features are similar or correlated ?")

	print("We can display relationship of quantitative features with a scatter plot.")
	print("From such a graph, we can observe an overall pattern between those two features.")
	print("Each scatter plot can be described by direction, form, and strengh/slope.")

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

	print("Look ! Defense Against the Dark Arts and Astronomy have a linear correlation !")
	print("It's a linear negative correlation with a strong slope (strong association)!")
	print("It basically means that the more you are good at Astronomy, the less you are good at Defense Against the Dark Arts. The contrary is also true.")

	features=['Defense Against the Dark Arts', 'Astronomy']
	fig, axs = plt.subplots(1, figsize=(30, 20))
	fig.suptitle('Strongest marks subjects correlation')
	drawStrongCorrelation(df, features, houses, colors, axs)
	plt.show()

	print("What does it mean for our Sorting Hat algorithm ?")
	print("Those features are correlated with each other. It's not useful to train a model with both feature, we can choose only one of them.")

	print("Another advantage of scatter plot is that it can help detect outliers values in multivariate settings.")
	print("It'll look like points anormaly far from the others. Here, it seems okay, though we could see from previous boxplot that they were some outliers for 2 lessons.")
