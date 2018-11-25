from django.db import models
from datetime import datetime  
import json
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import RegexValidator

class Currency(models.Model):
	name = models.CharField(max_length=50, unique = True)
	value = models.DecimalField(decimal_places=2,max_digits=5)

class Category(models.Model):
	category_name = models.CharField(max_length=50, validators=[RegexValidator(regex='^[a-zA-Z]*$', message='Category name must be Alphanumeric', code='invalid_category_name' ),])
	order = models.DecimalField(decimal_places=0,max_digits=2)

class RestaurantDetail(models.Model):
	name = models.CharField(max_length=50, unique = True)
	users = models.OneToOneField(User, null = True)
	default_currency = models.OneToOneField(Currency)

class Employee(models.Model):
	POSITIONS = (
		('0', 'waiter'),
		('1', 'cook'),
		('2', 'provaider'),
	)
	statuses = (
		('0', 'offline'),
		('1', 'notactive'),
		('2', 'active'),
	)
	activities = (
		('0', 'active'),
		('1', 'notactive')
	)
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	position = models.CharField(max_length=1, choices=POSITIONS)
	login = models.CharField(max_length=50, unique = True)
	password = models.CharField(max_length=50, default = "password")
	phonenumber = models.CharField(max_length=12)
	status = models.CharField(max_length=1, choices=statuses, default = '0')
	restaurant = models.ForeignKey(RestaurantDetail, null = True)
	active = models.CharField(max_length=1, choices=activities, default = '0')

class LoginLog(models.Model):	
	statuses = (
		('0', 'offline'),
		('1', 'notactive'),
		('2', 'active'),
	)
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=1, choices=statuses)	

class Product(models.Model):
	avs = (
		('0', 'small'),
		('1', 'medium'),
		('2', 'large'),
	)
	name = models.CharField(max_length=50, unique = True)
	av = models.CharField(max_length=2, choices=avs)
	unit = models.CharField(max_length=8)
	def __str__(self):
		return str(self.name)

class Dish(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	STATES = (
		('0', 'available'),
		('1', 'not available'),
	)
	name = models.CharField(max_length=50, unique = True)
	av = models.CharField(max_length=1, choices=STATES)
	price = models.DecimalField(decimal_places=2,max_digits=5)
	tax = models.DecimalField(decimal_places=2,max_digits=4)
	products = models.ManyToManyField(Product)
	description = models.CharField(max_length=300, null = True)
	
class WaiterTask(models.Model):
	STATES = (
		('0', 'started'),
		('1', 'ready'),
		('2', 'done'),
	)
	waiter = models.ForeignKey(Employee, null = True, related_name='waiter')
	cook = models.ForeignKey(Employee)
	currency = models.ForeignKey(Currency)
	price = models.DecimalField(decimal_places=2,max_digits=5, null = True)
	price_default = models.DecimalField(decimal_places=2,max_digits=5, null = True)
	table = models.IntegerField()
	state = models.CharField(max_length=1, choices=STATES, default = '0')
	comment = models.CharField(max_length=200, null = True)
	levels = models.DecimalField(decimal_places=0,max_digits=2)
	created_at = models.DateTimeField(auto_now_add=True)
	
class WaiterOrder(models.Model):
	dish = models.ForeignKey(Dish)
	task = models.ForeignKey(WaiterTask)
	count = models.DecimalField(decimal_places=0,max_digits=2)
	price = models.DecimalField(decimal_places=2,max_digits=5, null = True)
	price_default = models.DecimalField(decimal_places=2,max_digits=5, null = True)	
	comment = models.CharField(max_length=300, null = True)
	level = models.DecimalField(decimal_places=0,max_digits=2)
	created_at = models.DateTimeField(auto_now_add=True)


	

class CookTask(models.Model):
	PRIORITIES = (
		('0', 'normal'),
		('1', 'important'),
		('2', 'for yesterday'),
	)
	STATES = (
		('0', 'started'),
		('1', 'ready'),
		('2', 'done'),
	)
	state = models.CharField(max_length=1, choices=STATES, default = '0')
	cook = models.ForeignKey(Employee, null = True, related_name='cook')
	provider = models.ForeignKey(Employee)
	priority = models.CharField(max_length=1, choices=PRIORITIES, default = '0')
	comment = models.CharField(max_length=300, null = True)
	created_at = models.DateTimeField(auto_now_add=True)

class CookOrder(models.Model):
	product = models.ForeignKey(Product, related_name='product')
	count = models.DecimalField(decimal_places=0,max_digits=2)	
	created_at = models.DateTimeField(auto_now_add=True)
	task = models.ForeignKey(CookTask, related_name='task')
	def __str__(self):
		return str(self.product.name) + ", " + self.count + ", " + self.created_at 
    

class DishPrice(models.Model):
	dish = models.ForeignKey(Dish)
	currency = models.ForeignKey(Currency)
	price = models.DecimalField(decimal_places=2,max_digits=5)
	
	

	
def get_restaurant_current_currency(self): 
	return RestaurantDetail.objects.all().first().default_currency.name
User.add_to_class("get_restaurant_current_currency",get_restaurant_current_currency)	

def get_restaurant_name(self):
	return RestaurantDetail.objects.all().first().name
User.add_to_class("get_restaurant_name",get_restaurant_name)	

from django.utils.html import format_html
import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

def renderEdit(value):
	return format_html('<img class="edit" src="/static/img/edit-icon.png" />',value)
	


