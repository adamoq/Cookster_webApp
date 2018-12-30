from datetime import timedelta, date
import datetime

from cook.models import Product, Employee, Dish, Category, WaiterTask, CookTask, CookOrder, WaiterOrder, Currency, WaiterOrderDetails, DishTranslation
from cook.models import DishPrice, ProductTranslation, CategoryTranslation, Language, Notification
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from itertools import chain



class DishPriceResource(ModelResource):
	class Meta:
		queryset = DishPrice.objects.all()
		resource_name = 'dishprice'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']
class LanguageResource(ModelResource):
	class Meta:
		queryset = Language.objects.all()
		resource_name = 'lang'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']



class CategoryResource(ModelResource):
	class Meta:
		queryset = Category.objects.all().order_by("order")
		resource_name = 'category'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']

class ProductResource(ModelResource):
	class Meta:
		limit = 0
		queryset = Product.objects.all().order_by('name')
		resource_name = 'products'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']

class DishResource(ModelResource):
	category = fields.ForeignKey(CategoryResource, 'category',full=True)
	products = fields.ManyToManyField(ProductResource, 'products',full=True)
	class Meta:
		queryset = Dish.objects.all().order_by("category__order")
		resource_name = 'resdishes'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']
		filtering = {
            'av': ALL_WITH_RELATIONS,
        }
	def dehydrate(self, bundle):
		bundle.data['trans'] = list(chain(DishTranslation.objects.filter(dish = bundle.data['id']).values('name', 'description', 'lang__name', )))
		bundle.data['currencies'] = list(chain(DishPrice.objects.filter(dish = bundle.data['id']).values('price', 'currency__id', )))
		return bundle

class EmployeeResource(ModelResource):
	class Meta:
		queryset = Employee.objects.all().order_by('surname')
		resource_name = 'resemployees'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']
		filtering = {
            'position': ALL,
        }

class CookTaskResource(ModelResource):
	provider = fields.ForeignKey(EmployeeResource, 'provider',full=True)
	cook = fields.ForeignKey(EmployeeResource, 'cook',full=True)
	#orders = fields.ManyToManyField(OrderCookResource, 'cookorders',full=True, null = True)

	def dispatch_list(self, request, **kwargs):
        # TODO: Refactor this
		if request.method == "POST":
			orders = CookOrder.objects.filter(task = bundle.data['id']).values('count', 'product__name', 'product__unit')
			orderDesc = ""
			for order in orders:
				orderDesc += order.product__name + " x " + order.count + " " + order.product__unit
				Notification.objects.create(employee=bundle.data['cook'], title = "Dostales nowe zamowienie", desc = orderDesc)
			return super(CookTaskResource, self).dispatch_list(request, **kwargs)
		return super(CookTaskResource, self).dispatch_list(request, **kwargs)

	class Meta:
		always_return_data = True
		limit = 0
		today_min = datetime.date.today().strftime("%Y")
		today_minm = datetime.date.today().strftime("%m")
		today_mind = datetime.date.today().strftime("%d")
		queryset = CookTask.objects.filter(created_at__year = today_min, created_at__month = today_minm)

		resource_name = 'cooktasks'
		allowed_methods = ['get','put', 'post', 'delete']
		authentication = Authentication()
		authorization = Authorization()
		filtering = {
			'state': ALL,
			'cook' : ALL_WITH_RELATIONS,
			'provider':ALL_WITH_RELATIONS
        }
	def dehydrate(self, bundle):
		bundle.data['orders'] = CookOrder.objects.filter(task = bundle.data['id']).values('count', 'product__name', 'product__unit')
		return bundle


class OrderCookResource(ModelResource):
	product = fields.ForeignKey(ProductResource, 'product',full=True)
	task = fields.ForeignKey(CookTaskResource, 'task',full=True,null=True)
	class Meta:
		always_return_data = True
		limit = 0
		queryset = CookOrder.objects.all()
		resource_name = 'cookorders'
		allowed_methods = ['get','put', 'post', 'delete']
		authentication = Authentication()
		authorization = Authorization()


class CurrencyResource(ModelResource):
	class Meta:
		queryset = Currency.objects.all()
		resource_name = 'currency'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']





class OrderResource(ModelResource):
	waiter = fields.ForeignKey(EmployeeResource, 'waiter',full=True)
	cook = fields.ForeignKey(EmployeeResource, 'cook',full=True)
	currency = fields.ForeignKey(CurrencyResource, 'currency',full=True)
	class Meta:
		always_return_data = True
		limit = 0
		queryset = WaiterTask.objects.all()
		resource_name = 'waitertasks'
		allowed_methods = ['get','put', 'post', 'delete']
		authentication = Authentication()
		authorization = Authorization()

class OrderResourceGet(ModelResource):
	waiter = fields.ForeignKey(EmployeeResource, 'waiter',full=True)
	cook = fields.ForeignKey(EmployeeResource, 'cook',full=True)
	currency = fields.ForeignKey(CurrencyResource, 'currency',full=True)
#	created_at = fields.DateTimeField( 'creaded_at',full=True)
	class Meta:
		always_return_data = True
		limit = 0
		today_min = datetime.date.today() + datetime.timedelta(days = 2)
		today_minm = datetime.datetime.now() - datetime.timedelta(days = 1)
		today_mind = datetime.date.today().strftime("%d")
		queryset = WaiterTask.objects.filter(created_at__range=[today_minm.strftime('%Y-%m-%d %H:%S'), today_min.strftime('%Y-%m-%d %H:%S')], state = 0)
		resource_name = 'waitertasksget'
		allowed_methods = ['get',]
		filtering = {
			'cook' : ALL_WITH_RELATIONS,
			'waiter':ALL_WITH_RELATIONS,
			'state':ALL,
        }
		authentication = Authentication()
		authorization = Authorization()
	def dehydrate(self, bundle):
		order = WaiterOrderDetails.objects.filter(task = bundle.data['id'], state = 0)
		orders = []
		for ord in order:
			orders = list(chain(orders, WaiterOrder.objects.filter(task = ord).values('count', 'dish__name', 'comment', 'level', 'task__id')))
		bundle.data['orders'] = orders
		bundle.data['created_at'] = bundle.data['created_at'].strftime("%H:%M")
		return bundle

class OrderResourceGet1(ModelResource):
	waiter = fields.ForeignKey(EmployeeResource, 'waiter',full=True)
	cook = fields.ForeignKey(EmployeeResource, 'cook',full=True)
	currency = fields.ForeignKey(CurrencyResource, 'currency',full=True)
#	created_at = fields.DateTimeField( 'creaded_at',full=True)
	class Meta:
		always_return_data = True
		limit = 0
		today_min = datetime.date.today() + datetime.timedelta(days = 1)
		today_minm = datetime.datetime.now() - datetime.timedelta(days = 1)
		today_mind = datetime.date.today().strftime("%d")
		queryset1 = []
		for task in WaiterOrderDetails.objects.filter(state = "1"):
			queryset1.append(task.task.id)
		queryset = WaiterTask.objects.filter(created_at__range=[today_minm.strftime('%Y-%m-%d %H:%S'), today_min.strftime('%Y-%m-%d %H:%S')], state = 0,id__in=queryset1)
		resource_name = 'waitertasksget1'
		allowed_methods = ['get',]
		filtering = {
			'cook' : ALL_WITH_RELATIONS,
			'waiter':ALL_WITH_RELATIONS,
			'state':ALL,
        }
		authentication = Authentication()
		authorization = Authorization()
	def dehydrate(self, bundle):
		order = WaiterOrderDetails.objects.filter(task = bundle.data['id'], state = 1)
		orders = []
		for ord in order:
			orders = list(chain(orders, WaiterOrder.objects.filter(task = ord).values('count', 'dish__name', 'comment', 'level', 'task__id', 'task__state')))
		bundle.data['orders'] = orders
		bundle.data['created_at'] = bundle.data['created_at'].strftime("%H:%M")
		return bundle

class OrderResourceGet2(ModelResource):
	waiter = fields.ForeignKey(EmployeeResource, 'waiter',full=True)
	cook = fields.ForeignKey(EmployeeResource, 'cook',full=True)
	currency = fields.ForeignKey(CurrencyResource, 'currency',full=True)
#	created_at = fields.DateTimeField( 'creaded_at',full=True)
	class Meta:
		always_return_data = True
		limit = 0
		today_min = datetime.date.today() + datetime.timedelta(days = 1)
		today_minm = datetime.datetime.now() - datetime.timedelta(days = 1)
		today_mind = datetime.date.today().strftime("%d")
		queryset1 = []
		for task in WaiterOrderDetails.objects.filter(state = "2"):
			queryset1.append(task.task.id)
		queryset1 = WaiterTask.objects.filter(created_at__range=[today_minm.strftime('%Y-%m-%d %H:%S'), today_min.strftime('%Y-%m-%d %H:%S')], state = 0,id__in=queryset1)
		queryset2 = WaiterTask.objects.filter(created_at__range=[today_minm.strftime('%Y-%m-%d %H:%S'), today_min.strftime('%Y-%m-%d %H:%S')], state = 1)[:5]
		queryset = queryset1|queryset2
		resource_name = 'waitertasksget2'
		allowed_methods = ['get',]
		filtering = {
			'cook' : ALL_WITH_RELATIONS,
			'waiter':ALL_WITH_RELATIONS,
			'state':ALL,
        }
		authentication = Authentication()
		authorization = Authorization()
	def dehydrate(self, bundle):
		order = WaiterOrderDetails.objects.filter(task = bundle.data['id'], state = 2)
		orders = []
		for ord in order:
			orders = list(chain(orders, WaiterOrder.objects.filter(task = ord).values('count', 'dish__name', 'comment', 'level', 'task__id', 'task__state')))
		bundle.data['orders'] = orders
		bundle.data['created_at'] = bundle.data['created_at'].strftime("%H:%M")
		return bundle

class WaiterOrderDetailsResource(ModelResource):
	task = fields.ForeignKey(OrderResource, 'task',full=True)
	class Meta:
		always_return_data = True
		limit = 0
		queryset = WaiterOrderDetails.objects.all()
		resource_name = 'waiterorderdetails'
		allowed_methods = ['get','put', 'post', 'delete']
		authentication = Authentication()
		authorization = Authorization()



class WaiterCookResource(ModelResource):
	dish = fields.ForeignKey(DishResource, 'dish',full=True)
	task = fields.ForeignKey(WaiterOrderDetailsResource, 'task',full=True)
	class Meta:
		always_return_data = True
		limit = 0
		queryset = WaiterOrder.objects.all()
		resource_name = 'waiterorders'
		allowed_methods = ['get','put', 'post', 'delete']
		authentication = Authentication()
		authorization = Authorization()
class DishTranslationResource(ModelResource):
	lang = fields.ForeignKey(LanguageResource, 'lang',full=True)
	dish = fields.ForeignKey(DishResource, 'dish',full=True)
	class Meta:
		queryset = DishTranslation.objects.all()
		resource_name = 'dishtranslation'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']
class ProductranslationResource(ModelResource):
	lang = fields.ForeignKey(LanguageResource, 'lang',full=True)
	product = fields.ForeignKey(ProductResource, 'product',full=True)
	class Meta:
		queryset = ProductTranslation.objects.all()
		resource_name = 'producttranslation'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']
class CategoryTranslationResource(ModelResource):
	lang = fields.ForeignKey(LanguageResource, 'lang',full=True)
	category = fields.ForeignKey(CategoryResource, 'category',full=True)
	class Meta:
		queryset = DishTranslation.objects.all()
		resource_name = 'categorytranslation'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']