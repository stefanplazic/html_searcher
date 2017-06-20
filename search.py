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



if __name__=='__main__':
	
	#get file path from command line
	file_path = sys.argv[1]

	html_files = get_all_Files(file_path)
	
	parser = Parser()
	#[links, words] = parser.parse(file_path)

	
	
	