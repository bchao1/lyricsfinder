# lyricsfinder

A lightweight desktop application for lazy people who don't want to open a browser to download lyrics.

## Getting Started

### Prerequisites
You should first make sure the Internet is available, since all lyrics are retrieved from [this site](https://www.azlyrics.com/).
**Python 3.6.1** is used, and the following packages are needed:
```
bs4==0.0.1
requests==2.18.4
tkinter==8.6
```
You can install required packages using *pip*:
```
pip install bs4
```
Check the installed packages by typing:
```
pip freeze
```
For the **tkinter** module, first open a python shell and check its version by typing:
```
import tkinter
print(tkinter.TkVersion)
```

### Installing 
Go to the directory you wish to install **lyricsfinder** and type:
```
git clone https://github.com/Mckinsey666/lyricsfinder
```
You should then see a directory named **lyricsfinder**.

## Running 'lyricsfinder'
Go to the directory, and type on the terminal:
```
python3 lyricsfinder.py
```
You should see the following interface

![alt welcome page](https://github.com/Mckinsey666/lyricsfinder/blob/master/docs/1.png)

Type in the name of the song to search for its lyrics:

![alt welcome page](https://github.com/Mckinsey666/lyricsfinder/blob/master/docs/2.png)

Select the song and download the lyrics!
![alt welcome page](https://github.com/Mckinsey666/lyricsfinder/blob/master/docs/3.png)
![alt welcome page](https://github.com/Mckinsey666/lyricsfinder/blob/master/docs/4.png)

Once you launch **lyricsfinder**, you should see a **lyrics** directory that contains the downloaded lyrics.

## Authors
Brian Chao, National Taiwan University






