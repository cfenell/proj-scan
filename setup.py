from distutils.core import setup

setup(name = "proj-scan", 
      version="2018031201", 
      author="Carl-Fredrik Enell",
      author_email="fredrik@kyla.kiruna.se",
      url="http://kyla.kiruna.se/~fredrik/",
      package_dir = {'': 'modules'},
      py_modules = ['pcom'],
      scripts = ['scripts/projscan.py'],
  )
