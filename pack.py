from distutils.core import setup
import glob
import py2exe

setup(console=["app.py"],
       data_files=[("static",["static/*"])]
                   )

# python mysetup.py py2exe