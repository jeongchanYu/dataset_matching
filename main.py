import customfunction as cf
import os
import csv

with open('path.csv', 'r') as f:
    csv_list = csv.reader(f)
    csv_list = list(csv_list)
del csv_list[0]

for source_path, target_path in csv_list:
    print("(Source:{})/(Target:{}) : ".format(source_path, target_path), end="")

    if not os.path.exists(source_path):
        raise Exception("ERROR: Source path is not exist")
    if not os.path.exists(target_path):
        raise Exception("ERROR: Target path is not exist")

    if cf.compare_path_list(source_path, target_path):
        print("File is already same.")
        continue

    source_list = cf.read_path_list(source_path)
    target_list = cf.read_path_list(target_path)
    for i in range(len(target_list)):
        target_list[i] = target_list[i].replace(target_path, "")

    for source_select in source_list:
        temp_source_select = source_select.replace(source_path, "")
        try:
            target_list.index(temp_source_select)
            target_list.remove(temp_source_select)
        except:
            os.remove(source_select)

    if not cf.compare_path_list(source_path, target_path):
        raise Exception("ERROR: Target file is more than source file")

    print("Complete!")
