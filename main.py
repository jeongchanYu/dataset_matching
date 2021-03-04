import customfunction as cf
import os
import csv

with open('path.csv', 'r') as f:
    csv_list = csv.reader(f)
    csv_list = list(csv_list)
del csv_list[0]

for source_path, target_path in csv_list:
    if cf.compare_path_list(source_path, target_path):
        print("(Source:{}) and (Target:{}) is already same.".format(source_path, target_path))
        continue

    source_list =
    target_list = cf.read_path_list(target_path, 'wav')
