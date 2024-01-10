# Adding the root directory to sys.path to resolve the issue of the command line not finding the package.
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
