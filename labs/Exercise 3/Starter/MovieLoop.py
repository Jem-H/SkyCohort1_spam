movies = ["Jaws", "Star Wars", "Vanilla Sky", "The Mission", "Bridget Jones Diary 2"]

for movie in enumerate(movies, 1):
    length = len(movie[1])
    # print(type(movie[0])) = int
    # print(type(movie[1])) = str
    # print(type(length)) = int
    print(str(movie[0]) + ".", movie[1] + ",", str(length))