import urllib.request
import urllib.parse
import json
import time

print("*"*100)
print("En-CN Translate v1.0 2018.03.26\nmake by Jarvis.")
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print("*"*100)
while True:
    head = {}
    head['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    url = 'http://fanyi.baidu.com/sug'
    keyword = input("Enter the word you want to Translate(enter 'q!' to quit): ")
    if keyword == 'q!':
        break
    data = {}
    data['kw']=keyword
    data = urllib.parse.urlencode(data).encode('utf_8')
    req = urllib.request.Request(url,data)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf_8')
    target = json.loads(html)
    #print(target)
    if target['errno'] == 0:
        print("Result: %s\n"%(target['data'][0]['v']))
    else :
        print("can not found the result, please enter again.\n")
#input("Press <enter> to quit.")