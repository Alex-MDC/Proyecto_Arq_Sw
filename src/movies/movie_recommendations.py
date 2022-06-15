from abc import ABC, abstractmethod
import csv

# class AccountingSystem(ABC):

#     @abstractmethod
#     def create_purchase_invoice(self, purchase):
#         pass

#     @abstractmethod
#     def create_sale_invoice(self, sale):
#         log.debug('Creating sale invoice', sale)

class db():
	def __init__(self, file):
		self.rows = []
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
