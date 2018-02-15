#! /usr/bin/python

import cgi, cgitb

cgitb.enable()

def get():
    print 'Content-type: text/html\n\n'
    straw = open("songs.csv", "rU")
    songs = straw.read().split("\n")
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
                        <th><center>Song Name</center></th>
                        <th><center>Song Artist</center></th>
                        <th><center>Submitted By</center></th>
                    </tr>
                    """
    for i in range(len(songs) - 1):
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

            
