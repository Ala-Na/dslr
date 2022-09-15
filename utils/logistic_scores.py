import numpy as np

class LogisticScores():

	@staticmethod
	def accuracy(y: np.ndarray, y_hat: np.ndarray) -> float:
		"""
		Compute the accuracy score.
		Args:
			y:a numpy.ndarray for the correct labels
			y_hat:a numpy.ndarray for the predicted labels
		Returns:
			The accuracy score as a float.
			None on any error.
		Raises:
			This function should not raise any Exception.
		"""
		if not isinstance(y, np.ndarray) or y.size == 0:
			return None
		if not isinstance(y_hat, np.ndarray) or y_hat.shape != y.shape:
			return None
		return np.sum(y == y_hat) / y.size

	@staticmethod
	def precision(y: np.ndarray, y_hat: np.ndarray, \
			pos_label: int or str = 1) -> float:
		"""
		Compute the precision score.
		Args:
			y:a numpy.ndarray for the correct labels
			y_hat:a numpy.ndarray for the predicted labels
			pos_label: str or int, the class on which to report the 
			precision_score (default=1)
		Return:
			The precision score as a float.
			None on any error.
		Raises:
			This function should not raise any Exception.
		"""
		if not isinstance(y, np.ndarray) or y.size == 0:
			return None
		if not isinstance(y_hat, np.ndarray) or y_hat.shape != y.shape:
			return None
		if not isinstance(pos_label, int) and not isinstance(pos_label, str):
			return None
		truePos = np.sum((y == pos_label) & (y_hat == pos_label))
		falsePos = np.sum((y != pos_label) & (y_hat == pos_label))
		return truePos / (truePos + falsePos)

	@staticmethod
	def recall(y: np.ndarray, y_hat: np.ndarray, \
			pos_label: str or int = 1) -> float:
		"""
		Compute the recall score.
		Args:
			y:a numpy.ndarray for the correct labels
			y_hat:a numpy.ndarray for the predicted labels
			pos_label: str or int, the class on which to report the
			precision_score (default=1)
		Return:
			The recall score as a float.
			None on any error.
		Raises:
			This function should not raise any Exception.
		"""
		if not isinstance(y, np.ndarray) or y.size == 0:
			return None
		if not isinstance(y_hat, np.ndarray) or y_hat.shape != y.shape:
			return None
		if not isinstance(pos_label, int) and not isinstance(pos_label, str):
			return None
		truePos = np.sum((y == pos_label) & (y_hat == pos_label))
		falseNeg = np.sum((y == pos_label) & (y_hat != pos_label))
		return truePos / (truePos + falseNeg)

	@staticmethod
	def f1_score(y: np.ndarray, y_hat: np.ndarray, \
			pos_label: str or int = 1) -> float:
		"""
		Compute the f1 score.
		Args:
			y:a numpy.ndarray for the correct labels
			y_hat:a numpy.ndarray for the predicted labels
			pos_label: str or int, the class on which to report the
			precision_score (default=1)
		Returns:
			The f1 score as a float.
			None on any error.
		Raises:
			This function should not raise any Exception.
		"""
		if not isinstance(y, np.ndarray) or y.size == 0:
			return None
		if not isinstance(y_hat, np.ndarray) or y_hat.shape != y.shape:
			return None
		if not isinstance(pos_label, int) and not isinstance(pos_label, str):
			return None
		precision = precision(y, y_hat, pos_label)
		recall = recall(y, y_hat, pos_label)
		return 2 * precision * recall / (precision + recall)
