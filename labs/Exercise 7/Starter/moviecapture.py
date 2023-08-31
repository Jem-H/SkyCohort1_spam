#! /urs/bin/env python3
# Name:         .py
# Author:       Jemima Hsu
# Version:      v1.0
# Description:  This program
"""
    DocString:
"""
title = input("What is your favourite movie?")
director = input("Who is the director?")
year = input("What year was it released?")

fh_out = open("topFive.txt", "a")
fh_out.write(f"{title}, {director}, {year} \n")
fh_out.close()
