from distutils.core import setup
import py2exe

setup(console=['miner.py'],
		options={
			"py2exe":{
				"packages": ["frontend", "pool", "worker"]
			}
		})

