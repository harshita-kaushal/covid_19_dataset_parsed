# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory
from glob import glob
import json
import os

# all names in the inputs

# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))
def parse_data():
    data_stored = {}
#     print("files in biorxiv_medrxiv:")
    for dirname, _, filenames in os.walk('/kaggle/input/CORD-19-research-challenge/biorxiv_medrxiv/biorxiv_medrxiv'):
            for filename in filenames:
                if filename == '01e3b313e78a352593be2ff64927192af66619b5.json':
                    string_path = '/kaggle/input/CORD-19-research-challenge/biorxiv_medrxiv/biorxiv_medrxiv/' + filename
                    with open(string_path) as s:
                        json_data = json.load(s)
                        data_stored[json_data['paper_id']] = json_data
    
    return data_stored

parsed_data = parse_data()
    
def parse_authors_abstract(data_stored):
    refined_data = {}
    #print(len(data_stored)) 885 papers in json 
    # data will be they keys
    for data in data_stored:
        paper = data_stored[data]
        abstract_outer = paper['abstract']
        text_abstract = ""
        for i in abstract_outer:
            text_abstract += i['text']
#         print(text_abstract)
        
    #     print(paper)
        metadata = paper['metadata']
        key_title = metadata['title']
        refined_data[key_title] = {}
        
        #authors and their associated instituitons 
        authors_unrefined = metadata['authors'] # includes middle names etc
        authors_dict = {}
        for author in authors_unrefined: 
            name = author['first'] + " " + author['last']
            wrapped_org = author['affiliation']
            inst = wrapped_org['institution']
            lab =  wrapped_org['laboratory']
            if not lab:
                authors_dict[name] = inst
            else:
                authors_dict[name] = lab
#         print(authors_dict)
    
    refined_data[key_title]['Authors'] = authors_dict
    refined_data[key_title]['Abstract'] = text_abstract

    
    
    return refined_data
    
    
cleaned_data = parse_authors_abstract(parsed_data)
print(cleaned_data)

# def write_output():
#     save_path = '/kaggle/output/kaggle/working'
#     for i in cleaned_data:
#         name_of_file = i[key_title]
#         completeName = os.path.join(save_path, name_of_file+".txt")   
#         file1 = open(completeName, "w")
#         file1.write(cleaned_data)

#         file1.close()
        

    
# def parse_abstract():
#     for data in parsed_data:
#         val = parsed_data[data]
#         abstract_outer = val['abstract']
#         text_abstract = ""
#         for i in abstract_outer:
#             text_abstract += i['text']
#         print(text_abstract)

# parse_abstract()


# print(refined_data)
    
    
            
# print(data_stored)