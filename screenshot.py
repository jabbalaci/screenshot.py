#!/usr/bin/env python2
# encoding: utf-8

"""
screenshot.py
=============

Taking a screenshot of a webpage.

Usage:
  * screenshot.py -h
      Help.

  * screenshot.py -full http://reddit.com out.jpg
      Screenshot of the entire page (can be very high).

  * screenshot.py -window http://reddit.com out.jpg
      Screenshot of the area that you see in the browser.

  * screenshot.py -thumb http://reddit.com out.jpg
      Thumbnail of the area that you see in the browser.

Author: Laszlo Szathmary, alias Jabba Laci (jabba.laci@gmail.com), 2015
Blog:   https://pythonadventures.wordpress.com/
"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os
import sys
import tempfile

# customize these if you want (pixels)
WIDTH = 1024
THUMB_WIDTH = 250

RATIO = 4 / 3
HEIGHT = int(WIDTH / RATIO)
ROOT = os.path.dirname(os.path.abspath(__file__))
RASTERIZE_SCRIPT = "{root}/assets/rasterize.js".format(root=ROOT)


def print_help():
    print("""
Taking a screenshot of a webpage.
Usage: {0} option URL output
Options:
  -h, --help    this help
  -window       clip a window (size: {w}*{h})
  -full         entire page
  -thumb        make a thumbnail
""".strip().format(sys.argv[0], w=WIDTH, h=HEIGHT))


def which(program):
    """
    Equivalent of the which command in Python.

    source: http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
    """
    def is_exe(fpath):
        return os.path.exists(fpath) and os.access(fpath, os.X_OK)

    fpath = os.path.split(program)[0]
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def check_required_files():
    if not which("phantomjs"):
        print("Error: phantomjs is not available.")
        print("Tip: install it (http://phantomjs.org/build.html).")
        exit(1)
    if not which("convert"):
        print("Error: convert is not available.")
        print("Tip: it's part of the ImageMagick package.")
        exit(1)
    if not os.path.isfile(RASTERIZE_SCRIPT):
        print("Error: {f} is missing.".format(f=RASTERIZE_SCRIPT))
        exit(1)


def window_screenshot(url, fname):
    return 'phantomjs {rast} "{url}" {out} "{w}px*{h}px"'.format(
        rast=RASTERIZE_SCRIPT, url=url, out=fname,
        w=WIDTH, h=HEIGHT
    )


def full_screenshot(url, fname):
    return 'phantomjs {rast} "{url}" {out} {w}px'.format(
        rast=RASTERIZE_SCRIPT, url=url, out=fname, w=WIDTH
    )


def process_parameters(option, url, fname):
    if option == '-window':
        cmd = window_screenshot(url, fname)
        print('#', cmd)
        os.system(cmd)
    elif option == '-full':
        cmd = full_screenshot(url, fname)
        print('#', cmd)
        os.system(cmd)
    elif option == '-thumb':
        tmp = tempfile.NamedTemporaryFile(dir='.').name + ".png"
        cmd = window_screenshot(url, tmp)
        print('#', cmd)
        os.system(cmd)
        cmd = "convert -resize {w} {tmp} {out}".format(
            w=THUMB_WIDTH, tmp=tmp, out=fname
        )
        print('#', cmd)
        os.system(cmd)
        print('# remove', tmp)
        os.unlink(tmp)
    else:
        print("Error: unknown option.")

##############################################################################

if __name__ == "__main__":
    check_required_files()
    #
    if len(sys.argv) == 1:
        print_help()
    elif len(sys.argv) == 4:
        process_parameters(*sys.argv[1:])
    else:
        print_help()
