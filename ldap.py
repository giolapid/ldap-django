import os
import re


def search_by_user(info):
    os.system('www\\static\\modules\\ldapsearch.exe -b "o=safeway.com" -h ldapvip "uid=%s" '
              'cn title mail telephoneNumber mobile  manager > www\\static\\modules\\out.txt' %info)


def search_by_comp(info):
    regex = r"SAFEWAY\w+.\w+"
    os.system('www\\static\\modules\\PsLoggedon.exe /accepteula -l \\\%s > www\\static\\modules\\out.txt' % info)
    with open('www\\static\\modules\\out.txt') as f:
        for line in f:
            result = re.findall(regex, line)

    return result