from binarytree import tree, Node

class Query:

	def check(self,query):
		
		return_set = []
		for index, token in enumerate(query):
			if token == 'and' or token == 'or':
				if index == 0 or index == len(query) - 1:
					
					#raise an error
					raise ValueError('input must not start|end with queries AND|OR')

		
		
		

	