import pandas as pd
import numpy as np

def get_dataframe(filepath: str) -> pd.DataFrame:
	try:
		datas = pd.read_csv(filepath)
		return datas
	except:
		print("\033[91mOops, can't extract datas from {} data file.\033[0m".\
			format(filepath))
		print("\033[02;03mHint: Check file rights, file type, ...\033[0m")
		print("Exiting...")
		exit()

def get_numerics(df: pd.DataFrame) -> pd.DataFrame:
	return df.select_dtypes(include=np.number)

def get_mean_normalized(df: pd.DataFrame, numerics_df: pd.DataFrame) -> pd.DataFrame:
	for column in numerics_df.columns:
		df[column] = (df[column] - df[column].mean()) / df[column].std()
	return df

def get_houses_list(df: pd.DataFrame) -> list:
	return np.sort(df['Hogwarts House'].unique())
