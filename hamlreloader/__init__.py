from argparse import ArgumentParser

from .reloader import watch_directory

def main(*args, **kwargs):
	p = ArgumentParser()
	p.add_argument('watch_dir', nargs='?', default='.')
	p.add_argument('target_dir', nargs='?', default='.')
	a = p.parse_args()
	watch_directory(a.watch_dir, a.target_dir)