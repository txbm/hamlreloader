import logging
from os import unlink, listdir
from os.path import realpath, dirname, join

from nose.tools.trivial import assert_equal
from multiprocessing import Process

from hamlreloader import reloader

logging.basicConfig(level=logging.INFO)

def test_parse_file_ext():
	filename = 'lol.jpg'
	assert_equal(reloader.parse_file_ext(filename), '.jpg')

def test_watch_directory():
	sample_template = ''
	sample_directory = dirname(realpath(__file__)) + '/sample/'
	watch_directory = sample_directory + 'watch/'
	render_directory = sample_directory + 'render/'
	template_directory = sample_directory + 'templates/'
	with open(template_directory + 'haml.tmpl', 'r') as f:
		sample_template = f.read()
	
	p = Process(target=reloader.watch_directory, args=(watch_directory, render_directory))
	p.start()
	if p.is_alive():
		with open(watch_directory + 'test.haml', 'w') as f:
			f.write(sample_template)

		#with open(render_directory + 'test.html', 'r') as f:
		#	print f.read()
	
	p.terminate()
	p.join()

	for f in listdir(watch_directory):
		unlink(join(watch_directory, f))

	for f in listdir(render_directory):
		unlink(join(render_directory, f))
