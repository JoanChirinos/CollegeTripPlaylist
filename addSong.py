#! /usr/bin/python

import cgi, cgitb

cgitb.enable()

def add():
    fs = cgi.FieldStorage()
    si = [fs["songName"], fs["songArtist"], fs["userName"]]
    straw = open("songs.csv", "rU")
    text = straw.read()
    straw.close()

    ##Strip new line characters
    while text[-1] == '\n':
        text = text[0:-1]

    text += '\n' + si[0] + ',' + si[1] + ',' + si[2] + '\n'

    straw = open("songs.csv", 'w+')
    straw.write(text)
    straw.close()

add()
