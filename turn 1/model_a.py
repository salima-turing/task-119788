import unittest
import random

def aggregate_data(data, aggregation_func=sum):
	return aggregation_func(data)

class TestAggregationLogic(unittest.TestCase):

	def test_sum_aggregation(self):
		# Test with a diverse range of data
		data = [1, 2, 3, 4, 10]
		self.assertEqual(aggregate_data(data), sum(data))

		# Test for edge case: empty data
		self.assertEqual(aggregate_data([]), 0)

		# Test for single element data
		self.assertEqual(aggregate_data([42]), 42)

	def test_max_aggregation(self):
		# Test with different aggregation function
		data = [1, 54, -3, 78, 7, 54, -12]
		self.assertEqual(aggregate_data(data, max), max(data))

	def test_performance_with_large_data(self):
		# Test performance with large data set
		data = list(range(100000))
		self.assertEqual(aggregate_data(data), sum(data))

	def test_maintainability_with_custom_func(self):
		# Test with a custom aggregation function
		def custom_sum(data):
			return sum(x for x in data if x > 0)

		data = [-5, 1, 2, 3, -4, 8]
		self.assertEqual(aggregate_data(data, custom_sum), custom_sum(data))

if __name__ == '__main__':
	unittest.main()
