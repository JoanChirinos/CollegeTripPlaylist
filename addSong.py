#! /usr/bin/python

import cgi, cgitb

cgitb.enable()

def add():
    fs = cgi.FieldStorage()
    si = [fs.getvalue("songName"), fs.getvalue("songArtist"), fs.getvalue("userName")]
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

def displayThanks():
    print 'Content-type: text/html\n\n'
    print """
                <html>
                    
                    <head>
                        <title>College Trip Playlist</title>
                        <script type="text/javascript">
                            window.location.replace("index.html");
                        </script>
                        <link href="style.css" type="text/css" rel="stylesheet">
                    </head>
                    
                    <body>
                    </body>
                    
                </html>"""
add()
displayThanks()

