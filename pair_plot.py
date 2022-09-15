import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_classif
from utils.dataframe_manip import *

# Data engineering and feature selection
# https://medium.com/nerd-for-tech/data-engineering-a-feature-selection-example-with-the-iris-dataset-11f0554e4b00
# https://www.kaggle.com/code/bbloggsbott/feature-selection-correlation-and-p-value/notebook


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

if __name__ == '__main__':

	# seaborn library has a pair plot function, but at 42 school there not a lot
	# of space allowed to each user, so let's use matplotlib which is alreay present

	print("To select model, pair plot can be pretty informative. Let's draw one !")

	df = get_dataframe('./datasets/dataset_train.csv')
	df = df.drop('Index', axis=1)
	numerics_df = get_numerics(df)
	normalized_df = get_mean_normalized(df, numerics_df)
	houses = get_houses_list(df)
	colors = ['red', 'yellow', 'blue', 'green']

	fig, axs = plt.subplots(13, 13, figsize=(30, 20))	

	fig.suptitle('Pair plot for numerical data')

	for i, column_i in enumerate(numerics_df.columns):
		for j, column_j in enumerate(numerics_df.columns):
			axs[i, j].set_xticks([])
			axs[i, j].set_yticks([])
			if i == j:
				drawFeatureHistogram(normalized_df, column_i, houses, colors, axs[i, j], 20)
			else:
				drawScatterPlotCorrelation(normalized_df, column_i, \
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

	print("Note : You can only look at the lower or upper triangle of the pair plot, as they're reflection of each other for differents x and y axis.")

	print("What the use of that pair plot ?")
	print("It can help us to gain some knowledge on our features, and to see if some are useless and can be left out for training our model.")
	print("As seen with histogramm, for classificatio, we can left out feature with homogeneous distribution among all our classes as it won't help us discriminate.")
	print("We also saw with scatter plot that when multiple features are correlated, we can keep only one of the correlated features.")
	print("Here, we can see that some scattered plot pair don't separate the four classes very well.")
	print("We could also check their covariance matrix, for each pair of Hogwarts houses, for each subject.")

	# If possible download sklearn at 42

	print("Let's confirm our suspicion with sklearn program to select best features.")
	non_nan = normalized_df.select_dtypes(include=np.number)
	print("Here, I replace missing value (NaN) by mean, which may not always be the more adapted.")
	non_nan = non_nan.fillna(non_nan.mean())
	house_data = df['Hogwarts House'].copy()
	house_data.replace(houses, [0, 1, 2, 3], inplace=True)
	bestfeatures = SelectKBest(score_func=f_classif, k=13)
	houses_trim = bestfeatures.fit_transform(non_nan, house_data)
	for idx in range(len(non_nan.columns)):
		print('Subject: ', non_nan.columns.values[idx])
		print('score: ', bestfeatures.scores_[idx])
		print('pvalue:' , bestfeatures.pvalues_[idx], '\n')

	print("Note : A low score for a high pvalue is a sign that a feature can be dropped.")

	print("Let's drop: Arithmancy, Care of Magical Creatures, and either Defense Against the Dark Arts or Astronomy.")
	print("We can use the rest !")

	print("We also have categorical data and date in our dataset: Best Hand and Birthday.")
	print("We can modify them in numerical usable data. For example, best hand could be put to 0=right and 1=left.")
	print("And birthday can be cut into 3 field: Day of birth, month of birth, year of birth.")
	print("Are those data useful for house attribution ? Let's plot them to know.")

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

	print("Here, the scatter plot are not very informative, even more as we didn't make pair plot with numerical datas.")
	print("No correlation can be found.")
	print("But histogram show that there's an homogeneous distribution of our 4 classes for those features with small local differences.")
	print("They have little or none influence on the Hogwarts House. We also can drop them.")
