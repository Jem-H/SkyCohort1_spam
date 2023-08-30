movies = [{"title": "Jaws", "director": "Steven Spielberg", "year": "1975"},
          {"title": "Star Wars", "director": "George Lucas", "year": "1977"},
          {"title": "Vanilla Sky", "director": "Cameron Crowe", "year": "2001"},
          {"title": "The Mission", "director": "Rolan Joffe", "year": "1986"},
          {"title": "Bridget Jones Diary", "director": "Sharron McGuire", "year": "2001"}]

# Part 3
movie = {"title": "Jaws", "director": "Stephen Spielberg", "year": "2000"}
print("Movie:" + movie["title"])
print("Director:" + movie["director"])
print("Year:" + movie["year"])

# Part 5
# Iterate through each movie and print out title
for item in movies:
    print(item["title"], item["director"])