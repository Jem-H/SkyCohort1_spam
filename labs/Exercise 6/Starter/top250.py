#! /usr/bin/python

# import imdb
#
# ia = imdb.Cinemagoer()
#
# for movie in ia.get_top250_movies():
#     print(movie)

import re

# Starting line: DO NOT comment out
fh_in = open(r"/Users/jhj26/Documents/SkyCohort1_spam/labs/top_250.txt", mode="rt")

# Part 2
# for rank, movie in enumerate(fh_in, start=1):
#     print(f"{rank:>4d}: {movie}")

# Part 3
pattern = input("Enter movie name: " )
for rank, movie in enumerate(fh_in, start=1):
    m = re.search(pattern, str(movie), re.IGNORECASE)
    if m:
        print(f"{rank:>4d}: {movie}")

# Part 4 - pre-compile pattern
# This does not work!!!
# pattern = input("Enter movie name: " )
# reobj = re.compile(pattern)
# for rank, movie in enumerate(fh_in, start=1):
#     m = reobj.search(str(movie), re.IGNORECASE)
#     if m:
#         print(f"{rank:>4d}: {movie}")


# Closing line: DO NOT comment out
fh_in.close()
