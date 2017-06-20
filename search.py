from parser import Parser
import sys
import os

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
	my_pages = {}
	
	#create parser
	parser = Parser()

	for file in html_files:
		[links, words] = parser.parse(file)
		my_pages[file] = words_frequency(words)

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
	

if __name__=='__main__':
	
	#get file path from command line
	file_path = sys.argv[1]

	html_files = get_all_Files(file_path)

	my_pages = create_dictionary(html_files)
	print my_pages
	
	
	

	
	
	