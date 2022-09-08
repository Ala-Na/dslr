import pandas as pd
import numpy as np
import argparse
import os
from typing import Tuple

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

def getNumerics(df: pd.DataFrame) -> np.ndarray:
	no_index = df.drop('Index', axis=1)
	numerics_datas = no_index.select_dtypes(include=np.number)
	return numerics_datas

if __name__ == '__main__':
	parser = argparse.ArgumentParser("Sorting Hat - Describe program")
	parser.add_argument("dataset", type=str, help="File path of dataset to describe (with valid reading permission)")
	args = parser.parse_args()
	if not isinstance(args.dataset, str) or not os.path.isfile(args.dataset) :#or not os.access(args.dataset, os.R_OK):
		parser.print_help()
		exit(1)
	datas_df = getDataFrame(args.dataset)
	numerics_df = getNumerics(datas_df)
