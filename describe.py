import pandas as pd
import argparse
import os
from utils.dataframe_manip import get_dataframe, get_numerics
from utils.dataframe_statistics import DfStats

if __name__ == '__main__':

	parser = argparse.ArgumentParser("Sorting Hat - Describe program")
	parser.add_argument("dataset", type=str, help="File path of dataset to describe (with valid reading permission)")
	args = parser.parse_args()
	filename = args.dataset.split("/")[-1]
	if not isinstance(args.dataset, str) or not os.path.isfile(args.dataset):
		parser.print_help()
		exit(1)

	datas_df = get_dataframe(args.dataset)
	no_index = datas_df.drop('Index', axis=1)
	numerics_df = get_numerics(no_index)
	# For test set, column 'House' is empty and considered a numeric column as
	# NaN is a number. We drop columns containing only NaN as a precaution.
	numerics_df = numerics_df.dropna(how='all', axis=1)
	columns = numerics_df.columns.values

	stats = DfStats(numerics_df)

	count = stats.count
	description = pd.DataFrame(count.reshape(1, -1), index=['Count'], \
		columns=columns)

	mean = stats.mean
	description = pd.concat([description, pd.DataFrame(mean.reshape(1, -1), \
		index=['Mean'], columns=columns)])

	std = stats.std
	description = pd.concat([description, pd.DataFrame(std.reshape(1, -1), \
		index=['Std'], columns=columns)])

	minimum = stats.minimum
	description = pd.concat([description, pd.DataFrame(minimum.reshape(1, -1), \
		index=['Min'], columns=columns)])

	first_quart = stats.first_quartil
	description = pd.concat([description, pd.DataFrame(first_quart.reshape(1, -1), \
		index=['25%'], columns=columns)])

	median = stats.median
	description = pd.concat([description, pd.DataFrame(median.reshape(1, -1), \
		index=['50%'], columns=columns)])

	third_quart = stats.third_quartil
	description = pd.concat([description, pd.DataFrame(third_quart.reshape(1, -1), \
		index=['75%'], columns=columns)])

	maximum = stats.maximum
	description = pd.concat([description, pd.DataFrame(maximum.reshape(1, -1), \
		index=['Max'], columns=columns)])

	mode = stats.mode
	description = pd.concat([description, pd.DataFrame(mode.reshape(1, -1), \
		index=['Mode'], columns=columns)])

	ran = stats.range
	description = pd.concat([description, pd.DataFrame(ran.reshape(1, -1), \
		index=['Range'], columns=columns)])

	itqran = stats.itq_range
	description = pd.concat([description, pd.DataFrame(itqran.reshape(1, -1), \
		index=['ITQ'], columns=columns)])

	outliers = stats.outliers
	description = pd.concat([description, pd.DataFrame(outliers.reshape(1, -1), \
		index=['Outliers'], columns=columns)])

	pd.set_option('display.max_columns', len(description.columns.values))
	pd.set_option('display.float_format', '{:.6f}'.format)
	print(description)

	# Note: It may have some differences for std
	# (here I reimplemented numpy std and not pandas std)
	# and for 25% and 75% (and ITQ range) has there is lot of way to implement
	# it (I used the mathematical definition taught in high school)
	# UNCOMMENT NEXT LINE TO COMPARE
	# print(numerics_df.describe())
