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

### Customization

Check out the beginning of the source code. You may want to change `WIDTH`
and `THUMB_WIDTH`.

### Requirements

`screenshot.py` relies on PhantomJS and the command `convert`. `convert`
is part of the ImageMagick package. See <http://phantomjs.org/build.html>
for more information on how to install PhantomJS. We also need the
`rasterize.js` script that comes with PhantomJS. You can find a copy of it
in the `assets/` folder.

### Author

* Laszlo Szathmary, alias Jabba Laci (<jabba.laci@gmail.com>), 2015
* <https://pythonadventures.wordpress.com/>
