# Car Dataset Analysis

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT) /// Not really -> scroll to License

A Python program for analyzing a car dataset using pandas and object-oriented programming.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository contains a Python program that reads a car dataset from a JSON file, performs various analyses on the dataset, and then saves the processed data to a CSV file. The program is built using object-oriented programming principles and utilizes the pandas library for data manipulation.

## Features

- Load the car dataset from a JSON file.
- Calculate the number of unique cars in the dataset.
- Calculate the average horsepower of all the cars.
- Identify the top 5 heaviest cars.
- Display the number of cars made by each manufacturer.
- Show the number of cars made each year.
- Save the processed dataset to a CSV file.

## Installation

1. Clone the repository:
2. Install the required dependencies:
   ```sh
   pip install requirements.txt
   ```
   repository includes a requirements.txt file with the main dependencies but also a whole_requirements.txt created using pip freeze that includes all all packages in the environment including those that are not relevent to the project for testing purposes.
   pip install requirements.txt

## Usage
Feel free to change the context of the cars.json file as long as it matches the same structure

1. Run the program:
  ```sh
  python main.py
   ```

The program will load the dataset, perform the analyses, and save the results to a CSV file named car_dataset.csv.

## Logging

  The program uses logging to record events and information. Logs are saved in the car_dataset.log file.

## Contributing

  Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.

## License

  Feel free to use this code or parts of it as you see fit
   
