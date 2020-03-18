import re

import requests

part_files = []  # fill with list of files from download_threading()


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
	return split_size


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


def download_threading(start, end, url, i, path_to_temp) -> None:
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

		-name : path_to_temp
			-description : temp dir path ( to save each part )

	"""
	res = requests.get(url,
					   headers={"Range": f"bytes={start}-{end}"})  # grab file with start and end bound range
	with open(path_to_temp + f"/part{i}.jpg", 'wb') as f:
		f.write(res.content)  # create each part
		part_files.append(f.name)  # add path of part to list
	print(f"part {i + 1} finished ....")


def write_on_final_file():
	pass
