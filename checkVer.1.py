import requests
import re
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
start = time.clock()  
print(start)
with open("first5k.txt", "r") as ins:
    array = []
    i=1
    for line in ins:
        # if i%50==0:
        #     print(str(i)+"%")
        #     i=i+1
        print(i)
        i=i+1
        host="http://"+line.strip()
        try:
            r = requests.post(host+"/CHANGELOG.txt", verify=False)
            data = r.text
        except Exception:
            data = ""
        if "Drupal" in data and "<!doctype html>" not in data and "<!DOCTYPE html>" not in data:
            # print("ok")
            check = True
            sline=0
            while check:
                data = r.text.split('\n')[sline]
                if "Drupal" in data and "xxxx" not in data:
                    check=False
                else:
                    sline=sline+1
            result = host+" "+data
            array.append(result)
with open('outputF5k.txt', 'w') as f:
    for item in array:
        f.write("%s\n" % item)
print(time.clock() - start)