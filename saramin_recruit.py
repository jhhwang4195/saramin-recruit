#!/usr/bin/python
# -*- coding: utf-8 -*-

from requests import get
from bs4 import BeautifulSoup
import os
import sys

OUTPUT_FILE = "saramin_jd.txt"
SARAMIN_URL = "http://api.saramin.co.kr/job-search?keywords=%s&count=100&sr=directhire"

def my_print(f, prt):
	print("{}" .format(prt))
	f.write("{}" .format(prt))

def delete_file():
    rm_command = "rm %s" % OUTPUT_FILE
    os.system(rm_command)

def saramin():
    keywords = ['devops', 'ansible', 'github', '소켓', '패킷', 'docker', 'snmp', 'netconf', 
	'rest', 'slack', 'jenkins', 'KVM', '오픈스택', 'openstack', 'curl', '오픈소스', 
	'프로토콜', 'Multithread', 'Multi thread', '멀티스레드', 'Network Programming', 
	'TCP/IP' '네트워크', 'network']
	
    f = open(OUTPUT_FILE, "a")
    for keyword in keywords:
        my_print(f, "#################################################\n")
        my_print(f, "#%s\n" % keyword)
        my_print(f, "#################################################\n")

        url = SARAMIN_URL % keyword
        r = get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        for job in soup.find_all('job'):
            temp = job.find('company')
            company = temp.text.strip()
            my_print(f, "%s, %s, %s\n" %(company, job.title.text, job.url.text))

        f.write("\n\n")

    f.close()

if __name__ == '__main__':
    delete_file()
    saramin()
