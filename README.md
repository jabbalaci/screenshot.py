# screenshot.py

Taking a screenshot of a webpage.

`screenshot.py` is a wrapper script that calls `phantomjs` and `convert` to do
the real job. The advantage of `screenshot.py` is its very simple usage.

### Usage

* `screenshot.py -h`

  Help.

* `screenshot.py -full http://reddit.com full.jpg`

  Screenshot of the entire page (can be very high).

* `screenshot.py -window http://reddit.com window.jpg`

  Screenshot of the area that you see in the browser.

* `screenshot.py -thumb http://reddit.com thumb.jpg`

  Thumbnail of the area that you see in the browser.

* Sometimes there is a problem with the JavaScript on the given webpage,
  which can cause PhantomJS to crash :( In this case disable JS rendering
  with the `--nojs` extra option. Then use the script as explained above.

  Example:

  `screenshot.py --nojs -thumb http://buggy-js.com thumb.jpg`

### Customization

Check out the beginning of the source code. You may want to change `WIDTH`
and `THUMB_WIDTH`.

### Requirements

`screenshot.py` relies on PhantomJS and the command `convert`. `convert`
is part of the ImageMagick package. See <http://phantomjs.org/build.html>
for more information on how to install PhantomJS. We also need the
`rasterize.js` script that comes with PhantomJS. You can find a copy of it
in the `assets/` folder. I also put a customized version of the rendering
script to the `assets/` folder called `rasterize-nojs.js` that disables
JavaScript rendering on the given webpage.

### Author / Links

* Laszlo Szathmary, alias Jabba Laci (<jabba.laci@gmail.com>), 2015
* <https://pythonadventures.wordpress.com/2015/07/26/screenshot-py/>
* reddit discussion: <http://redd.it/3cyka8>
* appeared in [ImportPython Weekly Newsletter - Issue No 39](http://importpython.com/newsletter/no/39/)

