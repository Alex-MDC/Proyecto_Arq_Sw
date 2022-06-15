from abc import ABC, abstractmethod
import csv

#DP: Strategy pattern is very similiar to this repository pattern

class AbstractRepository(ABC):

    @abstractmethod
    def begin(self):
        pass

    @abstractmethod
    def get(self):
        pass

class Movie_Repository(AbstractRepository):
	def __init__(self, file):
		self.rows = []
		self.fields = []
		self.filename = file
		#"conexion a db" (se lee el archivo csv)
		self.begin()

	def begin(self):
		with open(self.filename, 'r') as csvfile:
			csvreader = csv.reader(csvfile)
			fields = next(csvreader)
			for row in csvreader:
				self.rows.append(row)

	def get(self):
		# retorna los registros
		return self.rows

	def getWithKey(self, pref_key):
		filteredMovies = list(filter(lambda row : int(row[0]) == pref_key, self.rows))
		return filteredMovies
