# -*- coding: utf-8 -*- 
"""
Software        PyCharm
ProjectName     FastAPI_test
FileName        1.py
Create Time     2021-01-13
System User     Administrator
Author          Smile_yang
"""

from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, )):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


