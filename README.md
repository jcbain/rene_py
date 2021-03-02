# renePY

A set of tools to assist with the simulation package [`descartes`](github.com/jcbain/descartes). A python 🐍 implementation of `rene`.

## Installing

**disclaimer:** renePY includes a dockerfile for your convenience as its capabilities are limited and fairly specific to a set of tasks geared to help with the simulation package `descartes`. For this reason, formal module upload on pip is beyond the scope of this project in its current state. 

If you don't have docker, you should be able to run these modules using `python3`.

steps:

1. clone this repo
2. navigate to rene_py
```sh
$ cd path/to/rene_py
```
3. create the docker image
```sh
$ docker build -t <imagename> .
```

# Utilizing

With the docker image created you can now run a container followed by one of the python scripts

```sh
$ docker run <imagename> list_param_sets.py --help
```

For the `write_json.py` script, a file is written so it would be helpful to mount a directory from your host on the container

```sh
$ docker run -v /path/to/host/dir:/tmp <imagename> write_json.py -i /tmp/input.txt -o /tmp/output.json
```

The `latex_image_produce.py` script quickly formats a string with a list of images that can be embedded into a `.tex` file.

```sh
$ docker run -v /path/to/all/images:/images <imagename> latex_image_produce.py -d /images -n path/in/latex/structure`
```


