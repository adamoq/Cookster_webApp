from django import forms
from .models import Product, Dish, Employee

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('name', 'av',)
		labels = {
            'name': 'Nazwa',
			'av': 'Dostępność'
        }

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('name',)
		labels = {
            'name': 'Nazwa',
        }

class DishForm(forms.ModelForm):
	class Meta:
		model = Dish
		fields = ('name', 'category', 'products','av')
		labels = {
            'name': 'Nazwa',
			'products': 'Produkty',
			'category': 'Kategoria',
			'av': 'Dostepność'
        }
	def __init__(self, *args, **kwargs):
		super(DishForm, self).__init__(*args, **kwargs)
		self.fields['products'].label_from_instance = lambda obj: "%s" % obj.name
		self.fields['category'].label_from_instance = lambda obj: "%s" % obj.name
		
class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ('name', 'surname', 'position','login', 'password')
		labels = {
            'name': 'Imię',
			'surname':'Nazwisko',
			'Stanowisko': 'Hasło',
			'login': 'Login',
			'password': 'Hasło'
        }
