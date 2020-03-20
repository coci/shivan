# shivan
Shivan is a lightweight download manager that written in python 🐍 . 

Shivan supports multi-part downloading method .
  
<p>&nbsp;</p>

## usage :

note : if you want to config Shivan please read otherwise please jump to step 2 .

### 1 - how to config:

you can configure Shivan in two terms :

    1 - where to save file after download file

    2 - how much Shivan must split file ( in range 1-8 parts)

to configure please enter :
```
$   python3 main.py --config
```
* note : configuration steps will ask 2 questions and if you hit enter and leave it blank in any of step , it acts :

    1- if step 1 leaved blank : save file in root of project

    2- if step 2 leaved blank : split file in 8 parts


### 2- how it works :

1- install requirements :

```
$   pip install -r requirements.txt
```

2- to download file :

```
$   python3 main.py <url>
```

3- enjoy :)


### contribute :
i appricate any PR or feedbacks to improve Shivan .

### note :
you may have a question (why i create this ?)

answer : i'm very curious about how donwload managers work because of that i wrote Shivan :)
<p>&nbsp;</p>

## TODO:
**Done :**

~~- fix final file name~~

~~- multi-thread download~~

~~- dynamic file extension~~

~~- parts name be same as a file name~~

~~- first show information about file~~

~~- add config file for defualt setting~~

~~- dynamic path~~

~~- url format validation~~

<p>&nbsp;</p>

  
**Short-term :**

- check url is downloadable

- dynamic number of part

- check if all parts downloaded then concate to final_file

- read from clipboard

<p>&nbsp;</p>

**Long-term :**

- MacOS app

- linux app
