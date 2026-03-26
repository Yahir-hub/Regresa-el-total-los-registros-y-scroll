import requests
from app.components.error import ApiError

BASE = "http://localhost:8000/products"
TIME_OUT = 10

def list_products(limit:int=20, offset:int=0):
    try:
        r = requests.get(f"{BASE}/", params={"limit":limit, "offset":offset}, timeout=TIME_OUT)
        if 200 <= r.status_code < 300:
            return r.json() if r.content else []
        raise ValueError(f"Error {r.status_code}", r.status_code, r.text)
    except requests.exceptions.RequestException as e:
        raise ValueError("Error de conexión", None, str(e))

def get_product(product_id:str): pass
def create_product(data:dict): pass
def update_product(product_id:str, data:dict): pass
def delete_product(product_id:str): pass