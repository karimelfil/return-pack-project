from django.shortcuts import get_object_or_404
from ninja import NinjaAPI , responses 
from .models import *
from .schemas import *
from .enum import *
from django.http import HttpResponse 
from typing import List
api = NinjaAPI()
# Create your views here.

#  create functions : 
@api.post("/customer/", response=customerOut)
def create_customer(request, payload: customerIn):
    customer = Customer.objects.create(
        type=payload.type,
        firstname=payload.firstname,
        lastname=payload.lastname,
        email=payload.email,
        website=payload.website,
        workphone=payload.workphone,
        phone=payload.phone,
        contact=payload.contact
    )
    return customer

@api.post("/supplier/", response=SupplierOut)
def create_supplier(request, payload: SupplierIn):
    supplier = Supplier.objects.create(
        type=payload.type,
        firstname=payload.firstname,
        lastname=payload.lastname,
        email=payload.email,
        workphone=payload.workphone,
        phone=payload.phone
    )
    return supplier

@api.post("/category/", response=categoryOut)
def create_category(request, payload: categoryIn):
    category = Category.objects.create(
        name=payload.name,
        description=payload.description
    )
    return category

@api.post("/item/", response=ItemOut)
def create_item(request, item: ItemIn):
    category = get_object_or_404(Category, id=item.category_id)
    item_obj = Item.objects.create(
        name=item.name,
        description=item.description,
        unit=item.unit,
        dimensions=item.dimensions,
        weight=item.weight,
        brand=item.brand,
        category=category
    )
    return ItemOut(
        name=item_obj.name,
        description=item_obj.description,
        unit=item_obj.unit,
        dimensions=item_obj.dimensions,
        weight=item_obj.weight,
        brand=item_obj.brand,
        category_id=category.id
    )

@api.post("/warehouse/", response=WarehouseOut)
def create_warehouse(request, payload: WarehouseIn):
    warehouse = Warehouse.objects.create(
        name=payload.name,
        address=payload.address,
        city=payload.city,
        country=payload.country,
        area=payload.area,
        capacity=payload.capacity,
        openingtime=payload.openingtime,
        closingtime=payload.closingtime,
        type=payload.type  
    )
    return WarehouseOut(
        id=warehouse.id,
        name=warehouse.name,
        address=warehouse.address,
        city=warehouse.city,
        country=warehouse.country,
        area=warehouse.area,
        capacity=warehouse.capacity,
        openingtime=warehouse.openingtime,
        closingtime=warehouse.closingtime,
        type=warehouse.type
    )

@api.post("/stock/", response=stockOut)
def create_stock(request, stock_in: stockIn):
    item = get_object_or_404(Item, id=stock_in.item_id)
    warehouse = get_object_or_404(Warehouse, id=stock_in.warehouse_id)
    
    stock = Stock.objects.create(
        name=stock_in.name,
        item=item,
        warehouse=warehouse,
        quantity=stock_in.quantity  
    )

    return stockOut(
        id=stock.id,
        name=stock.name,
        item_id=stock.item.id,
        warehouse_id=stock.warehouse.id,
        quantity=stock.quantity 
    )

@api.post("/packaging/create", response=packagingOut)
def create_packaging(request,packaging: packagingIn):
    item = Item.objects.get(pk=packaging.item_id)
    new_packaging = Packaging.objects.create(
        type=packaging.type,
        item=item,
        quantity=packaging.qty,
        weight=packaging.weight,
        price=packaging.price,
        capacity=packaging.capacity,
        dimensions=packaging.dimensions,
        unit=packaging.unit,
        storagespace=packaging.storagespace
    )
    packaging_dict = {
        "id": new_packaging.id,
        "type": new_packaging.type,
        "item_id": new_packaging.item_id,
        "qty": new_packaging.quantity,
        "weight": new_packaging.weight,
        "price": new_packaging.price,
        "capacity": new_packaging.capacity,
        "dimensions": new_packaging.dimensions,
        "unit": new_packaging.unit,
        "storagespace": new_packaging.storagespace
    }
    return packagingOut(**packaging_dict)

@api.post("/sales/", response=SalesOut)
def create_sales(request, sales: SalesIn):
    item = get_object_or_404(Item, id=sales.item_id)
    sales_obj = Sales.objects.create(
        amount=sales.amount,
        date=sales.date,
        currency=sales.currency,
        payment_method=sales.payment_method,
        item=item,
        quantity=sales.quantity,

    )
    return SalesOut(
        amount=sales_obj.amount,
        date=sales_obj.date,
        currency=sales_obj.currency,
        payment_method=sales_obj.payment_method,
        item_id=sales_obj.item.id,
        quantity=sales_obj.quantity,
    )

@api.post("/purchase/", response=purchaseOut)
def create_purchase(request, purchase: purchaseIn):
    item = get_object_or_404(Item, id=purchase.item_id)
    purchase_obj = Purchase.objects.create(
        amount=purchase.amount,
        date=purchase.date,
        currency=purchase.currency,
        payment_method=purchase.payment_method,
        item=item,
        quantity=purchase.quantity
    )
    return purchaseOut(
        amount=purchase_obj.amount,
        date=purchase_obj.date,
        currency=purchase_obj.currency,
        payment_method=purchase_obj.payment_method,
        item_id=purchase_obj.item.id,
        quantity=purchase_obj.quantity
    )

@api.post("/payment/", response=paymentOut)
def create_payment(request, payment: paymentIn):
    item = get_object_or_404(Item, id=payment.item_id)
    payment_obj = Payment.objects.create(
        amount=payment.amount,
        date=payment.date,
        currency=payment.currency,
        payment_method=payment.payment_method,
        item=item,
        quantity=payment.quantity
    )
    return paymentOut(
        amount=payment_obj.amount,
        date=payment_obj.date,
        currency=payment_obj.currency,
        payment_method=payment_obj.payment_method,
        item_id=payment_obj.item.id,
        quantity=payment_obj.quantity
    )

@api.post("/packagingmouvment/", response=PackagingMouvmentOut)
def create_packagingmouvment(request, payload: PackagingMouvmentIn):
    packaging = get_object_or_404(Packaging, id=payload.packaging_id)
    packaging_mouvment = PackagingMouvment.objects.create(
        name=payload.name,
        packaging=packaging,
        mouvement=payload.mouvement
    )
    return PackagingMouvmentOut(
        name=packaging_mouvment.name,
        packaging_id=packaging_mouvment.packaging.id,
        mouvement=packaging_mouvment.mouvement,
        
    )

@api.post("/orders/", response=OrderOut)
def create_order(request, payload: OrderIn):
    customer = get_object_or_404(Customer, id=payload.customer_id)
    packaging = get_object_or_404(Packaging, id=payload.packaging_id)
    item = get_object_or_404(Item, id=payload.item_id)
    
    order = Order.objects.create(
        customer_id=customer.id,  
        packaging_id=packaging.id, 
        item_id=item.id, 
        order_date=payload.order_date,
        notes=payload.notes,
        item_price=payload.item_price,
        returnablepackage_price=payload.returnablepackage_price,
        status=payload.status,
        order_number=payload.order_number,
        shipping_address=payload.shipping_address,
        total_amount=payload.total_amount,
        payment_method=payload.payment_method,
    )
    
    return OrderOut(
        id=order.id,
        customer_id=order.customer_id,
        packaging_id=order.packaging_id,
        item_id=order.item_id,
        order_date=order.order_date,
        notes=order.notes,
        item_price=order.item_price,
        returnablepackage_price=order.returnablepackage_price,
        status=order.status,
        order_number=order.order_number,
        shipping_address=order.shipping_address,
        total_amount=order.total_amount,
        payment_method=order.payment_method,
    )

@api.post("/shipments/", response=ShipmentOut)
def create_shipment(request,payload: ShipmentIn):
    packaging = get_object_or_404(Packaging, id=payload.packaging_id)
    shipment = Shipment.objects.create(  
        packaging_id=packaging.id, 
        tracking_number =payload.tracking_number,
        status=payload.status,

    )
    return ShipmentOut(
       packaging_id=shipment.packaging_id,
       tracking_number=shipment.tracking_number,
       status=shipment.status
    )

# CRUD methods :

@api.put("/customer/{customer_id}/{type}/{firstname}/{lastname}/{email}/{website}/{workphone}/{phone}/{contact}/", response=customerIn)
def update_customer(request, customer_id: int, type: custonerr, firstname: str, lastname: str, email: str, website: str, workphone: int, phone: int, contact: str):
    customer = Customer.objects.filter(id=customer_id).first()
    if not customer:
        return HttpResponse(status=404)

    customer.type = type.value
    customer.firstname = firstname
    customer.lastname = lastname
    customer.email = email
    customer.website = website
    customer.workphone = workphone
    customer.phone = phone
    customer.contact = contact
    customer.save()

    return customerIn(
        type=customer.type,
        firstname=customer.firstname,
        lastname=customer.lastname,
        email=customer.email,
        website=customer.website,
        workphone=customer.workphone,
        phone=customer.phone,
        contact=customer.contact
    )

@api.delete("/customer/{customer_id}/")
def delete_customer(request, customer_id: int):
    customer = Customer.objects.filter(id=customer_id).first()
    if not customer:
        return HttpResponse(status=404)

    customer.delete()
    return HttpResponse(status=204)

@api.put("/supplier/{supplier_id}/{type}/{firstname}/{lastname}/{email}/{workphone}/{phone}/", response=SupplierIn)
def update_supplier(request, supplier_id: int, type: custonerr, firstname: str, lastname: str, email: str, workphone: int, phone: int):
    supplier = Supplier.objects.filter(id=supplier_id).first()
    if not supplier:
        return HttpResponse(status=404)

    supplier.type = type.value
    supplier.firstname = firstname
    supplier.lastname = lastname
    supplier.email = email
    supplier.workphone = workphone
    supplier.phone = phone
    supplier.save()

    return SupplierIn(
        type=supplier.type,
        firstname=supplier.firstname,
        lastname=supplier.lastname,
        email=supplier.email,
        workphone=supplier.workphone,
        phone=supplier.phone,
    )

@api.delete("/supplier/{supplier_id}/")
def delete_supplier(request, supplier_id: int):
    supplier= Supplier.objects.filter(id=supplier_id).first()
    if not supplier:
        return HttpResponse(status=404)

    supplier.delete()
    return {"succces" : True}

@api.put("/category/{category_id}/{name}/{description}/", response=categoryIn)
def update_category(request, category_id: int, name: str, description: str):
    category = Category.objects.filter(id=category_id).first()
    if not category:
        return HttpResponse(status=404)

    category.name = name
    category.description = description
    category.save()

    return categoryIn(
        name=category.name,
        description=category.description
    )

@api.delete("/category/{category_id}/")
def delete_category(request, category_id: int):
    category = Category.objects.filter(id=category_id).first()
    if not category:
        return HttpResponse(status=404)

    category.delete()
    return {"succces" : True}

@api.put("/item/{item_id}/{category_id}/{name}/{description}/{unit}/{dimensions}/{weight}/{brand}/", response=ItemIn)
def update_item(request, item_id: int, category_id: int, name: str, description: str, unit: itemss, dimensions: float, weight: float, brand: str):
    item = Item.objects.filter(id=item_id).first()
    if not item:
        return HttpResponse(status=404)

    category = Category.objects.filter(id=category_id).first()
    if not category:
        return HttpResponse(status=404)

    item.category = category
    item.name = name
    item.description = description
    item.unit = unit.value
    item.dimensions = dimensions
    item.weight = weight
    item.brand = brand
    item.save()

    return ItemIn(
        name=item.name,
        description=item.description,
        unit=item.unit,
        dimensions=item.dimensions,
        weight=item.weight,
        brand=item.brand,
        category_id=category.id
    )

@api.delete("/item/{item_id}/")
def delete_item(request, item_id: int):
    item = Item.objects.filter(id=item_id).first()
    if not item:
        return HttpResponse(status=404)

    item.delete()
    return HttpResponse(status=204)

@api.put("/warehouse/{warehouse_id}/{address}/{city}/{country}/{area}/{capacity}/{openingtime}/{closingtime}/", response=WarehouseIn)
def update_warehouse(request, warehouse_id: int, address: str, city: str, country: str, area: str, capacity: int, openingtime: int, closingtime: int):
    warehouse = Warehouse.objects.filter(id=warehouse_id).first()
    if not warehouse:
        return HttpResponse(status=404)

    warehouse.address = address
    warehouse.city = city
    warehouse.country = country
    warehouse.area = area
    warehouse.capacity = capacity
    warehouse.openingtime = openingtime
    warehouse.closingtime = closingtime
    warehouse.save()

    return WarehouseIn(
        id=warehouse.id,
        address=warehouse.address,
        city=warehouse.city,
        country=warehouse.country,
        area=warehouse.area,
        capacity=warehouse.capacity,
        openingtime=warehouse.openingtime,
        closingtime=warehouse.closingtime,
    )

@api.delete("/warehouse/{warehouse_id}/")
def delete_warehouse(request, warehouse_id: int):
    warehouse = Warehouse.objects.filter(id=warehouse_id).first()
    if not warehouse:
        return HttpResponse(status=404)

    warehouse.delete()
    return HttpResponse(status=204)

@api.put("/stock/{stock_id}/{item_id}/{warehouse_id}/{quantity}/", response=stockIn)
def update_stock(request, stock_id: int, item_id: int, warehouse_id: int, quantity: int):
    stock = Stock.objects.filter(id=stock_id).first()
    if not stock:
        return HttpResponse(status=404)

    item = Item.objects.filter(id=item_id).first()
    if not item:
        return HttpResponse(status=404)

    warehouse = Warehouse.objects.filter(id=warehouse_id).first()
    if not warehouse:
        return HttpResponse(status=404)

    stock.item = item
    stock.warehouse = warehouse
    stock.quantity = quantity
    stock.save()

    return stockIn(
        name=item.name,
        item_id=item.id,
        warehouse_id=warehouse.id,
    )

@api.delete("/stock/{stock_id}/")
def delete_stock(request, stock_id: int):
    stock = Stock.objects.filter(id=stock_id).first()
    if not stock:
        return HttpResponse(status=404)

    stock.delete()
    return HttpResponse(status=204)

@api.put("/sales/{sales_id}/{amount}/{date}/{currency}/{payment_method}/{item_id}/{quantity}/",response=SalesIn)
def update_sales(request, sales_id: int, amount: float, date: date, currency: str, payment_method : str,item_id: int, quantity: int):
    sales = Sales.objects.filter(id=sales_id).first()
    if not sales:
        return HttpResponse(status=404)

    item = Item.objects.filter(id=item_id).first()
    if not item:
        return HttpResponse(status=404)

    sales.amount = amount
    sales.date = date
    sales.currency = currency
    sales.payment_method = payment_method
    sales.item = item
    sales.quantity = quantity
    sales.save()

    return SalesIn(
        amount=sales.amount,
        date=sales.date,
        currency=sales.currency,
        payment_method=sales.payment_method,
        item_id=sales.item_id,
        quantity=sales.quantity 
    )

@api.delete("/sales/{sales_id}/")
def delete_sales(request, sales_id: int):
    sales = Sales.objects.filter(id=sales_id).first()
    if not sales:
        return HttpResponse(status=404)

    sales.delete()
    return HttpResponse(status=204)

@api.put("/purchase/{purchase_id}/{amount}/{date}/{currency}/{payment_method}/{item_id}/{quantity}/",response=purchaseIn)
def update_purchase(request, purchase_id: int, amount: float, date: date, currency: str, payment_method : str,item_id: int, quantity: int):
    purchase = Purchase.objects.filter(id=purchase_id).first()
    if not purchase:
        return HttpResponse(status=404)

    item = Item.objects.filter(id=item_id).first()
    if not item:
        return HttpResponse(status=404)

    purchase.amount = amount
    purchase.date = date
    purchase.currency = currency
    purchase.payment_method = payment_method
    purchase.item = item
    purchase.quantity = quantity
    purchase.save()

    return purchaseIn(
        amount=purchase.amount,
        date=purchase.date,
        currency=purchase.currency,
        payment_method=purchase.payment_method,
        item_id=purchase.item_id,
        quantity=purchase.quantity 
    )

@api.delete("/purchase/{purchase_id}/")
def delete_purchase(request, purchase_id: int):
    purchase = Purchase.objects.filter(id=purchase_id).first()
    if not purchase:
        return HttpResponse(status=404)

    purchase.delete()
    return HttpResponse(status=204)

@api.put("/payment/{payment_id}/{amount}/{date}/{currency}/{payment_method}/{item_id}/{quantity}/",response=paymentIn)
def update_payment(request, payment_id: int, amount: float, date: date, currency: str, payment_method : str,item_id: int, quantity: int):
    payment = Payment.objects.filter(id=payment_id).first()
    if not payment:
        return HttpResponse(status=404)

    item = Item.objects.filter(id=item_id).first()
    if not item:
        return HttpResponse(status=404)

    payment.amount = amount
    payment.date = date
    payment.currency = currency
    payment.payment_method = payment_method
    payment.item = item
    payment.quantity = quantity
    payment.save()

    return paymentIn(
        amount=payment.amount,
        date=payment.date,
        currency=payment.currency,
        payment_method=payment.payment_method,
        item_id=payment.item_id,
        quantity=payment.quantity 
    )

@api.delete("/payment/{payment_id}/")
def delete_payment(request, payment_id: int):
    payment = Payment.objects.filter(id=payment_id).first()
    if not payment:
        return HttpResponse(status=404)

    payment.delete()
    return HttpResponse
    return HttpResponse(status=204)

@api.put("/packaging/{packaging_id}/{type}/{item_id}/{quantity}/{weight}/{price}/{capacity}/{dimensions}/{unit}/{durabilty}/{storagespace}/", response=packagingOut)
def update_packaging(request, packaging_id: int, type: str, item_id: int, quantity: int, weight: float, price: float, capacity: float, dimensions: float, unit: packss, durabilty: int, storagespace: float):
    packaging = Packaging.objects.filter(id=packaging_id).first()
    if not packaging:
        return HttpResponse(status=404)

    item = Item.objects.filter(id=item_id).first()
    if not item:
        return HttpResponse(status=404)

    packaging.type = type
    packaging.item = item
    packaging.quantity = quantity
    packaging.weight = weight
    packaging.price = price
    packaging.capacity = capacity
    packaging.dimensions = dimensions
    packaging.unit = unit.value
    packaging.storagespace = storagespace
    packaging.save()

    return packagingOut(
        type=packaging.type,
        item_id=packaging.item.id,
        qty=packaging.quantity,
        weight=packaging.weight,
        price=packaging.price,
        capacity=packaging.capacity,
        dimensions=packaging.dimensions,
        storagespace=packaging.storagespace
    )

api.delete("/packagingmouvment/{packagingmouvment_id}/")
def delete_packagingmouvment(request, packagingmouvment_id: int):
    packagingmouvment = get_object_or_404(PackagingMouvment, id=packagingmouvment_id)
    packagingmouvment.delete()
    return {"detail": "Packaging movement deleted successfully."}

@api.put("/packagingmouvment/{packagingmouvment_id}/", response=PackagingMouvmentOut)
def update_packagingmouvment(request, packagingmouvment_id: int, data: PackagingMouvmentIn):
    packagingmouvment = get_object_or_404(PackagingMouvment, id=packagingmouvment_id)
    
    packagingmouvment.name = data.name
    packagingmouvment.mouvement = data.mouvement
    
    if packagingmouvment.packaging_id != data.packaging_id:
        packaging = get_object_or_404(Packaging, id=data.packaging_id)
        packagingmouvment.packaging = packaging
    
    packagingmouvment.save()

    packaging = packagingmouvment.packaging
    return PackagingMouvmentOut(
        id=packagingmouvment.id,
        name=packagingmouvment.name,
        packaging_id=packaging.id if packaging else None,
        packaging_name=packaging.name if packaging else None,
        mouvement=packagingmouvment.mouvement,
    )

@api.delete("/packaging/{packaging_id}/")
def delete_packaging(request, packaging_id: int):
    packaging = Packaging.objects.filter(id=packaging_id).first()
    if not packaging:
        return HttpResponse(status=404)

    packaging.delete()
    return HttpResponse(status=204)

@api.put("/orders/{order_id}/", response=OrderOut)
def update_order(request, order_id: int, payload: OrderIn):
    order = get_object_or_404(Order, id=order_id)
    for attr, value in payload.dict().items():
        setattr(order, attr, value)
    order.save()
    updated_order = OrderOut(
        id=order.id,
        customer_id=order.customer_id,
        packaging_id=order.packaging_id,
        item_id=order.item_id,
        order_date=order.order_date,
        notes=order.notes,
        item_price=order.item_price,
        returnablepackage_price=order.returnablepackage_price,
        status=order.status,
        order_number=order.order_number,
        shipping_address=order.shipping_address,
        total_amount=order.total_amount,
        payment_method=order.payment_method,
    )
    
    return updated_order

@api.delete("/orders/{order_id}/")
def delete_order(request, order_id: int):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return {"success": True}

@api.get("/customer/{customer_id}/", response=customerIn)
def get_customer(request, customer_id: int):
    customer = get_object_or_404(Customer, id=customer_id)
    return customerIn(
        id=customer.id,
        type=customer.type,
        firstname=customer.firstname,
        lastname=customer.lastname,
        email=customer.email,
        website=customer.website,
        workphone=customer.workphone,
        phone=customer.phone,
        contact=customer.contact
    )

@api.put("/shipment/{shipment_id}/update")
def update_shipment(request, shipment_id: int, shipment_data: ShipmentIn):
    try:
        shipment_obj = Shipment.objects.get(id=shipment_id)
    except Shipment.DoesNotExist:
        return {"message": "Shipment not found"}
    shipment_obj.packaging_id = shipment_data.packaging_id
    shipment_obj.tracking_number = shipment_data.tracking_number
    shipment_obj.status = shipment_data.status
    shipment_obj.save()

    return {"message": "Shipment updated successfully"}

@api.delete("/shipment/{shipment_id}/delete")
def delete_shipment(request, shipment_id: int):
    try:
        shipment_obj = Shipment.objects.get(id=shipment_id)
    except Shipment.DoesNotExist:
        return {"message": "Shipment not found"}
    shipment_obj.delete()

    return {"message": "Shipment deleted successfully"}
# Get methods :

@api.get("/supplier/{supplier_id}/", response=SupplierIn)
def get_supplier(request, supplier_id: int):
    client = get_object_or_404(Supplier, id=supplier_id)
    return SupplierIn(
        id=client.id,
        type=client.type,
        firstname=client.firstname,
        lastname=client.lastname,
        email=client.email,
        workphone=client.workphone,
        phone=client.phone
    )

@api.get("/category/{category_id}/", response=categoryIn)
def get_category(request, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    return categoryIn(
        id=category.id,
        name=category.name,
        description=category.description
    )

@api.get("/warehouse/{warehouse_id}/", response=WarehouseIn)
def get_warehouse(request,warehouse_id: int):
    warehouse=get_object_or_404(Warehouse,id=warehouse_id)
    return WarehouseIn(
        id=warehouse.id,
        name=warehouse.name,
        address=warehouse.address,
        city=warehouse.city,
        country=warehouse.country,
        area=warehouse.area,
        capacity=warehouse.capacity,
        openingtime=warehouse.openingtime,
        closingtime=warehouse.closingtime,
        type=warehouse.type
    )

@api.get("/item/{item_id}/", response=ItemIn) 
def get_item(request, item_id: int): 
    item = get_object_or_404(Item, id=item_id) 
    return ItemIn( id=item.id, name=item.name, description=item.description, unit=item.unit, dimensions=item.dimensions, weight=item.weight, brand=item.brand, category_id=item.category.id if item.category else None, category_name=item.category.name if item.category else None )

@api.get("/sales/{sales_id}/", response=SalesIn)
def get_sales(request, sales_id: int):
    sales = get_object_or_404(Sales, id=sales_id)
    item = sales.item
    return SalesIn(
        id=sales.id,
        amount=sales.amount,
        date=sales.date,
        currency=sales.currency,
        payment_method=sales.payment_method,
        item_id=item.id if item else None,
        item_name=item.name if item else None,
        quantity=sales.quantity
    )

@api.get("/purchase/{purchase_id}/", response=purchaseIn)
def get_purchase(request, purchase_id: int):
    purchase = get_object_or_404(Purchase, id=purchase_id)
    item = purchase.item
    return purchaseIn(
        id=purchase.id,
        amount=purchase.amount,
        date=purchase.date,
        currency=purchase.currency,
        payment_method=purchase.payment_method,
        item_id=item.id if item else None,
        item_name=item.name if item else None,
        quantity=purchase.quantity
    )

@api.get("/payment/{payment_id}/", response=paymentIn)
def get_payment(request, payment_id: int):
    payment = get_object_or_404(Payment, id=payment_id)
    item = payment.item
    return paymentIn(
        id=payment.id,
        amount=payment.amount,
        date=payment.date,
        currency=payment.currency,
        payment_method=payment.payment_method,
        item_id=item.id if item else None,
        item_name=item.name if item else None,
        quantity=payment.quantity
    )

@api.get("/packaging/{packaging_id}/", response=packagingOut)
def get_packaging(request, packaging_id: int):
    packaging = get_object_or_404(Packaging, id=packaging_id)
    item = packaging.item
    return packagingOut(
        id=packaging.id,
        type=packaging.type,
        item_id=item.id if item else None,
        item_name=item.name if item else None,
        qty=packaging.quantity, 
        weight=packaging.weight,
        price=packaging.price,
        capacity=packaging.capacity,
        dimensions=packaging.dimensions,
        unit=packaging.unit,
        storagespace=packaging.storagespace
    )

@api.get("/packagingmouvment/{packagingmouvment_id}/", response=PackagingMouvmentOut)
def get_packagingmouvment(request, packagingmouvment_id: int):
    packagingmouvment = get_object_or_404(PackagingMouvment, id=packagingmouvment_id)
    packaging = packagingmouvment.packaging
    return PackagingMouvmentOut(
        id=packagingmouvment.id,
        name=packagingmouvment.name,
        packaging_id=packaging.id if packaging else None,
        mouvement=packagingmouvment.mouvement,
    )

@api.get("/stock/{stock_id}/", response=stockIn)
def get_stock(request, stock_id: int):
    stock = get_object_or_404(Stock, id=stock_id)
    item = stock.item
    warehouse = stock.warehouse

    return stockIn(
        name=stock.name,
        item_id=item.id if item else None,
        warehouse_id=warehouse.id if warehouse else None,
        quantity=stock.quantity  
    )

@api.get("/orders/{order_id}/", response=OrderOut)
def get_order(request, order_id: int):
    order = get_object_or_404(Order, id=order_id)
    return OrderOut(
        id=order.id,
        customer_id=order.customer_id,
        packaging_id=order.packaging_id,
        item_id=order.item_id,
        order_date=order.order_date,
        notes=order.notes,
        item_price=order.item_price,
        returnablepackage_price=order.returnablepackage_price,
        status=order.status,
        order_number=order.order_number,
        shipping_address=order.shipping_address,
        total_amount=order.total_amount,
        payment_method=order.payment_method,
    )

@api.get("/shipment/{shipment_id}")
def get_shipment(request, shipment_id: int):
    try:
        shipment_obj = Shipment.objects.get(id=shipment_id)
    except Shipment.DoesNotExist:
        return {"message": "Shipment not found"}
    shipment_data = ShipmentOut(
        packaging_id=shipment_obj.packaging_id,
        tracking_number=shipment_obj.tracking_number,
        status=shipment_obj.status
    )

    return shipment_data.dict()

# Other featues :

@api.get("/supplier/", response=List[SupplierOut])
def list_supplier(request):
    clients = Supplier.objects.all()
    return [
        SupplierOut(
            type=client.type,
            firstname=client.firstname,
            lastname=client.lastname,
            email=client.email,
            workphone=client.workphone,
            phone=client.phone
        ) for client in clients
    ]

@api.get("/supplier/{supplier_id}/", response=List[SupplierOut])
def search_supplier(request, supplier_id: int):
    client = Supplier.objects.filter(id=supplier_id).first()
    if client:
        return [SupplierOut(
            type=client.type,
            firstname=client.firstname,
            lastname=client.lastname,
            email=client.email,
            workphone=client.workphone,
            phone=client.phone,
        )]
    else:
        return responses(status_code=404, content={"message": "Client not found"})
    
@api.get("/supplier/{supplier_id}/",response=List[SupplierIn])
def search_supplier(request,supplier_id : int):
    supplier=Supplier.objects.filter(id=supplier_id).first()
    if supplier : 
        return [SupplierOut(
            type=supplier.type,
            firstname=supplier.firstname,
            lastname=supplier.lastname,
            email=supplier.email,
            workphone=supplier.workphone,
            phone=supplier.phone,

        )
        ]
    else:
        return responses.Response(status_code=404, content={"message": "Customer not found"})

@api.get("/customers/{customer_id}/", response=List[customerOut])
def search_customer(request, customer_id: int):
    customer = Customer.objects.filter(id=customer_id).first()
    if customer:
        return [customerOut(
            type=customer.type,
            firstname=customer.firstname,
            lastname=customer.lastname,
            email=customer.email,
            website=customer.website,
            workphone=customer.workphone,
            phone=customer.phone,
            contact=customer.contact
        )]
    else:
        return responses.Response(status_code=404, content={"message": "Customer not found"})
    
@api.get("/packaging/", response=List[packagingOut])
def list_packaging(request):
    packaging_instances = Packaging.objects.all()
    packaging_list = []
    for packaging_instance in packaging_instances:
        packaging = packagingOut(
            type=packaging_instance.type,
            item_id=packaging_instance.item_id,
            qty=packaging_instance.quantity,
            weight=packaging_instance.weight,
            price=packaging_instance.price,
            capacity=packaging_instance.capacity,
            dimensions=packaging_instance.dimensions,
            storagespace=packaging_instance.storagespace
        )
        packaging_list.append(packaging)
    return packaging_list

@api.get("/stock/", response=List[stockOut])
def list_stock(request):
    stock_instances = Stock.objects.all()
    stock_list = []
    for stock_instance in stock_instances:
        stock = stockOut(
            name=stock_instance.name,
            item_id=stock_instance.item_id,
            warehouse_id=stock_instance.warehouse_id,
            quantity=stock_instance.quantity  
        )
        stock_list.append(stock)
    return stock_list

@api.get("/customer/",response=List[customerOut])
def list_customer(request):
    customer_instaces=Customer.objects.all()
    custumer_list=[]
    for customeer_instance in customer_instaces :
        customer = customerOut(
            type=customeer_instance.type,
            firstname=customeer_instance.firstname,
            lastname=customeer_instance.lastname,
            email=customeer_instance.email,
            website=customeer_instance.website,
            workphone=customeer_instance.workphone,
            phone=customeer_instance.phone,
            contact=customeer_instance.contact,
        )
        custumer_list.append(customer)
    return custumer_list

@api.get("/packaging/returnable/count", response=List[PackagingCountOut])
def list_returnable_packaging(request):
    returnable_packaging_items = Packaging.objects.filter(type='returnable')
    packaging_list = []
    for packaging_item in returnable_packaging_items:
        packaging_list.append(PackagingCountOut(
            item_id=packaging_item.item_id,


            quantity=packaging_item.quantity
        ))
    return packaging_list

@api.get("/stock/company", response=List[stockOut])
def list_company_stock(request):
    company_warehouses = Warehouse.objects.filter(type='company')
    stock_list = []
    for warehouse in company_warehouses:
        stocks = Stock.objects.filter(warehouse=warehouse)
        for stock in stocks:
            stock_list.append(stockOut(
                id=stock.id,
                name=stock.name,
                item_id=stock.item.id,
                warehouse_id=stock.warehouse.id,
                quantity=stock.quantity
            ))
    return stock_list

@api.get("/stock/client", response=List[stockOut])
def list_client_stock(request):
    company_warehouses = Warehouse.objects.filter(type='client')
    stock_list = []
    for warehouse in company_warehouses:
        stocks = Stock.objects.filter(warehouse=warehouse)
        for stock in stocks:
            stock_list.append(stockOut(
                id=stock.id,
                name=stock.name,
                item_id=stock.item.id,
                warehouse_id=stock.warehouse.id,
                quantity=stock.quantity
            ))
    return stock_list

@api.get("/customer/orders/{customer_id}/", response=List[OrderOut])
def history_customer_orders(request, customer_id: int):
    customer = get_object_or_404(Customer, id=customer_id)
    orders = Order.objects.filter(customer=customer)
    customer_order_history = []

    for order in orders:
        order_data = OrderOut(
            id=order.id,
            customer_id=order.customer_id,
            packaging_id=order.packaging_id,
            item_id=order.item_id,
            order_date=order.order_date,
            notes=order.notes,
            item_price=order.item_price,
            returnablepackage_price=order.returnablepackage_price,
            status=order.status,
            order_number=order.order_number,
            shipping_address=order.shipping_address,
            total_amount=order.total_amount,
            payment_method=order.payment_method,
        )
        customer_order_history.append(order_data)

    return customer_order_history

@api.get("/packaging/returnable/stock/increase/")
def increase_stock_quantity_on_return(request):
    returnable_packaging_items = Packaging.objects.filter(type='returnable')
    for packaging_item in returnable_packaging_items:
        try:
            stock_items = Stock.objects.filter(item_id=packaging_item.item_id)
            if stock_items.exists():
                stock_item = stock_items.first() 
                total_quantity = sum(stock.quantity for stock in stock_items)
                stock_item.quantity += packaging_item.quantity
                stock_item.save()
            else:
                stock_item = Stock.objects.create(item_id=packaging_item.item_id, quantity=packaging_item.quantity)
                total_quantity = packaging_item.quantity
                
            print(f"Item ID: {packaging_item.item_id}, Total Quantity: {total_quantity}")
        except Exception as e:
            return {"error": str(e)}
    return {"message": "Stock quantities updated successfully"}

@api.get("/shipment/", response=List[ShipmentOut])
def list_shipments(request):
    shipments = Shipment.objects.all()
    shipments_list = [
        ShipmentOut(
            packaging_id=shipment.packaging_id,
            tracking_number=shipment.tracking_number,
            status=shipment.status
        ) for shipment in shipments
    ]
    return shipments_list

@api.get("/item/",response=List[ItemOut])
def list_item(request):
    item_instaces=Item.objects.all()
    item_list=[]
    for item_instance in item_instaces :
        item = ItemOut(
            name=item_instance.name,
            description=item_instance.description,
            unit=item_instance.unit,
            dimensions=item_instance.dimensions,
            weight=item_instance.weight,
            brand=item_instance.brand,
            category_id=item_instance.category_id,
        )
        item_list.append(item)
    return item_list

@api.get("/packaging/shipments/{packaging_id}/", response=List[ShipmentOut])
def packaging_shipment_status_tracking(request, packaging_id: int):
    packaging = get_object_or_404(Packaging, id=packaging_id)
    shipment = Shipment.objects.filter(packaging=packaging)
    packaging_shipment_status = []

    for shipments in shipment:
        shipment_data = ShipmentOut(
            id=shipments.id,
            status=shipments.status,
            packaging_id=shipments.packaging_id,
            tracking_number=shipments.tracking_number
        )
        packaging_shipment_status.append(shipment_data)

    return packaging_shipment_status

@api.get("/stock/{stock_id}/", response=List[stockOut])
def search_stock(request, stock_id: int):
    stock = Stock.objects.filter(id=stock_id).first()
    if stock:
        return [stockOut(
            name=stock.name,
            item_id=stock.item,
            warehouse_id=stock.warehouse,
            quantity=stock.quantity


        )]
    else:
        return responses.Response(status_code=404, content={"message": "Stock not found"})
    


@api.get("/warehouse/{warehouse_id}/", response=List[WarehouseOut])
def search_warehouse_by_city(request, warehouse_id: int):
    warehouse = Warehouse.objects.filter(id=warehouse_id).first
    if warehouse:
        return [WarehouseOut(
            name=warehouse.name,
            id=warehouse.id,
            address=warehouse.address,
            city=warehouse.city,
            country=warehouse.country,
            area=warehouse.area,
            capacity=warehouse.capacity,
            openingtime=warehouse.openingtime,
            closingtime=warehouse.closingtime,
            type=warehouse.type




        )]
    else:
        return responses.Response(status_code=404, content={"message": "Warehouse not found"})
    