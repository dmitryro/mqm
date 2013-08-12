#!/bin/sh

# Change all instances of ‘screen’ to whatever you have named your
# project’s stylesheet, `cd` to the directory in which this file lives and
# simply run `sh watch.sh`.

# No minification
#sass --watch your-project.scss:your-project.css --style compressed

sass --watch screen.scss:../css/screen.min.css --style exanded

exit 0
