# -*- coding: utf-8 -*- 
"""
Software        PyCharm
ProjectName     FastAPI_test
FileName        2.py
Create Time     2021-01-13
System User     Administrator
Author          Smile_yang
"""
import json
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Query

app = FastAPI()


class Item(BaseModel):
    password: Optional[str] = Query(None, min_length=3, max_length=50, regex="[a-zA-Z0-9.*@#?]")
    username: Optional[str] = Query(None, min_length=6, max_length=50, regex="[a-zA-Z_]")


@app.get("/items/")
async def read_items(
        item: str
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    print(item)
    data_info = json.loads(item, strict=False)
    if data_info:
        results.update({"password": data_info.get('password'), "username": data_info.get('username')})
    return results


@app.get("/items_new/")
async def read_items(
        item: Optional[Item] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    print(item)
    if item:
        if item.password:
            results.update({"password": item.password})
        if item.username:
            results.update({"username": item.username})
    return results
