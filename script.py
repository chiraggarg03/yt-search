#!/usr/bin/python3

import subprocess
import re
import os

vids = 'https://www.youtube.com/watch?v='

search = input("Enter Search Term : ")
search = search.replace(' ','+')
proc = subprocess.Popen(["curl -s https://www.youtube.com/results?search_query=" + search], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
x = str(out)
video_ids = re.findall(r"watch\?v=(\S{11})",x)

vids += video_ids[0]
run = 'python -m webbrowser -t ' + '"' + vids + '"'

os.system(run)
os.system("killall Terminal")


