#! /urs/bin/env python3
# Name:         .py
# Author:       Jemima Hsu
# Version:      v1.0
# Description:  This program
"""
    DocString:
"""
data_file = open("movies.txt", "rt")
data_file_out = open("movies_out.txt", "wt")

for line in data_file:
    print(line.title())
    data_file_out.write(line.title())

data_file.close()
data_file_out.close()