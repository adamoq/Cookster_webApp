#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dish, Product, Employee, Category, WaiterTask, RestaurantDetail, LoginLog, Notification
from .models import DishTranslation, Language,ProductTranslation, CategoryTranslation, Currency, DishPrice
from .models import WaiterOrderDetails, WaiterOrder, CookTask, CookOrder, DishProduct
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import ProductForm, CategoryForm, DishForm, EmployeeForm, ProductTransForm, CategoryTransForm, DishTransForm, LanguageForm, CurrencyForm, DishPriceForm, DishProductForm
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
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
	from cook.tables import ProductTable
	allProducts = Product.objects.all()
	if request.method == 'PUT':
		form = ProductForm(request.POST)
		if not form.is_valid():
			showError(request,_('data-invalid'))
		else:
			form.save()
			id = form.cleaned_data['id']
			state = form.cleaned_data['av']

			product = allProducts.filter(pk = id)
			#product.update(av=state)
			if product is not None:
				dishes = Dish.objects.all().filter(products = product)
				if dishes[0]:
					if state == 'small':
						dishes.update(av='1')
					elif state == '1' or state == '2':
						dishes.update(av='0')
						for i in range(len(dishes)):
							for product in dishes[i].products.all():
								if product.av == '0':
									dishes[i].av='1'
									dishes[i].save()
									break
	elif request.method == 'POST':
		form = ProductForm(request.POST)
		if not form.is_valid():
			showError(request,_('data-invalid'))
		else:
			form.save()
			name = form.cleaned_data['name']
			product = allProducts.filter(name = name).first()
			deflang = RestaurantDetail.objects.all().first().default_lang.id
			for lang in Language.objects.all():
				if deflang != lang.id:
					ProductTranslation.objects.create(product_id = product.id, lang_id = lang.id)

	template = loader.get_template('products.html')

	table = ProductTable(allProducts)
	RequestConfig(request,paginate={'per_page': 15}).configure(table)
	forms = {}
	if request.GET.get('page'): offset = int(request.GET.get('page'))
	else: offset = 1
	allProducts= allProducts[15 * (offset-1):15 * offset]
	producttranslations = ProductTranslation.objects.filter(product__in = allProducts).values('id', 'lang__name')
	#langs = Language.objects.values_list('pub_date')
	for product in allProducts:
		map = {}
		translits = []
		for object in ProductTranslation.objects.filter(product = product):
			transmap = {}
			transmap['form'] = ProductTransForm(instance=object)
			for trans in producttranslations :
				if trans['id'] == object.id:
					transmap['lang'] = trans['lang__name']
					break
			transmap['id'] = object.id
			transmap['data_target'] = 'api/producttranslation/'
			translits.append(transmap)
		map['trans'] = translits
		map['productForm'] = ProductForm(instance=product)
		forms[product.id]=map
	context = {
		'productsList': table,
		'form':ProductForm(),
		'formText': _("add-product-form"),
		'update_forms': forms,
		'data_target': 'api/products/',
		'add_text': _("add-product"),
		'edit_text': _("edit-product"),
		'charturl': '/products/raport/'
	}
	return HttpResponse(template.render(context, request))
	#return render(request, 'products.html', context)

@login_required
@csrf_exempt
def administration(request):
	from .forms import RestaurantDetailForm
	template = loader.get_template('administration.html')
	langforms = []
	restaurant = RestaurantDetail.objects.all().first()
	for lang in Language.objects.all():
		langmap = {}
		langmap['id'] = lang.id
		langmap['form'] = LanguageForm(instance = lang)
		if restaurant.default_lang.id == lang.id:
			langmap['isNotDefault'] = False
			langforms.insert(0, langmap)
		else :
			langmap['isNotDefault'] = True
			langforms.append(langmap)
		#langforms.append(langmap)
	currencyforms = []
	for lang in Currency.objects.all():

		langmap = {}
		langmap['id'] = lang.id
		langmap['name'] = lang.name
		langmap['form'] = CurrencyForm(instance = lang)
		if restaurant.default_currency.id == lang.id:
			langmap['isNotDefault'] = False
			currencyforms.insert(0, langmap)
		else :
			langmap['isNotDefault'] = True
			currencyforms.append(langmap)


	context = {
		'employesList': Employee.objects.all(),
		'productList': Product.objects.all(),
		'dishList': Dish.objects.all(),
		'data_target': 'api/lang/',
		'langforms' : langforms,
		'langform'  : LanguageForm(),
		'currencyforms' : currencyforms,
		'currencyform'  : CurrencyForm(),
		'data_target2': 'api/currency/',
		'restaurantform' : {'form':RestaurantDetailForm(instance = restaurant), 'id' : restaurant.id},
		'data_target3' : 'api/resdet/'
	}
	return HttpResponse(template.render(context, request))

@login_required
@csrf_exempt
def employers(request):
	from cook.tables import EmployeeTable
	template = loader.get_template('employers.html')
	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		form.restaurant = RestaurantDetail.objects.all().first()
		if not form.is_valid():
			showError(request,_("data-invalid"))
		else:
			form.save()
	forms = {}
	for employee in Employee.objects.all():
		transmap = {}
		transmap['productForm'] = EmployeeForm(instance=employee)
		forms[employee.id]=transmap

	table = EmployeeTable(Employee.objects.all())
	RequestConfig(request).configure(table)
	context = {
		'employesList': table,
		'update_forms': forms,
		'form': EmployeeForm(),
		'formText': _("add-employee-form"),
		'data_target': 'api/resemployees/',
		'add_text':  _("add-employee"),
		'edit_text':  _("edit-employee")
	}
	return HttpResponse(template.render(context, request))
@login_required
@csrf_exempt
def menu(request):
	from cook.tables import CategoryTable, DishTable

	if request.method == 'PUT':
		try:
			categoryform = CategoryForm(request.POST)
			if categoryform.is_valid():
				categoryform.save()

		except (IntegrityError,Error):
			pass


	elif request.method == 'PUT':
		showError(request, _("data-invalid"))
	elif request.method == 'POST':
		categoryform = CategoryForm(request.POST)
		if not categoryform.is_valid():
			showError(request,_("data-invalid"))
		else:
			categoryform.save()
			cat = Category.objects.filter(category_name = categoryform.cleaned_data['category_name']).first()
			default_lang = RestaurantDetail.objects.all().first().default_lang.id
			for object in Language.objects.all():
				if default_lang != object.id:
					CategoryTranslation.objects.create(category_id = cat.id, lang_id = object.id)
			#Category.objects.create(category_name=categoryform.cleaned_data['category_name'],order=categoryform.cleaned_data['order'])
	template = loader.get_template('menu.html')

	map = {}
	forms = {}
	currency = RestaurantDetail.objects.all().first().default_currency.ab
	categories = CategoryTranslation.objects.all()
	cattrans = categories.values('id','lang__name')



	dishes = Dish.objects.all()
	for category in Category.objects.all().order_by('order'):
		list = []
		list.append(category)
		table = DishTable(dishes.filter(category = category), currency)
		#table.columns.price = "zł"
		map[CategoryTable(list, currency)] = table
		#forms["c"+str(category.id)]=CategoryForm(instance=category)

		formmap = {}
		translits = []
		for object in categories.filter(category_id = category.id):
			transmap = {}
			transmap['form'] = CategoryTransForm(instance=object)
			for categorytrans in cattrans:
				if categorytrans['id'] == object.id:
					transmap['lang'] = categorytrans['lang__name']
					break
			transmap['id'] = object.id
			transmap['data_target'] = 'api/categorytranslation/'
			translits.append(transmap)
		formmap['trans'] = translits
		formmap['productForm'] = CategoryForm(instance=category)
		forms[category.id]=formmap


	context = {
		'categoryList': map,#Category.objects.all(),
		'form':CategoryForm(),
		'update_forms':forms,
		'data_target' : 'api/category/',
		'edit_text' : _("edit-category"),
		'add_text' :  _("add-category"),
		'formText': _("add-category-form"),#Category.objects.all(),,
		'add_text2' :  _("add-dish"),
		'charturl' : "/menu/raport",

	}
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
		else:
			dishForm = DishForm(request.POST)
		if dishForm.is_valid():
			dishForm.save()
			if dish is None:
				dish = Dish.objects.filter(name = dishForm.cleaned_data['name']).first()
				default_lang = RestaurantDetail.objects.all().first().default_lang.id
				for object in Language.objects.all():
					if default_lang != object.id:
						DishTranslation.objects.create(dish_id = dish.id, lang_id = object.id)
			else :
				return redirect("/menu")
		forms = []
		for object in DishPrice.objects.filter(dish = dish):
			transmap = {}
			transmap['form'] = DishPriceForm(instance=object)
			transmap['lang'] = object.currency.name
			transmap['id'] = object.id
			transmap['data_target'] = 'api/dishprice/'
			forms.append(transmap)
		for object in DishTranslation.objects.filter(dish = dish):
			transmap = {}
			transmap['form'] = DishTransForm(instance=object)
			transmap['lang'] = _('language')+' '+object.lang.name
			transmap['id'] = object.id
			transmap['data_target'] = 'api/dishtranslation/'
			forms.append(transmap)

		dishproductforms = []
		for object in DishProduct.objects.filter(dish = dish):
			transmap = {}
			transmap['form'] = DishProductForm(instance=object)
			transmap['id'] = object.id
			dishproductforms.append(transmap)





		context = {
			'dish':dishForm,
			'dishId':request.POST.get('id'),
			'add_text2' : _("add-dish"),
			'transforms' : forms,
			'dishform': DishProductForm(initial={"dish":dish}),
			'dishforms': dishproductforms,
			'data_target':'api/dishproducts/'
		}
		return HttpResponse(template.render(context, request))

	forms = []
	for object in DishPrice.objects.filter(dish = dish):
		transmap = {}
		transmap['form'] = DishPriceForm(instance=object)
		transmap['lang'] = object.currency.name
		transmap['id'] = object.id
		transmap['data_target'] = 'api/dishprice/'
		forms.append(transmap)
	for object in DishTranslation.objects.filter(dish = dish):
		transmap = {}
		transmap['form'] = DishTransForm(instance=object)
		transmap['lang'] = _('language')+' '+object.lang.name
		transmap['id'] = object.id
		transmap['data_target'] = 'api/dishtranslation/'
		forms.append(transmap)

	dishproductforms = []
	for object in DishProduct.objects.filter(dish = dish):
		transmap = {}
		transmap['form'] = DishProductForm(instance=object)
		transmap['id'] = object.id
		dishproductforms.append(transmap)


	context = {
		'dish':DishForm(instance = dish),
		'transforms' : forms,
		'dishform': DishProductForm(initial={"dish":dish}),
		'dishforms': dishproductforms,
		'data_target':'api/dishproducts/'
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
		dishesList = ""
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

					return HttpResponse(serializers.serialize("json", [user[0], RestaurantDetail.objects.all()[0]]))
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

def changeimg(request):
	import json
	if request.method == 'GET' and request.is_ajax():
		login = request.GET.get('login')
		json_data = json.loads(request.body)
		image = json_data['image']
		if login and image:
			user = Employee.objects.all().filter(login = login)
			if user is not None:
				user.update(avatar=image)
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
						dishes.update(av='1')
					elif state == "1" or state == "2":
						dishes.update(av='0')
						for i in range(len(dishes)):
							for product in dishes[i].products.all():
								if product.av == '0':
									dishes[i].av='1'
									dishes[i].save()
									break

					return HttpResponse(serializers.serialize("json", dishes))
	return HttpResponse("False")



def menu_chart(request):
	template = loader.get_template('charts/menu-chart.html')
	context = {
			'chart_type':'bar',
			'chart_type2':'doughnut',
			'url_json':'dish_chart_json',
			'url_json1':'category_chart_json1',
			'url_json2':'category_chart_json',
			'url_json3':'category_chart_json2',
			'charttitle' : '"'+_("product-chart-1")+'"',#'"Ilość zamówionych dań"',
			'charttitle1' :'"'+ _("product-chart-2")+'"',#'"Ilość zamówionych dań"',
			'charttitle2' : '"'+_("product-chart-3")+'"',#'"Ilość zamówionych dań z podziałem na kategorie"',
			'charttitle3' :'"'+ _("product-chart-4")+RestaurantDetail.objects.all().first().default_currency.name+'"',#'"Wartość zamówień z podziałem na kategorie (w '+RestaurantDetail.objects.all().first().default_currency.name+')"'
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
			'charttitle' : '"'+_("cookorders-chart"+'"'),#''"Ilość złożonych zamówień każdego dnia"',
			'charttitle1' : '"'+ _("cookorders-chart-1"+'"'),#'"Ilość złożonych zamówień przez kucharzy"',
			'charttitle2' : '"'+_("cookorders-chart-2")+'"',#'"Ilość zamówień przydzielonych do dostawców"',
			'charttitle3' : '"'+ _("cookorders-chart-3")+'"',#'"Ilość złożonych zamówień przez kucharzy"',
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
			'charttitle' : '"'+ _("waiterorders-chart")+'"',#'"Ilość złożonych zamówień każdego dnia"',
			'charttitle1' : '"'+ _("waiterorders-chart-1")+'"',#'"Ilość złożonych zamówień przez danego kelnera"',
			'charttitle2' : '"'+ _("waiterorders-chart-2")+'"',#'"Ilość zamówień przydzielonych do danego kucharza"',
			'charttitle3' : '"'+_("waiterorders-chart-3")+'"',#'"Ilość złożonych zamówień w danym dniu"',
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
			'prodId':request.GET.get('d'),
			'chart_type2':'line',
			'url_json':'products_chart_json',
			'url_json1':'products_chart_json2',
			'charttitle' : '"'+ _("products-chart")+'"',#'"Ilość złożonych zamówień każdego dnia"',
			'charttitle1' : '"'+ _("products-chart-1")+'"',#'"Ilość złożonych zamówień przez danego kelnera"',

			}
	return HttpResponse(template.render(context, request))
def employers_chart(request):
	template = loader.get_template('charts/employers-chart.html')
	context = {
			'chart_type':'bar',
			'prodId':request.GET.get('p'),
			'url_json':'employers_chart_json',
			'charttitle' : '"'+ _("products-chart")+'"'#'Godziny aktywności',
		}
	return HttpResponse(template.render(context, request))


















