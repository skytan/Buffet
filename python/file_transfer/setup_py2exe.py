from distutils.core import setup
import py2exe
import sys

includes = ["encodings", "encodings.*"]
sys.argv.append("py2exe")
options = {"py2exe": {"bundle_files": 3}
           }

#setup(console=["sample2.py"])
setup(options = options,
	  zipfile = None,
	  console = [{"script": 'cpy.py'} ]
	  )