from datetime import timedelta, date
import datetime

from cook.models import Product, Employee, Dish, Category, WaiterTask, CookTask, CookOrder, WaiterOrder, Currency, WaiterOrderDetails, DishTranslation
from cook.models import DishPrice, ProductTranslation, CategoryTranslation, Language, Notification, DishProduct
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
	def obj_create(self, bundle, **kwargs):
		bundle = super(LanguageResource, self).obj_create(bundle)
		lang = Language.objects.filter(name = bundle.data.get('name')).first()
		for object in Dish.objects.all():
			DishTranslation.objects.create(dish_id = object.id, lang_id = lang.id, name = object.name + lang.name, description = object.description + lang.name)
		for object in Product.objects.all():
			ProductTranslation.objects.create(product_id = object.id, lang_id = lang.id, name = object.name + lang.name)
		for object in Category.objects.all():
			CategoryTranslation.objects.create(category_id = object.id, lang_id = lang.id, name = object.category_name + lang.name)
		return bundle



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
		queryset = Dish.objects.all().order_by("category__order", "name")
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
		bundle.data['dishproducts'] = list(chain(DishProduct.objects.filter(dish = bundle.data['id']).values('count', 'product__name','product__unit', )))
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
class DishProductResource(ModelResource):
	dish = fields.ForeignKey(DishResource, 'dish')
	product = fields.ForeignKey(ProductResource, 'product')
	class Meta:
		queryset = DishProduct.objects.all()
		resource_name = 'dishproducts'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']
class CookTaskResource(ModelResource):
	provider = fields.ForeignKey(EmployeeResource, 'provider',full=True)
	cook = fields.ForeignKey(EmployeeResource, 'cook',full=True)
	#orders = fields.ManyToManyField(OrderCookResource, 'cookorders',full=True, null = True)
	def obj_create(self, bundle, **kwargs):

		employee = Employee.objects.filter(pk = bundle.data.get('cook').rsplit('/')[3]).first()
		orderDesc = "Zamówienie od: " + employee.name+" "+ employee.surname
		employee = Employee.objects.filter(pk = bundle.data.get('provider').rsplit('/')[3]).first()
		Notification.objects.create(employee=employee, title = "Dostales nowe zamowienie", desc = orderDesc)
		return super(CookTaskResource, self).obj_create(bundle, **kwargs)

	def obj_update(self, bundle, **kwargs):
# update an existing row
		id = int(kwargs['pk'])
		obj = CookTask.objects.filter(pk = id).first()
		if obj.state == "1":
			employee = Employee.objects.filter(pk = obj.provider.id).first()
			orderDesc = "Zamówienie od: " + obj.provider.name+" "+ obj.provider.surname
			employee = Employee.objects.filter(pk = obj.cook.id).first()
			Notification.objects.create(employee=employee, title = "status-changed", desc = orderDesc)
		elif obj.state == '2':
			for order in CookOrder.objects.filter(task = obj):
				product = order.product
				product.stock =+ order.count
				product.state = '2'
				product.save()
				dishes = Dish.objects.all().filter(products = product)
				if dishes[0]:
					dishes.update(av='0')
					for i in range(len(dishes)):
						for product in dishes[i].products.all():
							if product.av == '0':
								dishes[i].av='1'
								dishes[i].save()
								break
		return super(CookTaskResource, self).obj_update(bundle, **kwargs)
	def obj_delete(self, bundle, **kwargs):
		pk = int(kwargs['pk'])
		obj = CookTask.objects.filter(pk = pk).first()

		employee = Employee.objects.filter(pk = obj.provider.id).first()
		orderDesc = "Zamówienie od: " + employee.name+" "+ employee.surname
		employee = Employee.objects.filter(pk = obj.cook.id).first()
		Notification.objects.create(employee=employee, title = "status-deleted", desc = orderDesc)
		return super(CookTaskResource, self).obj_delete(bundle, **kwargs)

	class Meta:
		always_return_data = True
		limit = 0
		today_min = datetime.date.today().strftime("%Y")
		today_minm = datetime.date.today().strftime("%m")
		today_mind = datetime.date.today().strftime("%d")
		queryset = CookTask.objects.filter(created_at__year = today_min, created_at__month = today_minm)#, created_at__day = today_mind)

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
		bundle.data['orders'] = list(CookOrder.objects.filter(task = bundle.data['id']).values('count', 'product__name', 'product__unit', 'id'))
		bundle.data['created_at'] = bundle.data['created_at'].strftime("%H:%M")
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
	def obj_delete(self, bundle, **kwargs):
		pk = int(kwargs['pk'])
		obj = CookOrder.objects.filter(pk = pk).first()
		task = CookTask.objects.filter(pk = obj.task.id).first()
		bundle = super(OrderCookResource, self).obj_delete(bundle, **kwargs)
		if(not CookOrder.objects.filter(task = task)) :
			task.delete()
		return bundle

class CurrencyResource(ModelResource):
	class Meta:
		queryset = Currency.objects.all()
		resource_name = 'currency'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']

	def obj_create(self, bundle, **kwargs):
		bundle = super(CurrencyResource, self).obj_create(bundle)
		cur = Currency.objects.filter(name = bundle.data.get('name')).first()
		value = cur.value
		for object in Dish.objects.all():
			DishPrice.objects.create(dish_id = object.id, currency_id = cur.id, price =  object.price/value)
		return bundle



class RestaurantDetailResource(ModelResource):
	default_currency = fields.ForeignKey(CurrencyResource, 'default_currency',full=True)
	default_lang = fields.ForeignKey(LanguageResource, 'default_lang',full=True)
	class Meta:
		from .models import RestaurantDetail
		queryset = RestaurantDetail.objects.all()
		resource_name = 'resdet'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['put']
	def obj_update(self, bundle, **kwargs):
		from .models import RestaurantDetail
# update an existing row
		olddefault_lang = RestaurantDetail.objects.all().first().default_lang
		bundle = super(RestaurantDetailResource, self).obj_update(bundle, **kwargs)
		newdefault_lang = RestaurantDetail.objects.all().first().default_lang
		if newdefault_lang.id != olddefault_lang.id:
			dishtrans = DishTranslation.objects.filter(lang = newdefault_lang)
			for dish in Dish.objects.all():
				trans = dishtrans.get(dish = dish)
				dishname = dish.name
				dishdesc = dish.description
				dish.name = trans.name
				dish.description = trans.description
				trans.name = dishname
				trans.description = dishdesc
				trans.lang = olddefault_lang
				trans.save()
				dish.save()
			producttrans = ProductTranslation.objects.filter(lang = newdefault_lang)
			for product in Product.objects.all():
				trans = producttrans.get(product = product)
				productname = product.name
				product.name = trans.name
				trans.name = productname
				trans.lang = olddefault_lang
				trans.save()
				product.save()
			ctrans = CategoryTranslation.objects.filter(lang = newdefault_lang)
			for cat in Category.objects.all():
				trans = ctrans.get(category = cat)
				productname = cat.category_name
				cat.category_name = trans.name
				trans.lang = olddefault_lang
				trans.name = productname
				trans.save()
				cat.save()

		return bundle


class OrderResource(ModelResource):
	waiter = fields.ForeignKey(EmployeeResource, 'waiter',full=True)
	cook = fields.ForeignKey(EmployeeResource, 'cook',full=True)
	supplier = fields.ForeignKey(EmployeeResource, 'supplier',full=True,null=True)
	currency = fields.ForeignKey(CurrencyResource, 'currency',full=True)
	def obj_create(self, bundle, **kwargs):

		employee = Employee.objects.filter(pk = bundle.data.get('waiter').rsplit('/')[3]).first()
		orderDesc = "Zamówienie od: " + employee.name+" "+ employee.surname
		employee = Employee.objects.filter(pk = bundle.data.get('cook').rsplit('/')[3]).first()
		Notification.objects.create(employee=employee, title = "Dostales nowe zamowienie", desc = orderDesc)
		if bundle.data.get('supplier'):
			employee = Employee.objects.filter(pk = bundle.data.get('supplier').rsplit('/')[3]).first()
			Notification.objects.create(employee=employee, title = "Dostales nowe zamowienie", desc = orderDesc)
		return super(OrderResource, self).obj_create(bundle, **kwargs)
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
		queryset = WaiterTask.objects.filter(created_at__range=[today_minm.strftime('%Y-%m-%d %H:%S'), today_min.strftime('%Y-%m-%d %H:%S')], state = 0, reservation__isnull = True) | WaiterTask.objects.filter(reservation__range=[today_minm.strftime('%Y-%m-%d %H:%S'), today_min.strftime('%Y-%m-%d %H:%S')], state = 0)
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
			orders = list(chain(orders, WaiterOrder.objects.filter(task = ord).values('count', 'dish__name','id', 'comment', 'level', 'task__id')))
		bundle.data['orders'] = orders
		bundle.data['created_at'] = bundle.data['created_at'].strftime("%H:%M")
		return bundle
class ReservationResourceGet(ModelResource):
	waiter = fields.ForeignKey(EmployeeResource, 'waiter',full=True)
	cook = fields.ForeignKey(EmployeeResource, 'cook',full=True)
	currency = fields.ForeignKey(CurrencyResource, 'currency',full=True)
#	created_at = fields.DateTimeField( 'creaded_at',full=True)
	class Meta:
		always_return_data = True
		limit = 0
		today_min = datetime.date.today() + datetime.timedelta(days = 2)
		today_minm = datetime.datetime.now() - datetime.timedelta(days = 31)
		today_mind = datetime.date.today().strftime("%d")
		queryset = WaiterTask.objects.filter(reservation__isnull=False, state = 0)
		resource_name = 'reservations'
		allowed_methods = ['get',]
		authentication = Authentication()
		authorization = Authorization()
	def dehydrate(self, bundle):
		order = WaiterOrderDetails.objects.filter(task = bundle.data['id'], state = 0)
		orders = []
		for ord in order:
			orders = list(chain(orders, WaiterOrder.objects.filter(task = ord).values('count', 'dish__name', 'comment', 'level', 'task__id','id', 'task__state')))
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
		today_minm = datetime.datetime.now() - datetime.timedelta(days = 2)
		today_mind = datetime.date.today().strftime("%d")
		queryset1 = []
		for task in WaiterOrderDetails.objects.filter(state = "1"):
			queryset1.append(task.task.id)
		queryset = WaiterTask.objects.filter(created_at__range=[today_minm.strftime('%Y-%m-%d %H:%S'), today_min.strftime('%Y-%m-%d %H:%S')], reservation__isnull = True, state = 0,id__in=queryset1)
		queryset1 = WaiterTask.objects.filter(reservation__range=[today_minm.strftime('%Y-%m-%d %H:%S'), today_min.strftime('%Y-%m-%d %H:%S')], state = 0,id__in=queryset1)
		queryset = queryset|queryset1
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
			orders = list(chain(orders, WaiterOrder.objects.filter(task = ord).values('count', 'dish__name', 'comment', 'level', 'task__id','id', 'task__state')))
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
		today_minm = datetime.datetime.now() - datetime.timedelta(days = 2)
		today_mind = datetime.date.today().strftime("%d")
		queryset0 = []
		for task in WaiterOrderDetails.objects.filter(state = "2"):
			queryset0.append(task.task.id)
		queryset1 = WaiterTask.objects.filter(created_at__range=[today_minm.strftime('%Y-%m-%d %H:%S'), today_min.strftime('%Y-%m-%d %H:%S')], reservation__isnull = True, state = 0,id__in=queryset0)
		queryset2 = WaiterTask.objects.filter(created_at__range=[today_minm.strftime('%Y-%m-%d %H:%S'), today_min.strftime('%Y-%m-%d %H:%S')], state = 1)[:5]
		queryset3 = WaiterTask.objects.filter(reservation__range=[today_minm.strftime('%Y-%m-%d %H:%S'), today_min.strftime('%Y-%m-%d %H:%S')], state = 0,id__in=queryset0)
		queryset = queryset1|queryset2|queryset3
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
			orders = list(chain(orders, WaiterOrder.objects.filter(task = ord).values('count', 'dish__name', 'comment','id', 'level', 'task__id', 'task__state')))
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
	def obj_update(self, bundle, **kwargs):
# update an existing row
		pk = int(kwargs['pk'])
		obj = WaiterOrderDetails.objects.filter(pk = pk).first()
		if obj.state == '1':
			task = WaiterTask.objects.filter(pk = obj.task.id).first()
			employee = Employee.objects.filter(pk = task.cook.id).first()
			orderDesc = "Zamówienie od: " + employee.name+" "+ employee.surname
			employee = Employee.objects.filter(pk = task.waiter.id).first()
			Notification.objects.create(employee=employee, title = "status-ready", desc = orderDesc)
			for order in WaiterOrder.objects.filter(task = obj):
				dish = order.dish
				count = order.count
				for dishproduct in DishProduct.objects.filter(dish = dish):
					product = dishproduct.product
					product.stock =- dishproduct.count * count
					if product.stock < 0 : product.stock = 0
					product.save()
					if product.stock == 0 :
					    Dish.objects.all().filter(products = product).update(av='1')

		return super(WaiterOrderDetailsResource, self).obj_update(bundle, **kwargs)
	def obj_delete(self, bundle, **kwargs):
		pk = int(kwargs['pk'])
		obj = WaiterOrderDetails.objects.filter(pk = pk).first()
		taskid = obj.task.id
		task = WaiterTask.objects.filter(pk = taskid).first()
		bundle = super(WaiterOrderDetailsResource, self).obj_delete(bundle, **kwargs)
		if(not WaiterOrderDetails.objects.filter(task = task)) :
			employee = Employee.objects.filter(pk = task.waiter.id).first()
			orderDesc = "Zamówienie od: " + employee.name+" "+ employee.surname
			employee = Employee.objects.filter(pk = task.cook.id).first()
			Notification.objects.create(employee=employee, title = "status-deleted", desc = orderDesc)
			task.delete()
		return bundle



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
	def obj_update(self, bundle, **kwargs):
# update an existing row
		pk = int(kwargs['pk'])

		obj = WaiterOrder.objects.filter(pk = pk).first()
		task = WaiterTask.objects.filter(pk = obj.task.task.id).first()

		employee = Employee.objects.filter(pk = task.waiter.id).first()
		orderDesc = "Zamówienie od: " + employee.name+" "+ employee.surname
		employee = Employee.objects.filter(pk = task.cook.id).first()
		#Notification.objects.create(employee=employee, title = "Zmiana statusu zamówienia", desc = orderDesc)
		if 'count' in bundle.data:
			Notification.objects.create(employee=employee, title = "Zamówienie zostało edytowane", desc = orderDesc)
			from decimal import Decimal
			diff = Decimal(bundle.data['count']) / obj.count
			newprice = diff * obj.price
			newdefprice = diff * obj.price_default
			task.price = task.price + (newprice - obj.price)
			task.price_default = task.price_default + (newdefprice - obj.price)
			obj.price = newprice
			obj.price_default = newdefprice
			obj.save()
			task.save()
		return super(WaiterCookResource, self).obj_update(bundle, **kwargs)

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
		queryset = CategoryTranslation.objects.all()
		resource_name = 'categorytranslation'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']