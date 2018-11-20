from tastypie.resources import ModelResource
import datetime
from cook.models import Product, Employee, Dish, Category, WaiterTask, CookTask, CookOrder, CookOrderTask
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

class OrderCookResource(ModelResource):
	product = fields.ForeignKey(ProductResource, 'product',full=True)
	class Meta:
		queryset = CookOrder.objects.all()
		resource_name = 'cookorders'
		allowed_methods = ['get','put', 'post', 'delete']
		authentication = Authentication()
		authorization = Authorization()		

class CookTaskResource(ModelResource):
	provider = fields.ForeignKey(EmployeeResource, 'provider',full=True)
	cook = fields.ForeignKey(EmployeeResource, 'cook',full=True)
	cookorders = fields.ManyToManyField(OrderCookResource, 'cookorders',full=True)

	class Meta:
		today_min = datetime.date.today().strftime("%Y")
		today_minm = datetime.date.today().strftime("%m")
		queryset = CookTask.objects.filter(created_at__year = today_min, created_at__month = today_minm)
		resource_name = 'cooktasks'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']
		filtering = {
            'state': ALL,
            'provider': ALL_WITH_RELATIONS,
        }
		
class OrderCookTaskResource(ModelResource):
	task = fields.ForeignKey(CookTaskResource, 'task',full=True)
	order = fields.ForeignKey(OrderCookResource, 'order',full=True)
	class Meta:
		queryset = CookOrderTask.objects.all()
		resource_name = 'cookordertasks'
		allowed_methods = ['get','put', 'post', 'delete']
		authentication = Authentication()
		authorization = Authorization()


class OrderResource(ModelResource):
	waiter = fields.ForeignKey(EmployeeResource, 'waiter',full=True)
	class Meta:
		queryset = WaiterTask.objects.all()
		resource_name = 'waitertasks'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']
		filtering = {
            'state': ALL,
            'waiter': ALL_WITH_RELATIONS,
        }
		
class OrderCookResource(ModelResource):
	product = fields.ForeignKey(ProductResource, 'product',full=True)
	class Meta:
		queryset = CookOrder.objects.all()
		resource_name = 'cookorders'
		allowed_methods = ['get','put', 'post', 'delete']
		authentication = Authentication()
		authorization = Authorization()	
class WaiterCookTaskResource(ModelResource):
	task = fields.ForeignKey(OrderResource, 'task',full=True)
	order = fields.ForeignKey(OrderCookResource, 'order',full=True)
	class Meta:
		queryset = CookOrderTask.objects.all()
		resource_name = 'cookordertasks'
		allowed_methods = ['get','put', 'post', 'delete']
		authentication = Authentication()
		authorization = Authorization()