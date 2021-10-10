import os
import pandas as pd
import codecs
import numpy as np
import pickle

root = os.environ["project_root"]
path_notebooks = root + 'src/'
path_data = root + 'data/'
path_data_interim = path_data + 'interim/'
path_data_processed = path_data + 'processed/'

raw_data_files_path = path_data + 'raw/OnlineNewsPopularity/'
data_csv = raw_data_files_path + 'OnlineNewsPopularity.csv'
names_csv = raw_data_files_path + 'OnlineNewsPopularity.names'

working_data_csv = path_data_interim + 'data.csv'
data_csv_for_preprocessing = path_data_interim + 'data_csv_for_preprocessing.csv'
features_list = path_data_interim + 'features_list.csv'

def save_list_to_pkl(var, file):
    with open(path_data_interim + file, 'wb') as f:
        pickle.dump(var, f)

def load_list_from_pkl(file):
    with open(path_data_interim + file, 'rb') as f:
        mynewlist = pickle.load(f)
    return mynewlist

figures_dir = root + 'figures/'

