#! /urs/bin/env python3
# Name:         .py
# Author:       Jemima Hsu
# Version:      v1.0
# Description:  This program
"""
    DocString:
"""
# Part 2
topFive = ["Star Wars", "Jaws", "Postman Pat 2", "Vanilla Sky", "Absolutely Fabulous"]
print(topFive)
print(topFive[1])
topFive.append("LOTR")
print(topFive)
print(len(topFive))
topFive[-1] = "Bob the Builder"
print(topFive)
sort = sorted(topFive, key=str)
print(sort)