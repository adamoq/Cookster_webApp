from django import forms
from .models import Product, Dish, Employee, Category
from django.utils.translation import gettext as _
class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('name', 'av',)
		labels = {
            'name': _('Nazwa'),
			'av': _('Dostępność')
        }

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('category_name','order')
		labels = {
            'category_name': _('Nazwa'),
        }

class DishForm(forms.ModelForm):
	class Meta:
		model = Dish
		fields = ('name', 'category', 'description', 'products','av','price', 'tax')
		labels = {
            'name': _('Nazwa'),
			'products': _('Produkty'),
			'category': _('Kategoria'),
			'av': _('Dostepność'),
			'price': _('price')
        }
	def __init__(self, *args, **kwargs):
		super(DishForm, self).__init__(*args, **kwargs)
		self.fields['products'].label_from_instance = lambda obj: "%s" % obj.name		
		self.fields['category'].label_from_instance = lambda obj: "%s" % obj.category_name
		
class EmployeeForm(forms.ModelForm):
	POSITIONS = (
		('0', _('waiter')),
		('1', _('cook')),
		('2', _('provaider')),
	)
	#CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
	position = forms.ChoiceField(choices=POSITIONS)
	class Meta:
		model = Employee
		fields = ('id','name', 'surname', 'position','phonenumber','login', 'password', 'active')
		labels = {
            'name': _('Imię'),
			'surname':_('Nazwisko'),
			'position': _('Stanowisko'),
			'phonenumber': _('Numer telefonu'),
			'login': _('Login'),
			'password': _('Hasło')
        }
		