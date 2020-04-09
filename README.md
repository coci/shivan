# Shivan ![Version 1.0](http://img.shields.io/badge/version-v1.0-green.svg) ![Python 3.8](http://img.shields.io/badge/python-3.8-blue.svg) ![GNU 3](http://img.shields.io/badge/license-MIT%20License-blue.svg)

Shivan is a lightweight download manager that have been written in python :snake:.
Shivan supports multi-part downloading method.

### Getting Started

#### 1. Configuring

you can configure Shivan in two terms :

1. where to save file after Shivan downloads the file
2. how much Shivan must split file ( in range 1-8 parts)

To configure enter:

```bash
$ python3 main.py --config
```

Tip: Configuration steps will ask 2 questions and if you hit enter and leave it empty in any of step , it acts in:

1. if step 1 leaved blank : save file in root of project
2. if step 2 leaved blank : split file in 8 parts

#### 2. Usage

##### 2.1. Install Requirements

```bash
$ pip install -r requirements.txt
```

##### 2.2. Run-up

```bash
$ python3 main.py <url>
```

### Contribution

I appreciate any PR or feedbacks to improve Shivan.

### Tip

You may ask "why i made this"?

answer: I'm very curious about how donwload managers work because of that i wrote Shivan :)

### ToDo

- [x] fix final file name
- [x] multi-thread download
- [x] dynamic file extension
- [x] parts name be same as a file name
- [x] first show information about file
- [x] add config file for defualt setting
- [x] dynamic path
- [x] url format validation
- [x] check url is downloadable

__Short-term__

- Dynamic number of part
- Check if all parts downloaded then concate to final_file
- Read from clipboard
- Turn it to pypi package
- Create setup.py installation

__Long-term__

- MacOS app
- Linux app
