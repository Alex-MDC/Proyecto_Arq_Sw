
#OC principle
#programming to interfaces -- we are making the recommendation making its own class
#Single responsibility: this is the only class in charge of creating the recommendations!

from service import movie_repository

filename = "/src/movies/domain/movie_results.csv"

#DP: Simple factory, the switch is the kind of rating.

class Recommendation_Maker:
    def __init__(self):
        self.movie_repo = movie_repository.Movie_Repository(filename)

    # recommend a list of movies with the rating "flag", business logic inside each kind of recommendation
    # returning a top 10 of movies
    # magic key is matched to preference keys to get the filtered movies
    def recommend_with_true_rating(self,pref_key):
      
        filteredMovies = self.movie_repo.getWithKey(pref_key)
        filteredMovies = list(map(lambda row : row[1], filteredMovies))
        print("filtered movies:", filteredMovies)
        filteredMovies = filteredMovies[0:10]
        return filteredMovies

    def recommend_with_false_rating(self,pref_key):
       
        filteredMovies = self.movie_repo.getWithKey(pref_key)
        filteredMovies = list(map(lambda row : row[1], filteredMovies))
        print("filtered movies before reverse:", filteredMovies)
        filteredMovies_r = filteredMovies.copy()
        filteredMovies_r.reverse()
        filteredMovies_r = filteredMovies_r[0:10]
        print("filtered movies after reverse:", filteredMovies_r)
        return filteredMovies_r
