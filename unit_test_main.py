import unittest
from main import CarDatasetProcessor

class TestCarDatasetProcessor(unittest.TestCase):
    # Testing if json assets load properly and return something other than None
    def test_load_json_data(self):
        processor = CarDatasetProcessor('cars.json')
        processor.load_data()
        self.assertIsNotNone(processor.data)

    # Struggling at this point to come up with unit tests that don't include hardcoded values
    def test_unique_car_count(self):
        processor = CarDatasetProcessor('cars.json')  # Use a test JSON file
        processor.load_data()
        processor.process_data()
        self.assertEqual(processor.unique_cars, 311)


if __name__ == '__main__':
    unittest.main()