from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

quote_page = "http://codeforces.com/contest/1011/problem/A"
page = urlopen(quote_page)
soup = BeautifulSoup(page,'html.parser')
q_block = soup.find("div",class_='sample-test')
input_blocks = soup.find_all("div",class_='input')
output_blocks = soup.find_all("div",class_='output')

os.system("g++ A.cpp -o run.exe")

for i,j in zip(input_blocks,output_blocks):
	inputs = str(i.find("pre"))
	inputs = inputs.replace('<br/>','\n').replace('<pre>','\n').replace('</pre>','\n')
	# print(inputs)
	f = open('inputs.txt','w+')
	f.write(inputs)
	f.close()
	
	outputs = str(j.find("pre"))
	outputs = outputs.replace('<br/>','\n').replace('<pre>','\n').replace('</pre>','\n')
	# print(outputs)
	outputs = outputs.replace('\n','')

	os.system("./run.exe < inputs.txt >outputs.txt")

	with open('outputs.txt','r') as ff:
		data = ff.read()
		if(data.replace('\n','')==outputs.replace('\n','')):
			print("Correct")
		else:
			print("Incorrect")
			print(data)
			print(outputs)

print("\n Test with your own data\n ")
os.system('./run.exe')
os.system('rm run.exe inputs.txt outputs.txt')

