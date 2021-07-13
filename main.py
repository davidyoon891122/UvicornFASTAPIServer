from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import requests
### python main.py --reload -> reload 옵션 넣어주면, 파일 저장 될 때마다 재시작 해줌
###
###
app = FastAPI()


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Optional[bool] = None # None을 넣어주어서 옵션 변수가 된다. None 빼면 옵션값 없을 시 에러

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id":item_id, "q":q}


# @app.put("items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id, "itme_price":item.price}

db = []

class City(BaseModel):
    name: str
    timezone: str

@app.get("/")
def root():
    return {"Hello":"World"}

@app.get('/cities')
def get_cities():
    results = []
    for city in db:
        strs = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
        r = requests.get(strs)
        cur_time = r.json()['datetime']
        results.append({'name':city['name'], 'timezone':city['timezone'], 'current_time':cur_time})
    return results


@app.get('/cities/{city_id}')
def get_city(city_id: int):
    city = db[city_id-1]
    strs = f"https://worldtimeapi.org/api/timezone/{city['timezone']}"
    r = requests.get(strs)
    cur_time = r.json()['datetime']
    return {'name':city['name']}, {'timezone':city['timezone']}, {'current_time':cur_time}


@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1]

@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)

    return {}
