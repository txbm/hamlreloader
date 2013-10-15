import logging

from time import sleep

from os import makedirs
from os.path import (splitext, abspath, dirname, 
	basename, join, relpath, exists)

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from subprocess import call

logger = logging.getLogger('hamlreloader')

def parse_file_ext(p):
	return splitext(p)[-1].lower()

def watch_directory(watch_dir, target_dir, condition=None):
	if condition:
		condition.acquire()
	
	watch_path = abspath(watch_dir)
	logger.info('Watch path: %s' % watch_path)
	
	target_path = abspath(target_dir)
	logger.info('Target path: %s' % target_path)

	handler = ModifiedHandler(watch_path, target_path)
	obs = Observer()

	obs.schedule(handler, watch_path, recursive=True)
	obs.start()
	
	if condition:
		condition.notify()
		condition.release()
	try:
		while True:
			sleep(1)
	except KeyboardInterrupt:
		obs.stop()
	obs.join()

def render_haml(haml_file, dest_file):
	cmd = r'haml %s %s' % (haml_file, dest_file)
	call(cmd, shell=True)

class ModifiedHandler(FileSystemEventHandler):

	def __init__(self, watch_path, target_path):
		self.watch_path = watch_path
		self.target_path = target_path
		super(ModifiedHandler, self).__init__()

	def on_any_event(self, e):
		ext = parse_file_ext(e.src_path)
		if not ext == '.haml':
			return
		
		logger.info('Detected change in: %s' % e.src_path)

		subpath = dirname(relpath(e.src_path, self.watch_path))
		write_dir = join(self.target_path, subpath)
		
		if not exists(write_dir):
			makedirs(write_dir)
		
		write_path = join(write_dir, '%s.html' % splitext(basename(e.src_path))[0])

		logger.info('Writing to: %s' % write_path)
		render_haml(e.src_path, write_path)