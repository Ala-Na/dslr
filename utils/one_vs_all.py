from utils.dataframe_manip import *
from utils.logistic_regression import *
from utils.logistic_scores import *
from utils.array_manip import *
import pandas as pd
import numpy as np

class OneVsAll():

	"""
		Class to perform One vs All multiclass logistic regression.
		Here, y (targets) must be a value between 0 and number of classes - 1.
	"""

	def __init__(self, default_theta: list or np.ndarray, \
			max_y_val: int = 1, alpha: float = 0.001, \
            max_iter: int = 1000, penalty: str ='l2', lambda_: float = 1.0) \
			-> None:
		assert isinstance(max_y_val, int) and max_y_val > 0
		assert isinstance(default_theta, list or np.ndarray)
		self.max_y_val = max_y_val
		self.submodels = []		
		for _ in range(0, max_y_val):
			self.submodels.append(LogisticRegression(theta=default_theta, \
				alpha=alpha, max_iter=max_iter, penalty=penalty, \
				lambda_=lambda_))

	def perform(self, x_train: np.ndarray, y_train: np.ndarray, \
			x_val: np.ndarray or None = None, y_val: np.ndarray or None = None, \
			batch_size: int or None = None) -> list or None:
		if y_val is not None and x_val is not None:
			mse = []
		for value in range(0, self.max_y_val):
			y_train_tmp = np.select([y_train == value, \
				y_train != value], [1, 0], y_train)
			y_val_tmp = np.select([y_val == value, \
				y_val != value], [1, 0], y_val)
			if y_val is not None and x_val is not None:
				mse.append(self.submodels[value].gradient_descent(x_train, y_train_tmp, \
					x_val=x_val, y_val=y_val_tmp, batch_size=batch_size))
			else:
				self.submodels[value].gradient_descent(x_train, y_train_tmp, \
					batch_size=batch_size)
			print(y_train_tmp[:5])
			y_hat = np.round(self.submodels[value].predict(x_train))
			# Accuracy on training set
			print(sklearn.metrics.accuracy_score(y_train_tmp, y_hat))
		if y_val is not None and x_val is not None:
			return mse

	def predict(self, x: np.ndarray) -> np.ndarray:
		y_hat = []
		for idx in range(0, self.max_y_val):
			y_hat.append(self.submodels[idx].predict(x))
		return	np.argmax(y_hat, axis=0).reshape(-1, 1)

	def get_thetas(self) -> list:
		thetas = []
		for idx in range(0, self.max_y_val):
			thetas.append(self.submodels[idx].theta)
		return thetas	
