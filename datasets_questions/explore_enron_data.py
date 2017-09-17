#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

file_path="../final_project/final_project_dataset_unix.pkl"
file_handler = open(file_path, "rb") 
enron_data = pickle.load(file_handler, fix_imports=True)
file_handler.close()


#enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"),fix_imports = True)
#Print the length of th dictionary i.e the number of keys in the dictionary

print ("The number of keys:", len(enron_data))



