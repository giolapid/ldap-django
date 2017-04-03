import os

def search_by_user(info):
    os.system('www\\modules\\ldapsearch.exe -b "o=safeway.com" -h ldapvip "uid=%s" cn telephoneNumber mobile title manager mail' %info)