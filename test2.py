import os
import requests
import json

def test(path):
	str = "hello world";
	print("hello world!!!")
	print("hi, how are you.")
	print(os.path.isdir(path))
	print(os.path.isfile(path))
	idx = str.find(' ');
	print(str[idx+1:])

def testJson():
	f = open("d:\\pythonTest\\channel_v3.json")
	cfgs= json.load(f);
	f.close()
	print(cfgs)
	f =open("d:\\pythonTest\\channel_v3_1.json","w")
	json.dump(cfgs, f,indent=2);
	print(json.dump(cfgs,indent=2))
	f.close()


def test1():
	print("test1")
	res = requests.get("http://www.baidu.com");
	res.encoding = "GBK"
	print(res.content)


test(r'd:\\dbgTest')
#test1()
testJson()