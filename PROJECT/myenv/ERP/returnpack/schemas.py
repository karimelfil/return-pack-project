from ninja import Schema
from pydantic import BaseModel
from typing import List
from datetime import date ,time

class customerIn(BaseModel):
    type: str
    firstname: str
    lastname: str
    email: str
    website: str
    workphone: int
    phone: int
    contact: str

class customerOut(Schema):
    type: str
    firstname: str
    lastname: str
    email: str 
    website: str 
    workphone: int
    phone: int 
    contact: str = None

class SupplierIn(BaseModel):
    type : str
    firstname : str
    lastname : str
    email : str 
    workphone : int
    phone : int 

class SupplierOut(Schema):
    type : str
    firstname : str
    lastname : str
    email : str 
    workphone : int
    phone : int 

class categoryIn(BaseModel):
    name: str
    description : str

class categoryOut(Schema):
    name: str
    description : str   

class ItemIn(BaseModel):
    name : str
    description : str
    unit : str
    dimensions: float
    weight : float
    brand : str
    category_id : int

class ItemOut(Schema):
    name : str
    description : str
    unit : str
    dimensions : float
    weight : float
    brand : str
    category_id : int

class WarehouseIn(BaseModel):
    name: str
    address: str
    city: str
    country: str
    area: float
    capacity: int
    openingtime: time
    closingtime: time
    type: str  

class WarehouseOut(BaseModel):
    id: int
    name: str
    address: str
    city: str
    country: str
    area: float
    capacity: int
    openingtime: time
    closingtime: time
    type: str

class stockIn(BaseModel):
    name: str
    item_id: int
    warehouse_id: int
    quantity: int

class stockOut(Schema) :
    name : str
    item_id : int
    warehouse_id : int 
    quantity: int


class SalesIn(BaseModel):
    amount: float
    date: date
    currency: str
    payment_method: str
    item_id: int
    quantity: int

class SalesOut(BaseModel):
    amount: float
    date: date
    currency: str
    payment_method: str
    item_id: int
    quantity: int

class purchaseIn(BaseModel):
    amount: float
    date: date
    currency: str
    payment_method: str
    item_id: int
    quantity: int

class purchaseOut(Schema):
    amount: float
    date: date
    currency: str
    payment_method: str
    item_id: int
    quantity: int

class paymentIn(BaseModel):
    amount: float
    date: date
    currency: str
    payment_method: str
    item_id: int
    quantity: int

class paymentOut(Schema):
    amount: float
    date: date
    currency: str
    payment_method: str
    item_id: int
    quantity: int

class PackagingCountOut(BaseModel):
    item_id: int
    quantity: int

class packagingIn(BaseModel):
    type: str
    item_id: int
    qty: int
    weight: float
    price: float
    capacity: float
    dimensions: float
    unit: str
    storagespace: int

class packagingOut(BaseModel):
    type : str
    item_id : int
    qty : int
    weight : float
    price : float
    capacity : float
    dimensions : float
    storagespace : int 

class PackagingMouvmentIn(BaseModel):
    name: str
    packaging_id: int
    mouvement: str

class PackagingMouvmentOut(BaseModel):
    name: str
    packaging_id: int
    mouvement: str
  
class OrderIn(BaseModel):
    customer_id: int
    packaging_id: int
    item_id: int
    order_date: date
    notes: str
    item_price: float
    returnablepackage_price: float
    status: str 
    order_number: str
    shipping_address: str
    total_amount: float
    payment_method: str

class OrderOut(BaseModel):
    id: int
    customer_id: int
    packaging_id: int
    item_id: int
    order_date: date
    notes: str
    item_price: float
    returnablepackage_price: float
    status: str
    order_number: str
    shipping_address: str
    total_amount: float
    payment_method: str

class ShipmentIn(BaseModel):
    packaging_id:int 
    tracking_number: str
    status: str

class ShipmentOut(BaseModel):
    packaging_id:int 
    tracking_number: str
    status: str





    