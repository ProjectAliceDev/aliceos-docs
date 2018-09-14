#!/usr/bin/python

from shutil import copyfile
import os
import sys

def run_build():
    print "Attempting to delete any existing builds before running..."

    if os.path.exists("docs"):
        os.system("rm -rf docs")
    else:
        pass

    print "Building documentation with documentation-builder..."
    try:
        os.system("documentation-builder --template template.html --output-path ./docs --build-version-branches")
    except:
        print "Something went wrong. Are you sure you have documentation-builder installed?"

    print "Copying GitHub Pages files over..."
    try:
        copyfile(".htaccess", "docs/.htaccess")
        with open("docs/CNAME", "w+") as cname:
            cname.write("docs.aliceos.app")

        copyfile("index.html", "docs/index.html")
    except:
        "Something went wrong. Are you sure that you have the right files?"

def start_serve(action):
    if action == "build-only":
        run_build()
        print "Build completed."
    elif action == "build-local-test":
        run_build()
        print "Attempting to serve content locally..."

        if os.path.exists("docs"):
            os.chdir("docs")
            print "The content will now be served."
            print "Press CTRL+C to quit the serving process."
            os.system("python -m SimpleHTTPServer")
        else:
            print "There's no build directory, silly."
        os.system("clear")
        print "All done!"
        print "Make sure the docs folder remains when you push to GitHub!"
    else:
        print "Error: Argument " + action + " not recognized."

if __name__ == "__main__":
    start_serve(sys.argv[1])