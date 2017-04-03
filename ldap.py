import os
import re


def search_by_user(info):
    os.system('www\\modules\\ldapsearch.exe -b "o=safeway.com" -h ldapvip "uid=%s" '
              'cn title mail telephoneNumber mobile  manager > www\\modules\\out.txt' %info)


def search_by_comp(info):
    regex = r"SAFEWAY\w+.\w+"
    os.system('www\\modules\\PsLoggedon.exe /accepteula -l \\\%s > www\\modules\\out.txt' % info)
    with open('www\\modules\\out.txt') as f:
        for line in f:
            result = re.findall(regex, line)

    return result