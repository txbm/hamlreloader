from setuptools import setup, find_packages

setup(
	name="HamlReloader",
	version="0.0.1",
	packages=find_packages(),
	install_requires=['watchdog'],
	entry_points = {
		'console_scripts': [
			'hamwatch = hamlreloader:main'
		]
	}
)