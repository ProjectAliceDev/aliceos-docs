#!/usr/bin/python

import os

print "Attempting to delete any existing builds before running..."

if os.path.exists("build"):
    os.system("rm -rf build")
else:
    pass

print "Building documentation with documentation-builder..."
try:
    os.system("documentation-builder --template template.html --output-path ./docs")
except:
    print "Something went wrong. Are you sure you have documentation-builder installed?"

print "Attempting to serve content locally..."

if os.path.exists("build"):
    os.chdir("build")
    print "The content will now be served."
    print "Press CTRL+C to quit the serving process."
    os.system("python -m SimpleHTTPServer")
else:
    print "There's no build directory, silly."

print "All done!"