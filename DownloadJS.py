import sys, os
import requests
import argparse
import jsbeautifier


parser = argparse.ArgumentParser()

parser.add_argument('-c', '--cookie' , help='cookie string')
parser.add_argument('-o', '--output' , help='directory output', default='jsfile')
res = parser.parse_args()

cookies = dict(cookies_are=res.cookie)

if os.path.isdir(res.output) == False:
    os.mkdir(res.output)


def startX(url, cookies):
    try:
        r = requests.get(url.rstrip('\n'), cookies=cookies, verify=False)
        if r.status_code == 200:
            urlsplit = r.url.split("/")
            CountUrl = len(urlsplit) - 1
            print("[DOWNLOAD =>] " + urlsplit[CountUrl])
            if os.path.exists(res.output + "/" + urlsplit[2] + "/"):
                pass
            else:
                os.mkdir(res.output + "/" + urlsplit[2] + "/")

            with open(res.output + "/" + urlsplit[2] + "/" + urlsplit[CountUrl], 'wb') as f:
                f.write(r.content)
                res1 = jsbeautifier.beautify_file(res.output + "/" + urlsplit[2] + "/" +  urlsplit[CountUrl])
                f.write(res1.encode())
    except KeyboardInterrupt:
        print("== Выход из скрипта! ==")
        exit()


for url in sys.stdin:
    startX(url, cookies)
