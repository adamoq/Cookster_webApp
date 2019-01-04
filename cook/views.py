#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dish, Product, Employee, Category, WaiterTask, RestaurantDetail, LoginLog, Notification
from .models import DishTranslation, Language,ProductTranslation, CategoryTranslation, Currency, DishPrice
from .models import WaiterOrderDetails, WaiterOrder, CookTask, CookOrder
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import ProductForm, CategoryForm, DishForm, EmployeeForm, ProductTransForm, CategoryTransForm, DishTransForm, LanguageForm, CurrencyForm
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from cook.tables import ProductTable, EmployeeTable, CategoryTable, DishTable,  ProductTransTable, CategoryTransTable, DishTransTable
from django_tables2   import RequestConfig
from django.utils.translation import gettext as _


def main(request):
	if request.user.is_authenticated():
		redirect(products)
	else:
		return render(request, 'index.html')

@login_required
@csrf_exempt
def products(request):
		if request.method == 'PUT':
			form = ProductForm(request.POST)
			if not form.is_valid():
				showError(request,_('Dane produktu są niepoprawane.'))
			else:
				form.save()
				id = form.cleaned_data['name']
				state = form.cleaned_data['av']

				product = Product.objects.all().filter(name = id)
				if product is not None:
					dishes = Dish.objects.all().filter(products__in = [product])
					if dishes[0]:
						if state == "0":
							dishes.update(av='1')
						elif state == "1" or state == "2":
							dishes.update(av='0')
							for i in range(len(dishes)):
								for product in dishes[i].products.all():
									if product.av == '0':
										dishes[i].av='1'
										break
		elif request.method == 'POST':
			form = ProductForm(request.POST)
			if not form.is_valid():
				showError(request,_('Dane produktu są niepoprawane.'))
			else:
				form.save()
		template = loader.get_template('products.html')
		table = ProductTable(Product.objects.all())
		RequestConfig(request).configure(table)
		forms = {}
		for product in Product.objects.all():
			forms[product.id]=ProductForm(instance=product)
		context = {
			'productsList': table,
			'form':ProductForm(),
			'formText': _("Dodaj produkt"),
			'update_forms': forms,
			'data_target': 'api/products/',
			'add_text': _('Add product'),
			'edit_text': _('Edit product\'s description'),
			'charturl': '/products/raport/'
		}
		return HttpResponse(template.render(context, request))
		#return render(request, 'products.html', context)

@login_required
@csrf_exempt
def administration(request):
	employesList = Employee.objects.all()
	template = loader.get_template('administration.html')
	context = {
		'employesList': employesList,
	}
	return HttpResponse(template.render(context, request))

@login_required
@csrf_exempt
def employers(request):
	template = loader.get_template('employers.html')
	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		form.restaurant = RestaurantDetail.objects.all().first()
		if not form.is_valid():
			showError(request,_('Dane produktu są niepoprawane.'))
		else:
			form.save()
	forms = {}
	for employee in Employee.objects.all():
		forms[employee.id]=EmployeeForm(instance=employee)

	table = EmployeeTable(Employee.objects.all())
	RequestConfig(request).configure(table)
	context = {
		'employesList': table,
		'update_forms': forms,
		'form': EmployeeForm(),
		'formText': _('Dodaj pracownika'),
		'data_target': 'api/resemployees/',
		'add_text': _('Add worker'),
		'edit_text': _('Edit worker\'s description')
	}
	return HttpResponse(template.render(context, request))
@login_required
@csrf_exempt
def menu(request):

	if request.method == 'PUT':
		try:
			categoryform = CategoryForm(request.POST)
			if categoryform.is_valid():
				categoryform.save()

		except (IntegrityError,Error):
			pass


	elif request.method == 'PUT':
		showError(request,_('Dane są niepoprawane.'))
	elif request.method == 'POST':
		categoryform = CategoryForm(request.POST)
		if not categoryform.is_valid():
			showError(request,_('Dane kategorii są niepoprawane.'))
		else:
			categoryform.save()
			#Category.objects.create(category_name=categoryform.cleaned_data['category_name'],order=categoryform.cleaned_data['order'])
	template = loader.get_template('menu.html')

	map = {}
	forms = {}
	currency = RestaurantDetail.objects.all().first().default_currency.name
	for category in Category.objects.all().order_by('order'):
		list = []
		list.append(Category.objects.get(pk = category.id))
		table = DishTable(Dish.objects.filter(category = category), currency)
		#table.columns.price = "zł"
		map[CategoryTable(list, currency)] = table
		forms["c"+str(category.id)]=CategoryForm(instance=category)


	context = {
		'categoryList': map,#Category.objects.all(),
		'form':CategoryForm(),
		'update_forms':forms,
		'data_target' : 'api/category/',
		'edit_text' : "Edytuj Kategorię",
		'add_text' :  _('Dodaj kategorię'),
		'formText': _('Dodaj kategorię'),#Category.objects.all(),,
		'add_text2' :  _('Dodaj danie'),
		'data_target2' :  "/dish",
		'charturl' : "/menu/raport",

	}
	return HttpResponse(template.render(context, request))

@login_required
@csrf_exempt
def currencies(request):

	if request.method == 'POST':
		categoryform = CurrencyForm(request.POST)
		if not categoryform.is_valid():
			showError(request,_('Dane kategorii są niepoprawane.'))
		else:
			cur = Currency.objects.create(name=categoryform.cleaned_data['name'],value=categoryform.cleaned_data['value'],ab=categoryform.cleaned_data['ab'])
			cur.save()
			value = cur.value
			for object in Dish.objects.all():
				trans = DishPrice.objects.create(dish_id = object.id, currency_id = cur.id, price =  object.price/value)
	template = loader.get_template('currencies.html')

	map = {}
	forms = {}
	currency = RestaurantDetail.objects.all().first().default_currency.name
	currency = Currency.objects.get(pk = request.GET.get('d')).name
	for category in Category.objects.all().order_by('order'):
		list = []
		list.append(Category.objects.get(pk = category.id))

		#table.columns.price = "zł"
		map[CategoryTable(list, currency)] = DishTable(Dish.objects.filter(category = category), currency)
		forms["c"+str(category.id)]=CategoryForm(instance=category)


	context = {
		'categoryList': map,#Category.objects.all(),
		'form':CurrencyForm(),
		'update_forms':forms,
		'data_target' : 'api/category/',
		'edit_text' : "Edytuj Kategorię",
		'add_text' :  _('Dodaj kategorię'),
		'formText': _('Dodaj kategorię'),#Category.objects.all(),

		'form2':DishForm(),
		'add_text2' :  _('Dodaj danie')
	}
	return HttpResponse(template.render(context, request))




@login_required
@csrf_exempt
def trans(request):

	if request.method == 'PUT':
		try:
			dishform = DishTranslation(request.POST)
			if dishform.is_valid():
				dishform.save()

		except (IntegrityError,Error):
			pass


	elif request.method == 'PUT':
		showError(request,_('Dane są niepoprawane.'))
	elif request.method == 'POST':
		langform = LanguageForm(request.POST)
		if not langform.is_valid():
			showError(request,_('Dane kategorii są niepoprawane.'))
		else:
			try:
				language = Language.objects.create(name=langform.cleaned_data['name'])
				language.save()
				for object in Dish.objects.all().values_list('id', flat=True):
					trans = DishTranslation.objects.create(dish_id = object, lang_id = language.id)
					trans.save()
				for object in Product.objects.all().values_list('id', flat=True):
					trans = ProductTranslation.objects.create(product_id = object, lang_id = language.id)
					trans.save()
				for object in Category.objects.all().values_list('id', flat=True):
					trans = CategoryTranslation.objects.create(category_id = object, lang_id = language.id)
					trans.save()
			except (IntegrityError,Error):
				showError(request,_('Dane kategorii są niepoprawane.'))

	template = loader.get_template('translations.html')

	map = {}
	forms = {}
	forms2 = {}
	currency = RestaurantDetail.objects.all().first().default_currency.name
	for lang in Language.objects.all():
		map[DishTransTable(DishTranslation.objects.filter(lang_id = lang.id).order_by('name'))] = ProductTransTable(ProductTranslation.objects.filter(lang_id = lang.id).order_by('name'))
		for object in DishTranslation.objects.filter(lang_id = lang.id).order_by('name'):
			forms["d"+str(object.id)]=DishTransForm(instance=object)
		for object in ProductTranslation.objects.filter(lang_id = lang.id).order_by('name'):
			forms2["p"+str(object.id)]=ProductTransForm(instance=object)


	context = {
		'categoryList': map,#Category.objects.all(),
		'form':LanguageForm(),
		'update_forms':forms,
		'data_target' : 'api/dishtranslation/',
		'edit_text' : "Edytuj Kategorię",
		'update_forms2':forms2,
		'data_target2' : 'api/producttranslation/',
		'add_text' :  _('Dodaj kategorię'),
		'formText': _('Dodaj kategorię'),#Category.objects.all(),

		'form2':DishForm(),
		'add_text2' :  _('Dodaj danie')
	}
	return HttpResponse(template.render(context, request))







@login_required
@csrf_exempt
def category(request):
	template = loader.get_template('category.html')
	category = Category.objects.get(pk = request.GET.get('c'))
	dishes = Dish.objects.filter(category = category)
	table = DishTable(dishes)
	RequestConfig(request).configure(table)
	if request.method == 'POST':
		dishForm = DishForm(request.POST)
		dishForm.save()
		context = {
			'categoryName': category.category_name,
			'dishesList' : table,
			'form':DishForm(),
			'formText': _('Dodaj danie')
		}
	if request.method == 'GET':
		context = {
			'categoryName': category.category_name,
			'dishesList' : table,
			'form':DishForm(),
			'formText': _('Dodaj danie')
		}
	else:
		showError(request,_('Dane dania są niepoprawane.'))
	return HttpResponse(template.render(context, request))
@login_required
@csrf_exempt
def dish(request):
	template = loader.get_template('dish.html')
	dish = None
	if request.GET.get('d'): 
		dish = Dish.objects.get(pk = request.GET.get('d'))
	if request.method == 'POST':
		if dish: 
			dishForm = DishForm(request.POST, instance = dish)
		else: dishForm = DishForm(request.POST)
		if not dishForm.is_valid():
			showError(request,_('Dane kategorii są niepoprawane.'))
		else:
			dishForm.save()
			return redirect("/menu")
		context = {
			'dish':dishForm,
			'dishId':request.POST.get('id'),
			'add_text2' :  _('Dodaj danie'),
		}
		return HttpResponse(template.render(context, request))


	context = {
		'dish':DishForm(instance = dish),
	}

	return HttpResponse(template.render(context, request))


@login_required
@csrf_exempt
def orders(request):
	return render(request, 'orders.html')
@login_required
@csrf_exempt
def orders_waiter(request):

	template = loader.get_template('orders-waiter.html')
	waitertasks = WaiterTask.objects.all()
	tasks = []
	dishesList = ""
	currency = RestaurantDetail.objects.all().first().default_currency.ab
	order_currency = currency
	for task in waitertasks:
		status = "0"
		order_currency = currency
		if task.currency.ab is not order_currency:
			order_currency = task.currency.ab
		for order in WaiterOrderDetails.objects.all().filter(task = task):

			if (status is "0" or "1") and (order.state is "1" or order.state is "2") : status = order.state
			for orderdetail in WaiterOrder.objects.all().filter(task = order):
				
				dishesList += str(orderdetail.count) + " x " + orderdetail.dish.name + " - " + str(orderdetail.price_default) + currency +"\n"

		orderMap = {}
		orderMap["id"] = task.id
		orderMap["waiter"] = task.waiter.name + " " + task.waiter.surname
		orderMap["cook"] = task.cook.name +" "+ task.cook.surname
		orderMap["price_default"] = str(task.price_default) +" "+ currency
		orderMap["created_at"] = task.created_at
		orderMap["dishes"] = dishesList
		orderMap["state"] = status
		orderMap["table"] = task.table
		orderMap["updated_at"] = "task.created_at"
		orderMap["comment"] = task.comment
		if order_currency != currency:
			orderMap["price"] = str(task.price) + " " +order_currency
		tasks.append(orderMap)
	context = {
		'tasks': tasks,
		'charturl' : "/orders-waiter/raport",
	}
	return HttpResponse(template.render(context, request))
@login_required
@csrf_exempt
def orders_cook(request):

	template = loader.get_template('orders-waiter.html')
	waitertasks = CookTask.objects.all()
	tasks = []
	dishesList = ""
	for task in waitertasks:
		for order in CookOrder.objects.all().filter(task = task):				
			dishesList += str(order.count) + " x " + order.product.name + "\n"
			orderMap = {}
			orderMap["id"] = task.id
			orderMap["provider"] = task.provider.name + " " + task.provider.surname
			orderMap["cook"] = task.cook.name +" "+ task.cook.surname
			orderMap["created_at"] = task.created_at
			orderMap["products"] = dishesList
			orderMap["state"] = task.state
			orderMap["updated_at"] = "task.created_at"
			orderMap["comment"] = task.comment
		tasks.append(orderMap )
	context = {
		'tasks': tasks,
		'charturl' : "/orders-cook/raport",
	}
	return HttpResponse(template.render(context, request))



@csrf_exempt
def login_user(request):
	logout(request)
	username = password = ''
	if not request.user.is_authenticated:
		return HttpResponseRedirect('/products/')
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None and user.is_active:
			login(request, user)
			return HttpResponseRedirect('/products/')
	return render_to_response('login.html')
def showError(request, errorText):
	template = loader.get_template('error.html')
	HttpResponse(template.render({'errorText':errorText}, request))

from django.db import transaction
def login_mobile(request):
	if request.method == 'GET':
		login = request.GET.get('login')
		password = request.GET.get('password')
		if login and password :
			user = Employee.objects.all().filter(login = login)
			if not user.count():
				return HttpResponse("False")
			else:
				if user[0].password == password:
					user.update(status = "2")
					LoginLog.objects.create(employee=user.first(),status="2")
				
					return HttpResponse(serializers.serialize("json", [user[0], RestaurantDetail.objects.first()]))
	return HttpResponse("False")


def login_mobile_status(request):
	if request.method == 'GET':
		login = request.GET.get('login')
		status = request.GET.get('status')
		if login and status :
			employee = Employee.objects.all().filter(login = login)
			if employee is not None:
				employee.update(status = status)
				LoginLog.objects.create(employee=employee.first(),status=status)
				return HttpResponse("True")
	return HttpResponse("False")

def checknotif(request):
	if request.method == 'GET':
		userid = request.GET.get('id')

		if userid:
			employee = Employee.objects.all().filter(pk = userid)
			if employee is not None:
				notifications = Notification.objects.all().filter( employee = employee, active='0')
				for notification in notifications:
					notification.active = '1'
					notification.save()
				return HttpResponse(serializers.serialize("json", notifications))
	return HttpResponse("False")

def resetpassword(request):
	if request.method == 'GET':
		login = request.GET.get('login')
		password = request.GET.get('passwordOld')
		if login and password:
			user = Employee.objects.all().filter(login = login)
			if user is not None and user[0].password == password:
				user.update(password='reset')
				return HttpResponseRedirect('/employers/')

def changepassword(request):
	if request.method == 'GET':
		login = request.GET.get('login')
		password = request.GET.get('passwordOld')
		npassword = request.GET.get('passwordNew')
		if login and password and npassword:
			user = Employee.objects.all().filter(login = login)
			if user is not None and user[0].password == password:
					user.update(password=npassword)
					return HttpResponse(serializers.serialize("json", user))
	return HttpResponse("False")

def changephone(request):
	if request.method == 'GET':
		login = request.GET.get('login')
		password = request.GET.get('password')
		phonenumber = request.GET.get('phonenumber')
		if login and password and phonenumber:
			user = Employee.objects.all().filter(login = login)
			if user is not None and user[0].password == password:
				user.update(phonenumber=phonenumber)
				return HttpResponse(serializers.serialize("json", user))
	return HttpResponse("False")

def changeproduct(request):
	if request.method == 'GET':
		id = request.GET.get('id')
		state = request.GET.get('state')
		if id and state:
			product = Product.objects.all().filter(pk = id)
			product.update(av=state)
			if product is not None:
				dishes = Dish.objects.all().filter(products = product)
				if dishes[0]:
					if state == "0":
						dishes.update(av='0')
					elif state == "1" or state == "2":
						dishes.update(av='1')
						for i in range(len(dishes)):
							for product in dishes[i].products.all():
								if product.av == '0':
									dishes[i].av='0'
									break

					return HttpResponse(serializers.serialize("json", dishes))
	return HttpResponse("False")



def product_chart(request):
	template = loader.get_template('charts/menu-chart.html')
	context = {
			'chart_type':'bar',
			'chart_type2':'doughnut',
			'url_json':'dish_chart_json',
			'url_json1':'category_chart_json1',
			'url_json2':'category_chart_json',			
			'url_json3':'category_chart_json2',
			'charttitle' : '"Ilość zamówionych dań"',
			'charttitle1' : '"Ilość zamówionych dań"',
			'charttitle2' : '"Ilość zamówionych dań z podziałem na kategorie"',
			'charttitle3' : '"Wartość zamówień z podziałem na kategorie (w '+RestaurantDetail.objects.all().first().default_currency.name+')"'
		}
	return HttpResponse(template.render(context, request))

def cookorders_chart(request):
	template = loader.get_template('charts/orders-chart.html')
	context = {
			'chart_type':'bar',
			'chart_type2':'doughnut',
			'url_json':'cookorders_chart_json',
			'url_json1':'cookorders_chart_json2',
			'url_json2':'cookorders_chart_json3',			
			'url_json3':'cookorders_chart_json4',
			'charttitle' : '"Ilość złożonych zamówień każdego dnia"',
			'charttitle1' : '"Ilość złożonych zamówień przez kucharzy"',
			'charttitle2' : '"Ilość zamówień przydzielonych do dostawców"',
			'charttitle3' : '"Ilość złożonych zamówień przez kucharzy"',
			'backgroundColors':"['rgba(255, 99, 132, 1)',"+
			"'rgba(54, 162, 235, 1)',"+
			"'rgba(255, 206, 86, 1)',"+
			"'rgba(75, 192, 192, 1)',"+
			"'rgba(153, 102, 255, 1)',"+
			"'rgba(255, 159, 64, 1)']"
			}
	return HttpResponse(template.render(context, request))

def waiterorders_chart(request):
	template = loader.get_template('charts/orders-chart.html')
	context = {
			'chart_type':'bar',
			'chart_type2':'doughnut',
			'url_json':'waiterorders_chart_json',
			'url_json1':'waiterorders_chart_json2',
			'url_json2':'waiterorders_chart_json3',			
			'url_json3':'waiterorders_chart_json4',
			'charttitle' : '"Ilość złożonych zamówień każdego dnia"',
			'charttitle1' : '"Ilość złożonych zamówień przez danego kelnera"',
			'charttitle2' : '"Ilość zamówień przydzielonych do danego kucharza"',
			'charttitle3' : '"Ilość złożonych zamówień w danym dniu"',
			'backgroundColors':"['rgba(255, 99, 132, 1)',"+
			"'rgba(54, 162, 235, 1)',"+
			"'rgba(255, 206, 86, 1)',"+
			"'rgba(75, 192, 192, 1)',"+
			"'rgba(153, 102, 255, 1)',"+
			"'rgba(255, 159, 64, 1)']"
			}
	return HttpResponse(template.render(context, request))
def products_chart(request):
	template = loader.get_template('charts/products-chart.html')
	context = {
			'chart_type':'bar',
			'chart_type2':'line',
			'url_json':'products_chart_json',
			'url_json1':'products_chart_json2',
			'charttitle' : '"Ilość złożonych zamówień każdego dnia"',
			'charttitle1' : '"Ilość złożonych zamówień przez danego kelnera"',

			}
	return HttpResponse(template.render(context, request))
def employees_chart(request):
	template = loader.get_template('charts/twocharts.html')
	context = {
			'url_json':'dish_chart_json',
			'chart_type':'bar',
			'url_json1':'category_chart_json1',
			'chart_type2':'bar',
			'charttitle' : 'Ilość złożonych zamówień każdego dnia',
			'charttitle1' : 'Ilość złożonych zamówień przez kucharzy',
			'charttitle2' : 'Ilość zamówień przydzielonych do dostawców',
			'charttitle3' : 'Ilość złożonych zamówień każdego dnia',
		}
	return HttpResponse(template.render(context, request))


















