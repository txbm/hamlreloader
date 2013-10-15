from setuptools import setup, find_packages

setup(
	name="hamlreloader",
	version="0.0.1",
	url='http://github.com/petermelias/hamlreloader',
	license='MIT',
	author='Peter M. Elias',
	author_email='petermelias@gmail.com',
	description='Dead simple watcher / reloader for HAML',
	packages=find_packages(),
	install_requires=['watchdog'],
	extras_require={
		'test': ['nose', 'coveralls']
	},
	entry_points = {
		'console_scripts': [
			'hamwatch = hamlreloader:main'
		]
	},
	classifiers=[
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
		'Topic :: Software Development :: Libraries :: Python Modules'
	]
)