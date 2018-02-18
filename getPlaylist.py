#! /usr/bin/python

import cgi, cgitb
from random import shuffle

cgitb.enable()

def get():
    fs = cgi.FieldStorage()
    order = fs.getvalue("order", "none")
    
    print 'Content-type: text/html\n\n'
    straw = open("songs.csv", "rU")
    songs = straw.read().split("\n")
    while (songs[-1] == ""):
        songs = songs[0:-1]

    if order = "songName":
        songs = sorted(songs)
    elif order = "songArtist":
        songs = sorted(songs, key = lambda x: x[1])
    elif order = "submittedBy":
        songs = sorted(songs, key = lambda x: x[2])
    else:
        shuffle(songs)
        
        
    end = """
<html>
    <head>
        <title>College Trip Playlist</title>
        <link href="style.css" type="text/css" rel="stylesheet">
    </head>
    
    <body>
        <center>
            <h1>Winter 2018 Trip</h1>
            <table>
                <table>
                    <tr class="tableHead">
                        <th><a href="getPlaylist.py?order=songName"><center>Song Name</center></a></th>
                        <th><a href="getPlaylist.py?order=songArtist"><center>Song Artist</center></a></th>
                        <th><a href="getPlaylist.py?order=submittedBy"><center>Submitted By</center></a></th>
                    </tr>
                    """
    for i in range(len(songs)):
        if i % 2 == 0:
            toPrint = """
                    <tr class="oddRow">
                        <td><center>SONGNAME</center></td>
                        <td><center>ARTISTNAME</center></td>
                        <td><center>SUBMITTEDBY</center></td>
                    </tr>
                    """
            splitsongs = songs[i].split(',')
            toPrint = toPrint.replace('SONGNAME', splitsongs[0])
            toPrint = toPrint.replace('ARTISTNAME', splitsongs[1])
            toPrint = toPrint.replace('SUBMITTEDBY', splitsongs[2])
            end +=  toPrint
        else:
            toPrint = """
                    <tr class="evenRow">
                        <td><center>SONGNAME</center></td>
                        <td><center>ARTISTNAME</center></td>
                        <td><center>SUBMITTEDBY</center></td>
                    </tr>
                    """
            splitsongs = songs[i].split(',')
            
            toPrint = toPrint.replace('SONGNAME', splitsongs[0])
            toPrint = toPrint.replace('ARTISTNAME', splitsongs[1])
            toPrint = toPrint.replace('SUBMITTEDBY', splitsongs[2])
            end +=  toPrint
    end +=  """
</table>
        </center>
        <a href="index.html"><div class="back">Back</div></a>
        <div class="creds">~Joan Chirinos, 2018</div>
    </body>
</html>
"""

    print end
            


get()

            
