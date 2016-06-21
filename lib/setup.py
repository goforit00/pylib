__author__ = 'junqingfjq'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
import sys
import goforit.pkg_info

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# check the python version. Note: python3 is not supported by setuptools
if float("%d.%d" % sys.version_info[:2]) < 2.6 or float("%d.%d" % sys.version_info[:2]) >= 3.6:
	sys.stderr.write("Your Python version %d.%d.%d is not supported.\n" % sys.version_info[:3])
	sys.stderr.write("the installing requires Python between 2.5 and 3.6.\n")
	sys.exit(1)

source_dir_list = []
package_list = []
data_file_dict = {}
data_file_list = []
#for dir in os.listdir(os.getcwd()):
for dir in os.listdir(os.path.dirname(os.path.realpath(__file__))):
    if os.path.exists(os.path.join(dir, '__init__.py')):
        package_list.append(dir)
        source_dir_list.append(dir)

for source_dir in source_dir_list:
    for rootDir, dirs, files in os.walk(source_dir):
        for dir in dirs:
            dir = os.path.join(rootDir, dir)
            if os.path.exists(os.path.join(dir, '__init__.py')):
                package_list.append(dir.replace(os.sep, '.'))
        for file in files:
            file = os.path.join(rootDir, file)
            if not file.endswith('.py') and not file.endswith('.pyc') and '.svn' not in file and '.git' not in file:
                if rootDir not in data_file_dict.keys():
                    data_file_dict[rootDir] = [file]
                else:
                    data_file_dict[rootDir].append(file)

for k, v in data_file_dict.items():
    data_file_list.append((k, v))

setup(
	name = goforit.pkg_info.package,
	version = goforit.pkg_info.version,
    packages=package_list,
    data_files=data_file_list,
	author = goforit.pkg_info.author,
	author_email = "",
	license = goforit.pkg_info.license,
	description = goforit.pkg_info.short_description,
	long_description = goforit.pkg_info.long_description
	)
