import os
import pandas as pd
import codecs
import numpy as np
import pickle
from numpy import save, load

# root = os.environ["project_root"]
root = "/home/yash/Desktop/Courses/Data1030/Project/news_article_popularity/"
path_notebooks = root + 'src/'
path_data = root + 'data/'
path_data_interim = path_data + 'interim/'
path_data_processed = path_data + 'processed/'
path_results = root + 'results/'

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

preprocessed_data_path_train = path_data_interim + 'pp_train.npy'
preprocessed_data_path_val = path_data_interim + 'pp_val.npy'
preprocessed_data_path_test = path_data_interim + 'pp_test.npy'

preprocessed_data_y_train = path_data_interim + 'pp_train_y.npy'
preprocessed_data_y_val = path_data_interim + 'pp_val_y.npy'
preprocessed_data_y_test = path_data_interim + 'pp_test_y.npy'

MODEL_EVALUATIONS_PICKLE = 'model_evals.pkl'

def save_preprocessed_data(data, path):
    save(path, data)

def load_preprocessed_data(path):
    data = load(path)
    return data

def save_to_results(var, file):
    with open(path_results + file, 'wb') as f:
        pickle.dump(var, f)

def load_from_results(file):
    with open(path_results + file, 'rb') as f:
        mynewlist = pickle.load(f)
    return mynewlist

