# -*- coding: utf-8 -*-
import uuid
import csv

""" Clase de modelos de categorias. """
class Category:
	
	def __init__(self, category, uid=None):
		self.category = category
		self.uid = uid or uuid.uuid4()


	def to_dict(self):
		return vars(self)


	@staticmethod
	def schema():
		return ['category', 'uid']


""" Clase para el manejo de servicios de categorias. """
class CategoryService:
	
	def __init__(self, table):
		self.table = table


	def create(self, category):
		with open(self.table, mode='a', newline='', encoding='utf-8') as f:
			writer = csv.DictWriter(f, fieldnames=Category.schema())
			writer.writerow(category.to_dict())
			
			f.close()


def run():
	""" Proceso de ejecución. """
	FILENAME = 'files/categories.csv'
	while True:
		category_name = str(input("\n Ingrese la categoria: "))
		c = Category(category_name)

		# print(c.to_dict())

		cServ = CategoryService(FILENAME)
		cServ.create(c)


if __name__ == '__main__':
	run()