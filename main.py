import pandas as pd
import logging
import json

class CarDatasetProcessor:
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = None
        self.logger = self.setup_logging()

    def setup_logging(self):
        logger = logging.getLogger('car_dataset_logger')
        logger.setLevel(logging.INFO)

        # Create a file handler
        file_handler = logging.FileHandler('car_dataset.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        return logger

    def load_data(self):
        try:
            with open(self.json_file, 'r') as f:
                self.data = json.load(f)
                self.logger.info('Dataset loaded successfully')
        except Exception as e:
            self.logger.error(f'Error loading dataset: {e}')

    def process_data(self):
        if self.data is None:
            self.logger.error('Dataset not loaded')
            return

        df = pd.DataFrame(self.data)
        unique_cars = df['Name'].nunique()
        avg_hp = df['Horsepower'].mean()
        top_heavy_cars = df.nlargest(5, 'Weight_in_lbs')
        cars_by_manufacturer = df['Origin'].value_counts()
        cars_by_year = df['Year'].value_counts()

        self.logger.info(f'Number of unique cars: {unique_cars}')
        self.logger.info(f'Average horse power of all cars: {avg_hp}')
        self.logger.info('Top 5 heaviest cars:')
        self.logger.info(top_heavy_cars.to_string(index=False))
        self.logger.info('Number of cars made by each manufacturer:')
        self.logger.info(cars_by_manufacturer.to_string())
        self.logger.info('Number of cars made each year:')
        self.logger.info(cars_by_year.to_string())

        df.to_csv('car_dataset.csv', index=False)
        self.logger.info('Dataset saved to car_dataset.csv')

if __name__ == "__main__":
    processor = CarDatasetProcessor('cars.json')
    processor.load_data()
    processor.process_data()
