import subprocess
import io, time, random, math, json
from spotifyface import *
import glob, os

def grab(trid, clt, br):
    if "open.sp" in trid:
        trid = trid.replace("https://open.spotify.com/track/", "")
        trid = trid.split("?")[0]
        print(trid)
    subprocess.Popen(['[your path]/grab.bat', trid, clt, br], cwd="[your path]/") #[your path] is where it will be saved and where the .bat is located

clid = input("Enter client id: ")
bearer = input("Enter bearer: ")

plid = input("Enter playlist id: ")

pls = sp.playlist(plid)

itm = [apiTrackToNormal(x['track']) for x in pls['tracks']['items']]

for x in itm:
    if x[0] in blocklist:
        continue
    else:
        print(x[0] + " not blocked")
    grab(x[0], clid, bearer)

f = io.open("out" + str(math.ceil(time.time())) + ".json", 'w', encoding='utf8')
f.write(json.dumps(itm))
f.close()

for trk in itm:
    if not os.path.exists("your path" + trk[0] + ".json"):
        continue
    ff = io.open("your path" + trk[0] + ".json", 'r', encoding='utf8')
    fr = ff.read()
    ff.close()
    print(trk[0])
    lrcFileFromArr(lyricsFromText(fr), "[your path]\\" + slugify(trk[2] + " - " + trk[1]) + ".lrc")
