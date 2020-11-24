import tensorflow as tf
import numpy as np
#import pandas as pd
import csv
from functools import reduce
import math


def get_data(data_file):
    """
    read the stock data and split into train and test

    :param data_file: Path to the data file.
    :return: Tuple of train and test opening prices
    """
    # Done TODO: load training data from training file.
    test_ratio = 0.2

    with open(data_file, 'r') as csvfile:
        data = csv.reader(csvfile, delimiter = ',')
        raw = [d for d in data]

    darr = np.asarray(raw)

    darr =  darr[1:, :2]
    #date and open are cols respectively

    num_data_points = darr.shape[0]
    split_index = math.floor(num_data_points*test_ratio)

    test_data = darr[:split_index]
    train_data = darr[split_index:]

    return (train_data, test_data)

def main():
    get_data('./AAPL.csv')

if __name__ == '__main__':
    main()
