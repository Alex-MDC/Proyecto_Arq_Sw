
#OC principle
#programming to interfaces -- we are making the recommendation making its own class
#Single responsibility: this is the only class in charge of creating the recommendations!

import csv

filename = "/src/movies/movie_results.csv"

# initializing the titles and rows list
fields = []
rows = []
resultados =[]

# recommend_with_true_rating
def recommend_with_true_rating(pref_key):
    # with open(filename, 'r') as csvfile:
    #     csvreader = csv.reader(csvfile)
    #     fields = next(csvreader)
    #     for row in csvreader:
    #         rows.append(row)

    filteredMovies = list(filter(lambda row : int(row[0]) == pref_key, rows))
    filteredMovies = list(map(lambda row : row[1], filteredMovies))
    filteredMovies = filteredMovies[0:10]
    return filteredMovies

def recommend_with_false_rating(pref_key):
    # with open(filename, 'r') as csvfile:
    #     csvreader = csv.reader(csvfile)
    #     fields = next(csvreader)
    #     for row in csvreader:
    #         rows.append(row)

    filteredMovies = list(filter(lambda row : int(row[0]) == pref_key, rows))
    filteredMovies = list(map(lambda row : row[1], filteredMovies))
    filteredMovies = filteredMovies.reverse()
    filteredMovies = filteredMovies[0:10]
    return filteredMovies
