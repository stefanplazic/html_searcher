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


'''
for given link  it replaces ../ -> with full path
returns the full path to file
'''
def link_converter(link, file_name):
	parent_dir = file_name.split('/')[:-1]
	link_sub_dirs = link.split('../')[:-1]
	
	for links in link_sub_dirs:
		#evry time for ../ -> remove one level of dir 
		parent_dir.pop()

	full_link = '/'.join( parent_dir) + "/" + link.split('../')[-1]
	print full_link

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
	

if __name__=='__main__':
	
	#get file path from command line
	file_path = sys.argv[1]

	html_files = get_all_Files(file_path)

	my_pages = create_dictionary(html_files)
	
	option = 'n'
	while option != 'y':
	
		#take user input 
		user_input = raw_input('Enter the words   ')
		user_input = user_input.strip()
		user_input = user_input.split(' ')

		#search this document

		option = raw_input("Do you want to exit? (y|n):  ")
	

	
	
	
	

	
	
	