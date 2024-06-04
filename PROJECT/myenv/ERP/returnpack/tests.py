from django.test import TestCase

# Create your tests here.

from ninja.testing import TestClient
from django.test import TestCase
from .models import *
from django.test import TestCase ,Client
from django.urls import reverse
from .models import *
import json
from .schemas import *
from .views import api
from . views import *


#MODELS TESTER :


class ModelTestCase(TestCase):
    def setUp(self):
        pass

    def test_customer_creation(self):
        customer = Customer.objects.create(
            type="Type",
            firstname="John",
            lastname="Doe",
            email="john.doe@example.com",
            website="example.com",
            workphone=1234567890,
            phone=9876543210,
            contact="Some contact"
        )
        self.assertEqual(customer.type, "Type")
        self.assertEqual(customer.firstname, "John")
        self.assertEqual(customer.lastname, "Doe")
        self.assertEqual(customer.email, "john.doe@example.com")
        self.assertEqual(customer.website, "example.com")
        self.assertEqual(customer.workphone, 1234567890)
        self.assertEqual(customer.phone, 9876543210)
        self.assertEqual(customer.contact, "Some contact")

    def test_supplier_creation(self):
        supplier = Supplier.objects.create(
            type="Type",
            firstname="Jane",
            lastname="Doe",
            email="jane.doe@example.com",
            workphone=1234567890,
            phone=9876543210
        )
        self.assertEqual(supplier.type, "Type")
        self.assertEqual(supplier.firstname, "Jane")
        self.assertEqual(supplier.lastname, "Doe")
        self.assertEqual(supplier.email, "jane.doe@example.com")
        self.assertEqual(supplier.workphone, 1234567890)
        self.assertEqual(supplier.phone, 9876543210)

    def test_category_creation(self):
        category = Category.objects.create(
            name="Category Name",
            description="Category Description"
        )
        self.assertEqual(category.name, "Category Name")
        self.assertEqual(category.description, "Category Description")

    def test_item_creation(self):
        category = Category.objects.create(
            name="Category Name",
            description="Category Description"
        )
        item = Item.objects.create(
            name="Item Name",
            description="Item Description",
            unit="Unit",
            dimensions=10.0,
            weight=5.0,
            brand="Brand",
            category=category
        )
        self.assertEqual(item.name, "Item Name")
        self.assertEqual(item.description, "Item Description")
        self.assertEqual(item.unit, "Unit")
        self.assertEqual(item.dimensions, 10.0)
        self.assertEqual(item.weight, 5.0)
        self.assertEqual(item.brand, "Brand")
        self.assertEqual(item.category, category)
    


    def test_warehouse_creation(self):
        warehouse = Warehouse.objects.create(
            name="Warehouse Name",
            address="Warehouse Address",
            city="Warehouse City",
            country="Warehouse Country",
            area=100.0,
            capacity=1000,
            openingtime="08:00:00",
            closingtime="18:00:00",
            type="Warehouse Type"
        )
        self.assertEqual(warehouse.name, "Warehouse Name")
        self.assertEqual(warehouse.address, "Warehouse Address")
        self.assertEqual(warehouse.city, "Warehouse City")
        self.assertEqual(warehouse.country, "Warehouse Country")
        self.assertEqual(warehouse.area, 100.0)
        self.assertEqual(warehouse.capacity, 1000)
        self.assertEqual(warehouse.openingtime, "08:00:00")
        self.assertEqual(warehouse.closingtime, "18:00:00")
        self.assertEqual(warehouse.type, "Warehouse Type")

    def test_stock_creation(self):
        category = Category.objects.create(
            name="Category Name",
            description="Category Description"
        )
        item = Item.objects.create(
            name="Item Name",
            description="Item Description",
            unit="Unit",
            dimensions=10.0,
            weight=5.0,
            brand="Brand",
            category=category
        )
        warehouse = Warehouse.objects.create(
            name="Warehouse Name",
            address="Warehouse Address",
            city="Warehouse City",
            country="Warehouse Country",
            area=100.0,
            capacity=1000,
            openingtime="08:00:00",
            closingtime="18:00:00",
            type="Warehouse Type"
        )
        customer = Customer.objects.create(
            type="Type",
            firstname="John",
            lastname="Doe",
            email="john.doe@example.com",
            website="example.com",
            workphone=1234567890,
            phone=9876543210,
            contact="Some contact"
        )
        stock = Stock.objects.create(
            name="Stock Name",
            item=item,
            warehouse=warehouse,
            quantity=10,
            customer=customer
        )
        self.assertEqual(stock.name, "Stock Name")
        self.assertEqual(stock.item, item)
        self.assertEqual(stock.warehouse, warehouse)
        self.assertEqual(stock.quantity, 10)
        self.assertEqual(stock.customer, customer)
    

    def test_packaging_creation(self):
        category = Category.objects.create(
            name="Category Name",
            description="Category Description"
        )
        item = Item.objects.create(
            name="Item Name",
            description="Item Description",
            unit="Unit",
            dimensions=10.0,
            weight=5.0,
            brand="Brand",
            category=category
        )
        packaging = Packaging.objects.create(
            type="Type",
            item=item,
            quantity=10,
            weight=5.0,
            price=50.0,
            capacity=100.0,
            dimensions=20.0,
            unit="Unit",
            storagespace=200.0
        )
        self.assertEqual(packaging.type, "Type")
        self.assertEqual(packaging.item, item)
        self.assertEqual(packaging.quantity, 10)
        self.assertEqual(packaging.weight, 5.0)
        self.assertEqual(packaging.price, 50.0)
        self.assertEqual(packaging.capacity, 100.0)
        self.assertEqual(packaging.dimensions, 20.0)
        self.assertEqual(packaging.unit, "Unit")
        self.assertEqual(packaging.storagespace, 200.0)

    def test_sales_creation(self):
        category = Category.objects.create(
            name="Category Name",
            description="Category Description"
        )
        item = Item.objects.create(
            name="Item Name",
            description="Item Description",
            unit="Unit",
            dimensions=10.0,
            weight=5.0,
            brand="Brand",
            category=category
        )
        sales = Sales.objects.create(
            amount=100.0,
            date="2022-06-01",
            currency="USD",
            payment_method="Cash",
            item=item,
            quantity=5
        )
        self.assertEqual(sales.amount, 100.0)
        self.assertEqual(sales.date, "2022-06-01")
        self.assertEqual(sales.currency, "USD")
        self.assertEqual(sales.payment_method, "Cash")
        self.assertEqual(sales.item, item)
        self.assertEqual(sales.quantity, 5)


    def test_purchase_creation(self):
        category = Category.objects.create(
            name="Category Name",
            description="Category Description"
        )
        item = Item.objects.create(
            name="Item Name",
            description="Item Description",
            unit="Unit",
            dimensions=10.0,
            weight=5.0,
            brand="Brand",
            category=category
        )
        purchase = Purchase.objects.create(
            amount=200.0,
            date="2022-06-01",
            currency="USD",
            payment_method="Credit Card",
            item=item,
            quantity=10
        )
        self.assertEqual(purchase.amount, 200.0)
        self.assertEqual(purchase.date, "2022-06-01")
        self.assertEqual(purchase.currency, "USD")
        self.assertEqual(purchase.payment_method, "Credit Card")
        self.assertEqual(purchase.item, item)
        self.assertEqual(purchase.quantity, 10)

    def test_payment_creation(self):
        category = Category.objects.create(
            name="Category Name",
            description="Category Description"
        )
        item = Item.objects.create(
            name="Item Name",
            description="Item Description",
            unit="Unit",
            dimensions=10.0,
            weight=5.0,
            brand="Brand",
            category=category
        )
        payment = Payment.objects.create(
            amount=150.0,
            date="2022-06-01",
            currency="USD",
            payment_method="Bank Transfer",
            item=item,
            quantity=7
        )
        self.assertEqual(payment.amount, 150.0)
        self.assertEqual(payment.date, "2022-06-01")
        self.assertEqual(payment.currency, "USD")
        self.assertEqual(payment.payment_method, "Bank Transfer")
        self.assertEqual(payment.item, item)
        self.assertEqual(payment.quantity, 7)



    def test_packagingmouvment_creation(self):
        category = Category.objects.create(
            name="Category Name",
            description="Category Description"
        )
        item = Item.objects.create(
            name="Item Name",
            description="Item Description",
            unit="Unit",
            dimensions=10.0,
            weight=5.0,
            brand="Brand",
            category=category
        )
        packaging = Packaging.objects.create(
            type="Type",
            item=item,
            quantity=10,
            weight=5.0,
            price=50.0,
            capacity=100.0,
            dimensions=20.0,
            unit="Unit",
            storagespace=200.0
        )
        packagingmouvment = PackagingMouvment.objects.create(
            name="Mouvment Name",
            packaging=packaging,
            mouvement="In"
        )
        self.assertEqual(packagingmouvment.name, "Mouvment Name")
        self.assertEqual(packagingmouvment.packaging, packaging)
        self.assertEqual(packagingmouvment.mouvement, "In")

    


    def test_order_creation(self):
        customer = Customer.objects.create(
            type="Type",
            firstname="John",
            lastname="Doe",
            email="john.doe@example.com",
            website="example.com",
            workphone=1234567890,
            phone=9876543210,
            contact="Some contact"
        )
        category = Category.objects.create(
            name="Category Name",
            description="Category Description"
        )
        item = Item.objects.create(
            name="Item Name",
            description="Item Description",
            unit="Unit",
            dimensions=10.0,
            weight=5.0,
            brand="Brand",
            category=category
        )
        packaging = Packaging.objects.create(
            type="Type",
            item=item,
            quantity=10,
            weight=5.0,
            price=50.0,
            capacity=100.0,
            dimensions=20.0,
            unit="Unit",
            storagespace=200.0
        )
        order = Order.objects.create(
            customer=customer,
            packaging=packaging,
            item=item,
            order_date="2022-06-01",
            notes="Some notes",
            item_price=100.0,
            returnablepackage_price=50.0,
            status="Pending",
            order_number="Order Number",
            shipping_address="Shipping Address",
            total_amount=150.0,
            payment_method="Payment Method"
        )
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.packaging, packaging)
        self.assertEqual(order.item, item)
        self.assertEqual(order.order_date, "2022-06-01")
        self.assertEqual(order.notes, "Some notes")
        self.assertEqual(order.item_price, 100.0)
        self.assertEqual(order.returnablepackage_price, 50.0)
        self.assertEqual(order.status, "Pending")
        self.assertEqual(order.order_number, "Order Number")
        self.assertEqual(order.shipping_address, "Shipping Address")
        self.assertEqual(order.total_amount, 150.0)
        self.assertEqual(order.payment_method, "Payment Method")

    def test_shipment_creation(self):
        category = Category.objects.create(
            name="Category Name",
            description="Category Description"
        )
        item = Item.objects.create(
            name="Item Name",
            description="Item Description",
            unit="Unit",
            dimensions=10.0,
            weight=5.0,
            brand="Brand",
            category=category
        )
        packaging = Packaging.objects.create(
            type="Type",
            item=item,  
            quantity=10,
            weight=5.0,
            price=50.0,
            capacity=100.0,
            dimensions=20.0,
            unit="Unit",
            storagespace=200.0
        )
        shipment = Shipment.objects.create(
            packaging=packaging,
            tracking_number="Tracking Number",
            status="Status"
        )
        self.assertEqual(shipment.packaging, packaging)
        self.assertEqual(shipment.tracking_number, "Tracking Number")
        self.assertEqual(shipment.status, "Status")



#VIEWS TESTER :
# from rest_framework.test import APIClient
class APITestCase(TestCase):
    def setUp(self):
        # self.client = APIClient()
        self.supplier = Supplier.objects.create(
            type="Type",
            firstname="John",
            lastname="Doe",
            email="john.doe@example.com",
            workphone="123456789",
            phone="987654321"
        )
        self.category = Category.objects.create(
            name="Category Name",
            description="Category Description"
        )
        self.warehouse = Warehouse.objects.create(
            name="Warehouse Name",
            address="Warehouse Address",
            city="Warehouse City",
            country="Warehouse Country",
            area=100.0,
            capacity=1000,
            openingtime="08:00:00",
            closingtime="18:00:00",
            type="Warehouse Type"
        )
        self.item = Item.objects.create(
            name="Item Name",
            description="Item Description",
            unit="Unit",
            dimensions=10.0,
            weight=5.0,
            brand="Brand",
            category=self.category
        )
        self.sales = Sales.objects.create(
            amount=100.0,
            date="2022-06-01",
            currency="USD",
            payment_method="Cash",
            item=self.item,
            quantity=5
        )
        self.purchase = Purchase.objects.create(
            amount=200.0,
            date="2022-06-02",
            currency="USD",
            payment_method="Card",
            item=self.item,
            quantity=10
        )
        self.payment = Payment.objects.create(
            amount=300.0,
            date="2022-06-03",
            currency="USD",
            payment_method="Wire Transfer",
            item=self.item,
            quantity=15
        )
        self.packaging = Packaging.objects.create(
            type="Box",
            item=self.item,
            quantity=20,
            weight=10.0,
            price=50.0,
            capacity=100,
            dimensions=10,
            unit="cm",
            storagespace=5.0
        )
        self.packagingmouvment = PackagingMouvment.objects.create(
            name="Mouvment1",
            packaging=self.packaging,
            mouvement="In"
        )
        self.stock = Stock.objects.create(
            name="Stock1",
            item=self.item,
            warehouse=self.warehouse,
            quantity=50
        )
        self.order = Order.objects.create(
            customer_id=1,
            packaging_id=self.packaging.id,
            item_id=self.item.id,
            order_date="2022-06-04",
            notes="Order notes",
            item_price=100,
            returnablepackage_price=20,
            status="Pending",
            order_number="ORD123",
            shipping_address="123 Street, City",
            total_amount=120,
            payment_method="Card"
        )
        self.shipment = Shipment.objects.create(
            packaging_id=self.packaging.id,
            tracking_number="TRACK123",
            status="Shipped"
        )

