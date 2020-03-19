import re
import sys
import time
import requests
import os
import json
from progress.bar import Bar

  # fill with list of files from download_threading()


def parts_size(url) -> list:
	"""
	split file into 8 part from header
	param:
		- name : url
			- description : provided url
	responses:
		- name : split_size
			- description : list of possible part size ( in byte )
	"""
	resquest = requests.head(url)  # grab header
	full_size = int(resquest.headers['content-Length'])  # full size
	split_size = [x for x in range(0, full_size, full_size // 8)]  # create
	split_size[8] = full_size  # fix least size to remainder byte from split
	return (split_size,full_size)


def grab_file_name(url) -> str:
	"""
	grab file name from link
	param:
		- name : url
			- description : downlaod link
	responses:
		- name : file_name
			- description : file name + file extension
	"""
	file_name = list(url.split('/')) 
	return file_name[-1]


def download_threading(start, end, url, i,file_name,part_files, path_to_temp) -> None:
	"""
	multi-thread downloading

	param:
		-name : start
			-description : from (byte)

		-name : end
			-description : to (byte)

		-name : url
			-description : file link

		-name : i
			-description : iter counter

		-name : file_name
			-description : original file name without file extension

		-name : part_files
			-description : array of file path

		-name : path_to_temp
			-description : temp dir path ( to save each part )

	"""	
	res = requests.get(url,
					   headers={"Range": f"bytes={start}-{end}"},stream=True)  # grab file with start and end bound range

	bar = Bar(f'Part {i+1} :', max=(end-start)//1024 + 1)
	with open(path_to_temp + f"/part{i+1}-{file_name}", 'wb') as f:
		for chunk in res.iter_content(1024):
			bar.next()
			f.write(chunk)  # create each part)
	part_files.append(f.name)  # add path of part to list
	bar.finish()

def set_config():
	config_file_path = str(os.getcwd()) + "/config.cfg"

	if os.path.exists(config_file_path):
		config_file = json.load(open(config_file_path,'r'))
	else:
		config_file = {}
	
	print("where do you need store downloaded file as default ?")
	print("provide path like : /User/example/desktop")
	print("** note ** : if you hit enter and leave it blank , its store file in root of project.")
	path_to_download = input("")

	config_file["path_to_download"]= path_to_download

	print("how many do you need shivan splits download ?")
	print("provide number in range(1-8) : ")
	print("** note ** : if you hit enter and leave it blank , its set 8 part as a default.")
	parts = input("")

	if parts:
		if int(parts) > 8 :
			parts = 8
	config_file["part"]= parts

	json.dump(config_file,open(config_file_path,'w+'))




