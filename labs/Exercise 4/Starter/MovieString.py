#! /usr/bin/python

movie = "Local Hero, 111 minutes, Bill Forsyth, Burt Lancaster"

print("-" * len(movie))

print(movie.replace(",", ":"))

print("Film: " + movie[0:10])

print("Duration: " + movie[12:23])

print("Director: " + movie[25:37])

print("Starring: " + movie[39:])

print("-" * len(movie))

fields = movie.split(",")
hours = int(fields[1].split()[0]) //60
mins = int(fields[1].split()[0]) % 60

print("-" * len(movie))
print(movie.replace(",", ":"))
print("Film: " + fields[0])
print("Duration: " + str(hours) + " hour, " + str(mins) + " mins")
print("Director: " + fields[2])
print("Starring:" + fields[3])
print("-" * len(movie))

movie = "Local Hero, 111 minutes, Bill Forsyth, Burt Lancaster"
print("-" * len(movie))
print(movie.replace(",", ":"))
print(f"Film:" + fields[0])


