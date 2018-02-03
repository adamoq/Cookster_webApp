from django.db import models
from datetime import datetime  
import json
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Category(models.Model):
	name = models.CharField(max_length=50)
	
class Employee(models.Model):
	POSITIONS = (
		('0', 'waiter'),
		('1', 'cook'),
		('2', 'provaider'),
	)
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	position = models.CharField(max_length=1, choices=POSITIONS)
	login = models.CharField(max_length=50)
	password = models.CharField(max_length=50, default = "password")
		
class Product(models.Model):
	avs = (
		('0', 'small'),
		('1', 'medium'),
		('2', 'large'),
	)
	name = models.CharField(max_length=50)
	av = models.CharField(max_length=2, choices=avs)
	

class Dish(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE )
	STATES = (
		('0', 'available'),
		('1', 'not available'),
	)
	name = models.CharField(max_length=50)
	av = models.CharField(max_length=1, choices=STATES)
	products = models.ManyToManyField(Product)
	
		
class WaiterTask(models.Model):
	STATES = (
		('0', 'started'),
		('1', 'ready'),
		('2', 'done'),
	)
	waiter = models.ForeignKey(Employee, on_delete=models.CASCADE )
	dishes = models.ManyToManyField(Dish)
	table = models.IntegerField()
	state = models.CharField(max_length=1, choices=STATES, default = '0')
	comment = models.CharField(max_length=200, default = ' ')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
class CookTask(models.Model):
	PRIORITIES = (
		('0', 'normal'),
		('1', 'important'),
		('2', 'for yesterday'),
	)
	provider = models.ForeignKey(Employee, on_delete=models.CASCADE)
	products = models.CharField(max_length=300, default = ' ')
	priority = models.CharField(max_length=1, choices=PRIORITIES, default = '0')
	comment = models.CharField(max_length=200, default = ' ')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)