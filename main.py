import os
import shutil
import sys
from threading import Thread

from exception import UrlDoesNotExists
from operation import parts_size, grab_file_name, download_threading, part_files


class Shivan(object):
	def __init__(self, url):
		self.url = url
		self._prepare()  # preprocess before download
		self._download()

	def _split(self):
		"""
		split full size of file to n part .
		for examples full size of file is 174010 and we need to split file to 8 parts :
			we split parts like :
				[0, 29001, 58002, 87003, 116004, 145005, 174010]
		then we request for each part to download file in 8 parts like his:
			first part => 0 - 29001 byte
			second part => 29002 - 58002 byte
			....
			least part => 145006 - 174010 byte
		"""
		return parts_size(self.url)

	def _prepare(self):
		self._file_name = grab_file_name(self.url)  # grab file name from url

	def _download(self):
		path_to_temp = str(os.getcwd()) + "/.temp"  # temp dir path

		if not os.path.exists(path_to_temp):
			os.mkdir(path_to_temp)  # create temp dir

		splited_parts = self._split()  # grab <list> of parts size
		for i in range(0, len(splited_parts) - 1):
			start = splited_parts[i] + 1 if i > 0 else splited_parts[i]  # start of range(byte)
			end = splited_parts[i + 1]  # end of range (byte)

			# download each part in seprate thread
			download_in_thread = Thread(target=download_threading(start, end, self.url, i, path_to_temp))
			download_in_thread.start()

		final = open(str(os.getcwd()) + f"/{self._file_name}", "wb")  # create final file

		# part_files is list of each part path that fill in operation module
		for i in part_files:
			temp_file = open(i, 'rb')  # open as read byte mode (rb)
			temp_file = temp_file.read()
			final.write(temp_file)  # write each part in order on final file
			os.remove(i)  # delete part
		final.close()
		shutil.rmtree(path_to_temp)  # delete temp folder


if __name__ == "__main__":
	try:
		if len(sys.argv) > 1:
			url = sys.argv[1]
		else:
			raise UrlDoesNotExists
	except UrlDoesNotExists:
		print("please enter url ......")
		sys.exit(1)
	action = Shivan(url)

# TODO : fix final file name <solved>
# TODO : multi-thread download <solved>
# TODO : dynamic file extension


# TODO : add config file for defualt setting
# TODO : add config file
# TODO : dynamic path for download file
