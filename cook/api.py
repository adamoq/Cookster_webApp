from tastypie.resources import ModelResource
import datetime
from cook.models import Product, Employee, Dish, Category, WaiterTask, CookTask, CookOrder, WaiterOrder, Currency
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

class CategoryResource(ModelResource):
	class Meta:
		queryset = Category.objects.all().order_by("order")
		resource_name = 'category'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']

class ProductResource(ModelResource):
	class Meta:
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

	class Meta:
		always_return_data = True
		today_min = datetime.date.today().strftime("%Y")
		today_minm = datetime.date.today().strftime("%m")
		today_mind = datetime.date.today().strftime("%d")
		queryset = CookTask.objects.filter(created_at__year = today_min, created_at__month = today_minm, created_at__day = today_mind)

		resource_name = 'cooktasks'
		allowed_methods = ['get','put', 'post', 'delete']
		authentication = Authentication()
		authorization = Authorization()
	def dehydrate(self, bundle):
		bundle.data['orders'] = CookOrder.objects.filter(task = bundle.data['id']).values('count', 'product__name', 'product__unit')
		return bundle


class OrderCookResource(ModelResource):
	product = fields.ForeignKey(ProductResource, 'product',full=True)
	task = fields.ForeignKey(CookTaskResource, 'task',full=True,null=True)
	class Meta:
		always_return_data = True
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
		today_min = datetime.date.today().strftime("%Y")
		today_minm = datetime.date.today().strftime("%m")
		today_mind = datetime.date.today().strftime("%d")
		queryset = WaiterTask.objects.filter(created_at__year = today_min, created_at__month = today_minm, created_at__day = today_mind)
		resource_name = 'waitertasks'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']

		filtering = {
            'state': ALL,
            'waiter': ALL_WITH_RELATIONS,
			'cook' : ALL_WITH_RELATIONS,
        }
	def dehydrate(self, bundle):
		bundle.data['orders'] = WaiterOrder.objects.filter(task = bundle.data['id']).values('count', 'dish__name', 'dish__unit')

class WaiterCookResource(ModelResource):
	dish = fields.ForeignKey(DishResource, 'dish',full=True)
	task = fields.ForeignKey(OrderResource, 'task',full=True)
	class Meta:
		queryset = WaiterOrder.objects.all()
		resource_name = 'waiterorders'
		allowed_methods = ['get','put', 'post', 'delete']
		authentication = Authentication()
		authorization = Authorization()
