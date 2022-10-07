from utils.dataframe_manip import *
from utils.logistic_regression import *
from utils.logistic_scores import *
from utils.array_manip import *
import numpy as np
import os
import sklearn.metrics

class OneVsAll():

	'''
		Class to perform One vs All multiclass logistic regression.
		Here, y (targets) must be a value between 0 and number of classes - 1.
	'''

	def __init__(self, nb_features: int, max_y_val: int = 1, \
			initialization: str = 'random', alpha: float = 0.001, \
			beta_1: float = 0.9, beta_2: float = 0.99, \
			epsilon: float = 1e-8, lambda_: float = 1.0, \
			max_iter: int = 1000, regularization: str = 'l2', \
			optimization: str = None, early_stopping: bool = False, \
			decay: bool = False, decay_rate: float = 1.0, \
			decay_interval: int or None = 1000) -> None:
		assert isinstance(max_y_val, int) and max_y_val > 0
		self.max_y_val = max_y_val
		self.submodels = []
		for _ in range(0, max_y_val):
			self.submodels.append(LogisticRegression(nb_features, \
				initialization=initialization, alpha=alpha, beta_1=beta_1, \
				beta_2=beta_2, epsilon=epsilon, lambda_=lambda_, \
				max_iter=max_iter, regularization=regularization, \
				optimization=optimization, early_stopping=early_stopping, \
				decay=decay, decay_rate=decay_rate, \
				decay_interval=decay_interval))

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
			y_hat = np.round(self.submodels[value].predict(x_train))
		if y_val is not None and x_val is not None:
			return mse

	def predict(self, x: np.ndarray) -> np.ndarray:
		y_hat = []
		for idx in range(0, self.max_y_val):
			y_hat.append(self.submodels[idx].predict(x))
		return	np.argmax(y_hat, axis=0).reshape(-1, 1)

	def set_thetas(self, thetas_lst: list) -> None:
		for idx in range(0, self.max_y_val):
			self.submodels[idx].set_values(thetas_lst[idx])

	def get_thetas(self) -> list:
		thetas = []
		for idx in range(0, self.max_y_val):
			thetas.append(self.submodels[idx].theta)
		return thetas

	def save_values_npz(self, filepath='thetas.npz') -> None:
		if (os.path.isfile(filepath)):
			os.remove(filepath)
		thetas = self.get_thetas()
		try:
			np.savez(filepath, thetas=thetas)
		except:
			print("\033[91mOops, can't save values in {} file.\033[0m".format(filepath))

	def get_values_npz(self, filepath='thetas.npz') -> None:
		try:
			values = np.load(filepath)
			thetas = values['thetas']
			for idx in range(0, self.max_y_val):
				self.submodels[idx].set_values(thetas[idx])
		except:
			print("\033[91mOops, can't get values from {} file.\033[0m".format(filepath))

