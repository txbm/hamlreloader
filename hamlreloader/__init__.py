import logging

from argparse import ArgumentParser

from os import getcwd

from .reloader import watch_directory

logging.basicConfig(level=logging.INFO)

def main(*args, **kwargs):
	base_dir = getcwd()
	p = ArgumentParser()
	p.add_argument('watch_dir', nargs='?', default=base_dir)
	p.add_argument('target_dir', nargs='?', default=base_dir)
	a = p.parse_args()
	watch_directory(a.watch_dir, a.target_dir)