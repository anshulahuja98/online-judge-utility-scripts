from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import sys
user_base_url = "https://www.spoj.com/users/"
user = str(sys.argv[1])
url = user_base_url + user + '/'

problem_list_page = urlopen(url)
soup = BeautifulSoup(problem_list_page,'html.parser')
td_list = soup.find_all('td')
q_list = []
for td in td_list:
	question_code = str(td.text)
	q_list.append(question_code)
	# print(question_code)

q_date_list = []
submission_base_url = "https://www.spoj.com/status/"
for problem in q_list:
	submission_page_url = submission_base_url + problem + ',' + user + '/'
	submission_page = urlopen(submission_page_url)
	soup = BeautifulSoup(submission_page,'html.parser')
	span = soup.find_all("span")[2]
	date =  str(span.text)
	problem_base_url = "https://www.spoj.com/problems/"
	problem_url = problem_base_url+problem+'/'
	print(problem,date,problem_url)
	if '<' not in [problem,date,problem_url]:
		q_date_list.append([problem,date,problem_url])
	

q_date_list = sorted(q_date_list, key=lambda y: (int(y[1][0:4]),int(y[1][5:7]),int(y[1][8:10])))

f = open('datewise_problems_%s.txt'%user,'w+')
for problem in q_date_list: 
	f.write(problem[2]+ " " + problem[1]+'\n')
f.close()

