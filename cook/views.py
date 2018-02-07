from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dish, Product, Employee, Category, WaiterTask
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django import forms
from .forms import ProductForm, CategoryForm, DishForm, EmployeeForm
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
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
				showError(request,'Dane produktu są niepoprawane.')
			else:
				form.save()   
		elif request.method == 'POST':
			form = ProductForm(request.POST)
			if not form.is_valid():
				showError(request,'Dane produktu są niepoprawane.')
			else:
				form.save()       
		productsList = Product.objects.all()
		template = loader.get_template('products.html')
		form = ProductForm()
		context = {
			'productsList': productsList,
			'form':form,
			'formText': 'Dodaj produkt'
		}
		return HttpResponse(template.render(context, request))

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
	employesList = Employee.objects.all()
	template = loader.get_template('employers.html')
	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		if not form.is_valid():
			showError(request,'Dane produktu są niepoprawane.')
		else:
			form.save()   
	context = {
		'employesList': employesList,
		'form': EmployeeForm(),
		'formText': 'Dodaj pracownika'
	}
	return HttpResponse(template.render(context, request))
@login_required
@csrf_exempt	
def menu(request):
	if request.method == 'PUT':
		categoryform = CategoryForm(request.POST)
		if not categoryform.is_valid():
			showError(request,'Dane kategorii są niepoprawane.')
		else:
			categoryform.save()   
	elif request.method == 'POST':
		categoryform = CategoryForm(request.POST)
		if not categoryform.is_valid():
			showError(request,'Dane kategorii są niepoprawane.')
		else:
			Category.objects.create(name=categoryform.cleaned_data['name'])    
	categoryList = Category.objects.all()
	template = loader.get_template('menu.html')
	categoryform = CategoryForm()
	context = {
		'categoryList': categoryList,
		'form':categoryform,
		'formText': 'Dodaj kategorię'
	}
	return HttpResponse(template.render(context, request))
@login_required
@csrf_exempt		
def category(request):
	template = loader.get_template('category.html')
	category = Category.objects.get(pk = request.GET.get('c'))
	dishes = Dish.objects.filter(category = category)
	if request.method == 'POST':
		dishForm = DishForm(request.POST)
		dishForm.save()
		context = {
			'categoryName': category.name,
			'dishesList' : dishes,
			'form':DishForm(),
			'formText': 'Dodaj danie'
		}
	if request.method == 'GET':
		dishForm = DishForm()
		context = {
			'categoryName': category.name,
			'dishesList' : dishes,
			'form':dishForm,
			'formText': 'Dodaj danie'
		}
	else:
		showError(request,'Dane dania są niepoprawane.')
	return HttpResponse(template.render(context, request))
@login_required
@csrf_exempt	
def dish(request):
	template = loader.get_template('dish.html')
	
	if request.method == 'POST':
		dishForm = DishForm(request.POST, instance = Dish.objects.get(pk = request.POST.get('id')))
		if not dishForm.is_valid():
			showError(request,'Dane kategorii są niepoprawane.')
		else:
			dishForm.save() 
		context = {
			'dish':dishForm,
			'dishId':request.POST.get('id')
		}
	
	elif request.method == 'GET':
		dish = Dish.objects.get(pk = request.GET.get('d'))
		dishForm = DishForm( instance = dish)
		context = {
			'dish':dishForm,
			'dishId':dish.id
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
	tasks = WaiterTask.objects.all()
	context = {
		'tasks': tasks,
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
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/products/')
    return render_to_response('login.html')
def showError(request, errorText):
	template = loader.get_template('error.html')
	HttpResponse(template.render({'errorText':errorText}, request))
def login_mobile(request):
	if request.method == 'GET':
		login = request.GET.get('login')
		password = request.GET.get('password')
		if login and password :
			user = Employee.objects.all().filter(login = login)
			if user is not None and user[0].password == password: return HttpResponse(serializers.serialize("json", user))
	return HttpResponse("False")
def changepassword(request):
	if request.method == 'GET':
		login = request.GET.get('login')
		password = request.GET.get('passwordOld')
		npassword = request.GET.get('passwordNew')
		if login and password and npassword:
			user = Employee.objects.all().filter(login = login)
			if user is not None and user[0].password == password: 
				user[0].password = npassword
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
				user[0].phonenumber = phonenumber
				return HttpResponse(serializers.serialize("json", user))
	return HttpResponse("False")