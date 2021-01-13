# -*- coding: utf-8 -*- 
"""
Software        PyCharm
ProjectName     FastAPI_test
FileName        requests_.py
Create Time     2021-01-13
System User     Administrator
Author          Smile_yang
"""

import requests

item = {
    "password": "Demon_2020",
    "username": "Start_2020"
}
password = "Demon_2020"
username = "Start_2020"
# print(json.dumps(item))
# url = f"http://127.0.0.1:8000/items/?item={json.dumps(item)}"
# response = requests.get(url=url)
# print(response.text)
# print(response.url)

url_new = f"http://127.0.0.1:8000/items_new/"
response_new = requests.get(url=url_new)
print(response_new.text)
print(response_new.url)
