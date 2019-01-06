#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils.html import format_html
import django_tables2 as tables
from django.utils.translation import gettext_lazy as _
from .models import Dish, Product, Employee, Category, WaiterTask, RestaurantDetail, ProductTranslation, DishTranslation, Language
def render_av(value):
	if value == "small":
		return format_html(renderSmallAv(),value)
	elif value == "medium":
		return format_html(renderMediumAv(),value)
	elif value == "large":
		return format_html(renderLargeAv(),value)
	else: return format_html(value,value)

def renderSmallAv():
	return '<div class="small av-ico choosen"></div>'
def renderMediumAv():
	return '<div class="medium av-ico choosen"></div>'
def renderLargeAv():
	return '<div class="large av-ico choosen"></div>'
def renderEdit(value):
	return format_html('<img class="edit" src="/static/img/edit-icon.png" />',value)
def renderGps():
	return '<img class="gps-ico" src="/static/img/gps.png" />'
class LanguageTransTable(tables.Table):
	name = tables.Column(verbose_name = _('Name'), attrs={'td': {'class': 'name'},'th': {'class': 'name'}})
	edit = tables.Column(empty_values=(), verbose_name=_('Edit'), attrs={'td': {'class': 'edit'},'th': {'class': 'edit'}})

	def render_edit(self, value):
		return renderEdit(value)	
class CurrencyTable(tables.Table):
	name = tables.Column(verbose_name = _('Name'), attrs={'td': {'class': 'name'},'th': {'class': 'name'}})
	edit = tables.Column(empty_values=(), verbose_name=_('Edit'), attrs={'td': {'class': 'edit'},'th': {'class': 'edit'}})

	def render_edit(self, value):
		return renderEdit(value)	
class ProductTransTable(tables.Table):
	product = tables.Column( verbose_name='',attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})
	name = tables.Column(verbose_name = _('Name'), attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})
	edit = tables.Column(empty_values=(), verbose_name=_('Edit'), attrs={'td': {'class': 'edit'},'th': {'class': 'edit'}})
	id = tables.Column(verbose_name = _('Id'), attrs={'td': {'class': 'small id'},'th': {'class': 'size22'}})
	def render_edit(self, value):
		return renderEdit(value)
	def render_id(self, value):
		return format_html("p"+str(value),value)
class CategoryTransTable(tables.Table):
	category = tables.Column( verbose_name='',attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})
	name = tables.Column( verbose_name='',attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})
	edit = tables.Column(empty_values=(), verbose_name=_('Edit'), attrs={'td': {'class': 'edit'},'th': {'class': 'edit'}})	
	id = tables.Column(verbose_name = _('Id'), attrs={'td': {'class': 'small id'},'th': {'class': 'size22'}})

	def render_id(self, value):
		return format_html("c"+str(value),value)

	def render_edit(self, value):
		return renderEdit(value)
class DishTransTable(tables.Table):
	dish = tables.Column( verbose_name='',attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})
	name = tables.Column(verbose_name = _('Name'), attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})
	description = tables.Column(verbose_name = _('Name'), attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})
	edit = tables.Column(empty_values=(), verbose_name=_('Edit'), attrs={'td': {'class': 'edit'},'th': {'class': 'edit'}})
	id = tables.Column(verbose_name = _('Id'), attrs={'td': {'class': 'small id'},'th': {'class': 'small'}})
	def render_edit(self, value):
		return renderEdit(value)
	def render_id(self, value):
		return format_html("d"+str(value),value)
class ProductTable(tables.Table):
	id = tables.Column(verbose_name =_('Id'), attrs={'td': {'class': 'small id'},'th': {'class': 'small'}})
	av = tables.Column( verbose_name='',attrs={'td': {'class': 'small'},'th': {'class': 'small'}})
	name = tables.Column(verbose_name = _('Name'), attrs={'td': {'class': 'name'},'th': {'class': 'name'}})

	edit = tables.Column(empty_values=(), verbose_name=_('Edit'), attrs={'td': {'class': 'edit'},'th': {'class': 'edit'}})

	def render_edit(self, value):
		return renderEdit(value)
	def render_av(self, value):
		return render_av(value)

class EmployeeTable(tables.Table):
	id = tables.Column(verbose_name = _('Id'), attrs={'td': {'class': 'small id'},'th': {'class': 'small'}})
	status = tables.Column(verbose_name='', attrs={'td': {'class': 'small-status'},'th': {'class': 'small-status'}})
	name = tables.Column(verbose_name = _('Imię'), attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})
	surname = tables.Column( verbose_name=_('Nazwisko'),attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})
	position = tables.Column( verbose_name=_('Pozycja'),attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})
	phonenumber = tables.Column( verbose_name=_('Numer telefonu'),attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})
	reset = tables.Column(empty_values=(),verbose_name='', attrs={'td': {'class': 'status'},'th': {'class': 'status'}})
	edit = tables.Column(empty_values=(), verbose_name='', attrs={'td': {'class': 'edit'},'th': {'class': 'edit'}})

	def render_edit(self, value):
		return renderEdit(value)
	def render_reset(self, value, record):
		if record.active == '1':
			return format_html('<div class="notactive">notactive</div>',value)
		if record.status == "0" : return format_html('<a id="reset" href="/reset/password/?login='+str(record.login)+'&passwordOld='+str(record.password)+'"><div class="notactive reset">resetuj hasło</div></a>',value)
		elif record.status == "1" : return format_html(renderGps(),value)
		elif record.status == "2" : return format_html(renderGps(),value)

	def render_gps(self, value):
		return format_html('<img src="/static/img/gps.png" />',value)

	def render_status(self, value, record):
		if record.active == '1':
			return format_html('<div class="small av-ico choosen">',value)
		if value == "offline" : return format_html('<div class="small av-ico choosen">',value)
		elif value == "notactive" : return format_html('<div class="medium av-ico choosen"></div>',value)
		elif value == "active" : return format_html('<div class="large av-ico choosen"></div>',value)

class CategoryTable(tables.Table):

	category_name = tables.Column(verbose_name = _('Nazwa'), attrs={'td': {'class': 'categoryname'},'th': {'class': 'size22'}})
	edit = tables.Column(empty_values=(), verbose_name='', attrs={'td': {'class': 'edit'},'th': {'class': 'edit'}})
	id = tables.Column(verbose_name = _('Id'), attrs={'td': {'class': 'small id'},'th': {'class': 'small'}})

	def render_edit(self, value):
		return renderEdit(value)
	def render_id(self, value):
		return format_html("c"+str(value),value)
class DishTable(tables.Table):
	#currency = RestaurantDetail.objects.all().first().default_currency.name

	currency = " "
	def __init__(self, *args, **kwargs):
		super(DishTable, self).__init__(*args, **kwargs)
		x = args[1]
		if x:
			self.currency = str(x)


	av = tables.Column( verbose_name=_('Dostępność'),attrs={'td': {'class': 'small'},'th': {'class': 'small'}})
	name = tables.Column(verbose_name = _('Nazwa'), attrs={'td': {'class': 'dishname'},'th': {'class': 'dishname'}})
	id = tables.Column(verbose_name = _('Id'), attrs={'td': {'class': 'small id'},'th': {'class': 'small'}})
	products = tables.Column( verbose_name=_('Produkty'))
	price = tables.Column( verbose_name=_('price'),attrs={'td': {'class': 'status'},'th': {'class': 'status'}})

	edit = tables.Column(empty_values=(), verbose_name=_('Edit'), attrs={'td': {'class': 'edit'},'th': {'class': 'edit'}})

	def render_edit(self, value, record):
		return format_html('<a href="/dish/?d='+str(record.id)+'"><img class="edit" src="/static/img/edit-icon.png" /></a>',value)

	def render_av(self, value):
		if value == "not available":
			return format_html('<div class="small av-ico choosen"></div>',value)
		elif value == "available":
			return format_html('<div class="large av-ico choosen"></div>',value)
		else: return format_html(value,value)
	def render_products(self, value):
		if value is not None:
			return ', '.join([category.name for category in value.all()])
	def render_price(self, value):
		return format_html(str(value)+" "+self.currency,value)

class DishCurrTable(tables.Table):
	#currency = RestaurantDetail.objects.all().first().default_currency.name

	currency = " "
	id = 1
	def __init__(self, *args, **kwargs):
		super(DishTable, self).__init__(*args, **kwargs)
		x = args[1]
		if x:
			self.currency = str(x)
		x = args[2]
		if x:
			self.id = str(x)


	av = tables.Column( verbose_name=_('Dostępność'),attrs={'td': {'class': 'small'},'th': {'class': 'small'}})
	name = tables.Column(verbose_name = _('Nazwa'), attrs={'td': {'class': 'dishname'},'th': {'class': 'dishname'}})
	id = tables.Column(verbose_name = _('Id'), attrs={'td': {'class': 'small id'},'th': {'class': 'small'}})
	products = tables.Column( verbose_name=_('Produkty'))
	price = tables.Column( verbose_name=_('price'),attrs={'td': {'class': 'status'},'th': {'class': 'status'}})

	edit = tables.Column(empty_values=(), verbose_name=_('Edit'), attrs={'td': {'class': 'edit'},'th': {'class': 'edit'}})

	def render_edit(self, value, record):
		return format_html('<a href="/dish/?d='+str(record.id)+'"><img class="edit" src="/static/img/edit-icon.png" /></a>',value)

	def render_av(self, value):
		if value == "not available":
			return format_html('<div class="small av-ico choosen"></div>',value)
		elif value == "available":
			return format_html('<div class="large av-ico choosen"></div>',value)
		else: return format_html(value,value)
	def render_products(self, value):
		if value is not None:
			return ', '.join([category.name for category in value.all()])
	def render_price(self, value):
		return format_html(str(value)+" "+self.currency,value)