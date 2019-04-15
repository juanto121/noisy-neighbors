import os

CURRENT_FOLDER = '/home/pi/Documents/noise-meter/'

def remove_files_in_directory(directory):
	DIR_TO_REMOVE = CURRENT_FOLDER + directory
	for _file in os.listdir(DIR_TO_REMOVE):
	  file_path = os.path.join(DIR_TO_REMOVE, _file) 
	  try:
	    if os.path.isfile(file_path):
	      os.unlink(file_path)
	  except Exception as e:
	    print(e)

