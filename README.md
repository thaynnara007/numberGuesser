# NumberGuesser

This is a game where you should think on a prime number between 1 and 8000 and the computer must guess which number it is. You also can give some tips for the computer. The faster you get the computer to guess your number, the better.

---

## Usage 

> Let's create a virtual environment
```shell
$ python3 -m venv venv
```
> Let's activate our virtual environment
* On Mac/Linux:
```shell
$ . /venv/bin/activate
```
> Let's install the dependencies
```shell
$ pip3 install -r requirements.txt
```

> Let's enter in the directory
```shell
$ cd numberGuesser
```
> Let's migrate our data base
```shell
$ python3 manage.py migrate
```
> Let's start the app
```shell
$ python3 manage.py runserver
```
```shell
$ Starting development server at http://localhost:8000/
```

## Technologies

```
Django==3.1.2
```
```
djangorestframework==3.12.1
```
