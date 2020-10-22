####################################
# author: Gonzalo Salazar
# course: 2020 Complete Python Bootcamps: From Zero to Hero in Python
# purpose: lecture notes
# description: Section 17 - PDFs and CSV files
# other: N/A
####################################

import os
import csv

os.getcwd()
os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_PythonBootcamp/files_sec17')

# The module Openpyxl is useful for Excel files. It supports Excel formulas and
# retains a lof of Excel specific functionality. Check other libraries on
# python-excel.org

# There is another for Google Sheets, the Google Sheets Python API, which allows
# Python to directly make changes to the spreadsheets hosted online.

# CSV

# open the file
# encoding is important if we have languages different from English or weird
# symbols such as @ (at)
data = open('example.csv',encoding = 'utf-8')

# csv.reader
csv_data = csv.reader(data)

# reformat the csv into a python object (list of lists)
data_lines = list(csv_data)

data_lines[0]
len(data_lines)

for line in data_lines[:5]:
    print(line)

all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])
#all_emails

full_names = []
for line in data_lines[1:]:
    full_names.append(line[1] + ' ' + line[2])
#full_names

file_to_output = open('to_save_file.csv', mode = 'w', newline = '')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])

data.close()
file_to_output.close()
