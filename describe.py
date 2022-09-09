import pandas as pd
import numpy as np
import argparse
import os
import math

def getDataFrame(filepath: str) -> pd.DataFrame:
	try:
		datas = pd.read_csv(filepath)
		return datas
	except:
		print("\033[91mOops, can't extract datas from {} data file.\033[0m".\
			format(filepath))
		print("\033[02;03mHint: Check file rights, file type, ...\033[0m")
		print("Exiting...")
		exit()

def getNumerics(df: pd.DataFrame) -> pd.DataFrame:
	no_index = df.drop('Index', axis=1)
	numerics_datas = no_index.select_dtypes(include=np.number)
	# For test set, column 'House' is empty and considered a numeric column as
	# NaN is a number. We drop columns containing only NaN as a precaution.
	numerics_datas = numerics_datas.dropna(how='all', axis=1)
	return numerics_datas

def countFeatures(df: pd.DataFrame) -> np.ndarray:
	count = np.zeros(len(df.columns))
	for idx, column in enumerate(df.columns):
		count[idx] = df[column].count()
	return count

def meanFeatures(df: pd.DataFrame, count: np.ndarray) -> np.ndarray:
	mean =  np.zeros(len(df.columns))
	for idx, column in enumerate(df.columns):
		mean[idx] = df[column].sum() / count[idx]
	return mean

def stdFeatures(df: pd.DataFrame, mean: np.ndarray, count: np.ndarray) -> np.ndarray:
	# Please note that pandas std function behave differently of numpy std
	# Here, we reproduce the same output as numpy
	std =  np.zeros(len(df.columns))
	for idx, column in enumerate(df.columns):
		for value in df[column]:
			if not math.isnan(value):
				std[idx] += (value - mean[idx]) ** 2
		std[idx] = math.sqrt(std[idx] / count[idx])
	return std

def minFeatures(df: pd.DataFrame) -> np.ndarray:
	minimum = np.zeros(len(df.columns))
	for idx, column in enumerate(df.columns):
		for row, value in enumerate(df[column]):
			if row == 0 or math.isnan(minimum[idx]) or ((not math.isnan(value)) \
					and value < minimum[idx]):
				minimum[idx] = value
	return minimum

def maxFeatures(df: pd.DataFrame) -> np.ndarray:
	maximum = np.zeros(len(df.columns))
	for idx, column in enumerate(df.columns):
		for row, value in enumerate(df[column]):
			if row == 0 or math.isnan(maximum[idx]) or ((not math.isnan(value)) \
					and value > maximum[idx]):
				maximum[idx] = value
	return maximum

# Beware ! There's more than one way to calculate percentile and if it's
# compared with another function, it may differs.
# Function for p = 50 is calculus of median
def percentileFeatures(df: pd.DataFrame, p: int) -> np.ndarray:
	assert isinstance(p, int) and not (p > 100 or p < 0)
	perc = np.zeros(len(df.columns))
	for idx, column in enumerate(df.columns):
		column = df[column].dropna()
		sorted_column = np.sort(column)
		perc_idx = int(len(sorted_column) * p / 100)
		if perc_idx <= 0:
			perc[idx] = sorted_column[0]
		elif perc_idx >= len(sorted_column):
			perc[idx] = sorted_column[len(sorted_column) - 1]
		else :
			perc_idx = math.ceil(perc_idx)
			if p == 50 and len(sorted_column) % 2 == 0:
				perc[idx] = (sorted_column[perc_idx] + sorted_column[perc_idx - 1]) / 2
			else:
				perc[idx] = sorted_column[perc_idx]
	return perc

if __name__ == '__main__':

	parser = argparse.ArgumentParser("Sorting Hat - Describe program")
	parser.add_argument("dataset", type=str, help="File path of dataset to describe (with valid reading permission)")
	args = parser.parse_args()
	filename = args.dataset.split("/")[-1]
	if not isinstance(args.dataset, str) or not os.path.isfile(args.dataset):
		parser.print_help()
		exit(1)

	datas_df = getDataFrame(args.dataset)
	numerics_df = getNumerics(datas_df)
	columns = numerics_df.columns.values


	count = countFeatures(numerics_df)
	description = pd.DataFrame(count.reshape(1, -1), index=['Count'], \
		columns=columns)

	mean = meanFeatures(numerics_df, count)
	description = pd.concat([description, pd.DataFrame(mean.reshape(1, -1), \
		index=['Mean'], columns=columns)])

	std = stdFeatures(numerics_df, mean, count)
	description = pd.concat([description, pd.DataFrame(std.reshape(1, -1), \
		index=['Std'], columns=columns)])

	minimum = minFeatures(numerics_df)
	description = pd.concat([description, pd.DataFrame(minimum.reshape(1, -1), \
		index=['Min'], columns=columns)])

	first_quart = percentileFeatures(numerics_df, 25)
	description = pd.concat([description, pd.DataFrame(first_quart.reshape(1, -1), \
		index=['25%'], columns=columns)])

	median = percentileFeatures(numerics_df, 50)
	description = pd.concat([description, pd.DataFrame(median.reshape(1, -1), \
		index=['50%'], columns=columns)])

	second_quart = percentileFeatures(numerics_df, 75)
	description = pd.concat([description, pd.DataFrame(second_quart.reshape(1, -1), \
		index=['75%'], columns=columns)])

	maximum = maxFeatures(numerics_df)
	description = pd.concat([description, pd.DataFrame(maximum.reshape(1, -1), \
		index=['Max'], columns=columns)])

	pd.set_option('display.max_columns', len(description.columns.values))
	pd.set_option('display.float_format', '{:.6f}'.format)
	print(description)

