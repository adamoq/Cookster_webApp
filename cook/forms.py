# -*- coding: utf-8 -*-
from django import forms
from .models import Product, Dish, Employee, Category, DishTranslation, Language,ProductTranslation, CategoryTranslation, Currency, DishPrice, DishProduct
from django.utils.translation import gettext as _
class ProductForm(forms.ModelForm):
	avs = (
		('0', _('not available')),
		('1', _('small')),
		('2', _('high')),
	)
	av = forms.ChoiceField(choices=avs)
	class Meta:
		model = Product
		fields = ('name', 'av','unit',)
		labels = {
            'name': _('name'),
			'av': _('av'),
			'unit' : _('unit')
        }

class DishProductForm(forms.ModelForm):
	product = forms.ModelChoiceField(queryset=Product.objects, empty_label=None)
	class Meta:
		model = DishProduct
		fields = ('count', 'product','dish')
		labels = {
            'product': _('product'),
        }
class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('category_name','order')
		labels = {
            'category_name': _('name'),
            'order':_('sequence')
        }
		
class CurrencyForm(forms.ModelForm):
	class Meta:
		model = Currency
		fields = ('name', 'ab', 'value')
		labels = {
            'name': _('name'),
            'ab' : _('ab'),
            'value' : _('value')

        }	
class DishPriceForm(forms.ModelForm):
	class Meta:
		model = DishPrice
		fields = ('price',)
		labels = {     
            'price' : _('price')
        }	
	
class CategoryTransForm(forms.ModelForm):
	class Meta:
		model = CategoryTranslation
		fields = ('name',)
		labels = {
            'name': _('translation'),
        }
class LanguageForm(forms.ModelForm):
	STATES = (
		('en-US', 'en-US'),
		('en-GB', 'en-GB'),
		('de-DE', 'de-DE'),
		('fr-FR', 'fr-FR'),
		('pl-PL', 'pl-PL'),
	)
	ab = forms.ChoiceField(choices=STATES)
	class Meta:
		model = ProductTranslation
		fields = ('name','ab')
		labels = {
            'name': _('name'),
            'ab': _('ab'),
        }


	
class ProductTransForm(forms.ModelForm):
	class Meta:
		model = ProductTranslation
		fields = ('name',)
		labels = {
            'name': _('translation'),
        }
class DishTransForm(forms.ModelForm):
	description = forms.CharField( widget=forms.Textarea )
	class Meta:
		model = DishTranslation
		fields = ('name', 'description',)
		labels = {
            'name': _('translation'),
            'description': _('description'),
        }
class RestaurantDetailForm(forms.ModelForm):
	default_lang = forms.ModelChoiceField(queryset=Language.objects, empty_label=None)
	default_currency = forms.ModelChoiceField(queryset=Currency.objects, empty_label=None)
	STATES = (
		('0', _('active')),
		('1', _('notactive')),
	)
	#CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
	autoorder = forms.ChoiceField(choices=STATES)
	class Meta:
		from .models import RestaurantDetail
		model = RestaurantDetail
		fields = ('name', 'default_currency', 'default_lang', 'takeaway','autoorder')
		labels = {
            'name': _('name'),
            'default_currency': _('default_currency'),
            'default_lang': _('default_lang'), 
            'takeaway': _('takeaway'),
            'autoorder': _('autoorder')
        }


class DishForm(forms.ModelForm):
	STATES = (
		('0', _('available')),
		('1', _('not available')),
	)
	#CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
	av = forms.ChoiceField(choices=STATES)
	category = forms.ModelChoiceField(queryset=Category.objects, empty_label=None)
	description = forms.CharField( widget=forms.Textarea )
	class Meta:
		model = Dish
		fields = ('name', 'category', 'description', 'av','price', 'tax')
		labels = {
            'name': _('name'),
			'category': _('category'),
			'av': _('av'),
			'price': _('price')
        }
	def __init__(self, *args, **kwargs):
		super(DishForm, self).__init__(*args, **kwargs)
		self.fields['category'].label_from_instance = lambda obj: "%s" % obj.category_name
		
class EmployeeForm(forms.ModelForm):
	POSITIONS = (
		('0', _('waiter')),
		('1', _('cook')),
		('2', _('provaider')),
		('3', _('supplier'))
	)
	ACTIVES = (
		('0', _('active')),
		('1', _('notactive')),
	)
	#CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
	position = forms.ChoiceField(choices=POSITIONS)
	active = forms.ChoiceField(choices=ACTIVES)
	class Meta:
		model = Employee
		fields = ('id','name', 'surname', 'position','phonenumber','login', 'password', 'active')
		labels = {
            'name': _('fname'),
			'surname':_('surname'),
			'position': _('position'),
			'phonenumber': _('phonenumber'),
			'login': _('login'),
			'password': _('password'),
			'active': _('active'),
        }
		