from time import sleep

from os.path import splitext, abspath, dirname, basename, join

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from subprocess import call

def parse_file_ext(p):
	return splitext(p)[-1].lower()

def watch_directory(watch_dir, target_dir):
	while 1:
		tp = abspath(dirname(target_dir))
		h = ModifiedHandler(tp)
		o = Observer()
		p = abspath(dirname(watch_dir))
		o.schedule(h, p, recursive=True)
		o.start()
		try:
			while 1:
				sleep(1)
		except KeyboardInterrupt:
			o.stop()
		o.join()


def render_haml(haml_file, dest_file):
	cmd = r'haml %s %s' % (haml_file, dest_file)
	call(cmd, shell=True)
	print 'Regenerated to: %s' % dest_file

class ModifiedHandler(FileSystemEventHandler):

	def __init__(self, target_dir):
		self.target_dir = target_dir
		super(ModifiedHandler, self).__init__()

	def on_any_event(self, e):
		ext = parse_file_ext(e.src_path)
		if not ext == '.haml':
			return
		wp = join(self.target_dir, '%s.html' % splitext(basename(e.src_path))[0])
		render_haml(e.src_path, wp)