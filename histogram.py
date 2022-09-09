import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Maybe do scaled and non scaled data ?
# https://stats.stackexchange.com/questions/562203/normalizing-and-scaling-are-different
# https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0


def getDataFrame() -> pd.DataFrame:
	try:
		filepath = './datasets/dataset_train.csv'
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
	return numerics_datas

def getHousesList(df: pd.DataFrame) -> list:
	return df['Hogwarts House'].unique()

def drawFeatureHistogram(df: pd.DataFrame, feature: str, houses: list, \
		colors: list, ax: plt.axes) -> None:
	for house, color in zip(houses, colors):
		house_df = df.loc[df['Hogwarts House'] == house]
		house_array = house_df[feature].values
		ax.hist(house_array, bins=20, color=color, alpha=0.25)
		ax.set_title(feature)


if __name__ == "__main__":
	print("Which lesson at Hogwarts has a homogeneous mark's repartition between all four houses ?\n")

	datas_df = getDataFrame()
	numerics_df = getNumerics(datas_df)
	houses = getHousesList(datas_df)
	colors = ['blue', 'green', 'red', 'yellow']

	fig, axs = plt.subplots(3, 5)
	fig.suptitle('Mark\'s repartition by subject')

	for idx, column in enumerate(numerics_df.columns):
		drawFeatureHistogram(datas_df, column, houses, colors, axs[int((idx / 5) % 3), idx % 5])
	axs[-1, -1].axis('off')
	axs[-1, -2].axis('off')

	plt.show()
