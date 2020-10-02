'''
Setup: > echo "DL_DIR=<path to directory you want sorted>" > .env
On change in directory specified in DL_DIR, will sort specified file types into
designated subdirectories.
'''

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dotenv import load_dotenv
import os, time, logging, re

load_dotenv()

class DirEventHandler(FileSystemEventHandler):
	def on_modified(self, event):
		if not os.path.exists(path+'/PDFs'): os.mkdir(path+'/PDFs')
		if not os.path.exists(path+'/images'): os.mkdir(path+'/images')
		if not os.path.exists(path+'/sound'): os.mkdir(path+'/sound')
		for file_name in os.listdir(path):
			if re.search(r'.jpg|.png|.jpeg',file_name):
				os.rename(path+'/'+file_name, path+'/images/'+file_name)
			elif re.search(r'.pdf', file_name):
				os.rename(path+'/'+file_name, path+'/PDFs/'+file_name)
			elif re.search(r'.aac|.mp4|.mp3|.m4a|.wav', file_name):
				os.rename(path+'/'+file_name, path+'/sound/'+file_name)

if __name__ == "__main__":
	observer = Observer()
	path = os.getenv("DL_DIR")
	event_handler = DirEventHandler()
	observer.schedule(event_handler, path, recursive=True)
	observer.start()
	try:
		while True:
			time.sleep(10)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()
