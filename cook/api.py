from tastypie.resources import ModelResource
from cook.models import Product, Employee, Dish, Category, WaiterTask, CookTask, DishOrder
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from itertools import chain
class CategoryResource(ModelResource):
	class Meta:
		queryset = Category.objects.all()
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
		queryset = Dish.objects.all().order_by('category.name','name')
		resource_name = 'resdishes'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']
		filtering = {
            'av': ALL_WITH_RELATIONS,    
        }

class DishOrderResource(ModelResource):
	dish = fields.ForeignKey(DishResource, 'dish',full=True)
	class Meta:
		queryset = DishOrder.objects.all()
		resource_name = 'dishorder'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']		
		always_return_data = True
		
class EmployeeResource(ModelResource):
	class Meta:
		queryset = Employee.objects.all().order_by('surname')
		resource_name = 'resemployees'		
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']	
		
class EmployeeProductResource(ModelResource):
	class Meta:
		queryset = list(chain(Employee.objects.all(), Product.objects.all().order_by('name')))
		resource_name = 'resemployeesproducts'		
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']	


		
		
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
	provider = fields.ForeignKey(EmployeeResource, 'provider',full=True)
	class Meta:
		queryset = CookTask.objects.all()
		resource_name = 'cooktasks'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']
		filtering = {
            'state': ALL,
            'provider': ALL_WITH_RELATIONS,       
        }