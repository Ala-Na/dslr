import pandas as pd
import numpy as np
import math

class DfStats():
	def __init__(self, df: pd.DataFrame) -> None:
		if not df.shape[1] == df.select_dtypes(include=np.number).shape[1]:
			raise ValueError("DfStats need to receive a dataframe with only numerics values inside columns.")
		self.df = df
		self.count = self.count_features()
		self.mean = self.mean_features()
		self.std = self.std_features()
		self.min = self.min_features()
		self.max = self.max_features()
		self.range = self.range_features()
		self.first_quartil = self.percentile_features(25)
		self.median = self.percentile_features(50)
		self.third_quartil = self.percentile_features(75)
		self.itq_range = self.interquartile_range_features()
		self.mode = self.mode_features()
		self.outliers = self.detect_outliers()

	def count_features(self) -> np.ndarray:
		self.count = np.zeros(len(self.df.columns))
		for idx, column in enumerate(self.df.columns):
			self.count[idx] = len(self.df[column]) - self.df[column].isna().sum()
		return self.count

	def mean_features(self) -> np.ndarray:
		self.mean =  np.zeros(len(self.df.columns))
		for idx, column in enumerate(self.df.columns):
			if self.count[idx] != 0:
				self.mean[idx] = self.df[column].sum() / self.count[idx]
		return self.mean

	# Please note that pandas std function behave differently of numpy std
	# Here, we reproduce the same output as numpy
	def std_features(self) -> np.ndarray:
		self.std =  np.zeros(len(self.df.columns))
		for idx, column in enumerate(self.df.columns):
			for value in self.df[column]:
				if not math.isnan(value):
					self.std[idx] += (value - self.mean[idx]) ** 2
			self.std[idx] = math.sqrt(self.std[idx] / self.count[idx])
		return self.std

	def min_features(self) -> np.ndarray:
		self.minimum = np.zeros(len(self.df.columns))
		for idx, column in enumerate(self.df.columns):
			for row, value in enumerate(self.df[column]):
				if row == 0 or math.isnan(self.minimum[idx]) or ((not math.isnan(value)) \
						and value < self.minimum[idx]):
					self.minimum[idx] = value
		return self.minimum

	def max_features(self) -> np.ndarray:
		self.maximum = np.zeros(len(self.df.columns))
		for idx, column in enumerate(self.df.columns):
			for row, value in enumerate(self.df[column]):
				if row == 0 or math.isnan(self.maximum[idx]) or ((not math.isnan(value)) \
						and value > self.maximum[idx]):
					self.maximum[idx] = value
		return self.maximum

	# Beware ! There's more than one way to calculate percentile and if it's
	# compared with another function, it may differs.
	# Function for p = 50 is calculus of median
	def percentile_features(self, p: int) -> np.ndarray:
		assert isinstance(p, int) and not (p > 100 or p < 0)
		perc = np.zeros(len(self.df.columns))
		for idx, column in enumerate(self.df.columns):
			column = self.df[column].dropna()
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

	def mode_features(self) -> np.ndarray:
		self.mode = np.zeros(len(self.df.columns))
		for idx, column in enumerate(self.df.columns):
			column = self.df[column].dropna()
			max_repet = 0
			for i, item in enumerate(column.values):
				repet = 0
				for comp in column.values[i:]:
					if item == comp:
						repet += 1
				if repet > max_repet:
					max_repet = repet
					self.mode[idx] = item
		return self.mode

	def range_features(self) -> np.ndarray:
		assert len(self.minimum) == len(self.maximum)
		self.range = np.zeros(len(self.minimum))
		for idx in range(len(self.minimum)):
			self.range[idx] = self.maximum[idx] - self.minimum[idx]
		return self.range

	def interquartile_range_features(self) -> np.ndarray:
		assert len(self.first_quartil) == len(self.third_quartil)
		self.itq_range = np.zeros(len(self.first_quartil))
		for idx in range(len(self.first_quartil)):
			self.itq_range[idx] = self.third_quartil[idx] - self.first_quartil[idx]
		return self.itq_range

	def mean_normalization(self) -> pd.DataFrame:
		normalized_df = self.df.copy()
		for idx, column in enumerate(normalized_df.columns):
			normalized_df[column] = (self.df[column] \
				- self.df[column].mean()) / self.std[idx]
		return normalized_df

	def detect_outliers(self) -> int:
		normalized_df = self.mean_normalization()
		self.outliers = np.zeros(len(self.df.columns))
		for idx, column in enumerate(self.df.columns):
			abs_z_score = normalized_df[column].abs()
			outliers_arr =  abs_z_score > 3
			outliers_arr = np.asarray(abs_z_score[outliers_arr])
			self.outliers[idx] = len(outliers_arr)
		return self.outliers
