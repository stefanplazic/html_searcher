from parser import Parser
import sys
import os
import operator

'''
returns all html files in given directory
'''
def get_all_Files( dir_Path='python-2.7.7-docs-html'):
	
	my_files = []
	
	for file in os.listdir(dir_Path):
		if os.path.isdir(os.path.join(dir_Path,file)):
			
			#if file is directorijum -> do recursive call
			my_files.extend(get_all_Files(os.path.join(dir_Path, file)))
		
		elif file.endswith('.html') or file.endswith('.htm'):
			my_files.append(os.path.join(dir_Path,file))

	return my_files


def create_dictionary(html_files = []):
	
	#dic to holed data for all pages
	my_pages = create_page_dir(html_files)
	
	
	#create parser
	parser = Parser()

	for file in html_files:
		[links, words] = parser.parse(file)
		my_pages[file]['words'] = words_frequency(words)
		
		for link in links:
			
			if link in my_pages:
				# save to file where link points
				my_pages[link]['links'].append(file)
			

	return my_pages


def create_page_dir(html_files):
	my_pages = {}
	for file in html_files:
		my_pages[file] = {'words':[], 'links':[]}

	return my_pages


def words_frequency(list_of_words):
	
	bags_of_words = {}

	for word in list_of_words:
		
		if word in bags_of_words:
			#if word is already in the list - increment
			bags_of_words[word] += 1

		else:
			bags_of_words[word] = 1

	return bags_of_words
	

def search(my_pages, list_of_words):
	
	search_result = {}
	
	for page in my_pages:
		
		score = 0
		#check if page contatins that word at all
		for word in list_of_words:
			if word in my_pages[page]['words']:
				score += my_pages[page]['words'][word] 

			#add result only if score is different from zero
			if score !=0:
				search_result[page] = score

	
	#return sorted(search_result.values(),reverse=True)
	return sorted(search_result.items(), key=operator.itemgetter(1),reverse=True)

	

if __name__=='__main__':
	
	#get file path from command line
	file_path = sys.argv[1]

	html_files = get_all_Files(file_path)

	my_pages = create_dictionary(html_files)
	#print my_pages
	option = 'n'
	while option != 'y':
	
		#take user input 
		user_input = raw_input('Enter the words   ')
		user_input = user_input.strip()
		user_input = user_input.split(' ')

		search_result = search(my_pages, user_input)
		print 'Your results: '
		print search_result

		option = raw_input("Do you want to exit? (y|n):  ")
	

	
	
	
	

	
	
	