import json
import io


def lyricsFromText(tx):
    lns = json.loads(tx)['lyrics']['lines']
    ret = []
    for x in lns:
        ret.append((x['startTimeMs'], x['words']))
    return ret

def lyricsFromFile(file):
    f = io.open(file, 'r', encoding='utf8')
    p = f.read()
    f.close()
    return lyricsFromText(p)


import datetime

def lrcFromArr(arr):
    retstr = ""
    for line in arr:
        rawdt = str(datetime.timedelta(milliseconds=int(line[0])))
        if not rawdt.endswith("000"):
            rawdt = str(datetime.timedelta(milliseconds=int(line[0]) + 1))
        retstr += ("[" + rawdt[:-4]).replace("[0:", "[") + "]" + " " + line[1] + "\n"
    return retstr.strip()

def lrcFileFromArr(arr, fn):
    try:
        print(fn)
        f = io.open(fn, 'w', encoding='utf-8')
        f.write(lrcFromArr(arr).encode('utf-8', 'ignore').decode('utf-8','ignore'))
        f.close()
    except e as Exception:
        print(e)
