import os
import pandas as pd
import codecs
import numpy as np

root = os.environ["project_root"]
print(root)
path_notebooks = root + 'src/'
path_data = root + 'data/'
path_data_interim = path_data + 'interim/'
path_data_processed = path_data + 'processed/'

raw_data_files_path = path_data + 'raw/OnlineNewsPopularity/'
data_csv = raw_data_files_path + 'OnlineNewsPopularity.csv'
names_csv = raw_data_files_path + 'OnlineNewsPopularity.names'

working_data_csv = path_data_interim + 'data.csv'
features_list = path_data_interim + 'features_list.csv'
