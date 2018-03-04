from tastypie.resources import ModelResource
from cook.models import Product, Employee, Dish, Category, WaiterTask, CookTask, DishOrder
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

class CategoryResource(ModelResource):
	class Meta:
		queryset = Category.objects.all()
		resource_name = 'category'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']
	
class ProductResource(ModelResource):
	class Meta:
		queryset = Product.objects.all()
		resource_name = 'products'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']

		
		
class DishResource(ModelResource):
	category = fields.ForeignKey(CategoryResource, 'category')
	class Meta:
		queryset = Dish.objects.all()
		resource_name = 'resdishes'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']
		filtering = {
            'position': ALL_WITH_RELATIONS,    
        }

class DishOrderResource(ModelResource):
	dish = fields.ForeignKey(Dish, 'dish',full=True)
	class Meta:
		queryset = DishOrder.objects.all()
		resource_name = 'dishorder'
		authentication = Authentication()
		authorization = Authorization()
		allowed_methods = ['get','put', 'post', 'delete']		
		
class EmployeeResource(ModelResource):
	class Meta:
		queryset = Employee.objects.all()
		resource_name = 'resemployees'
		authentication = Authentication()
		authorization = Authorization()
		filtering = {
            'position': ALL,    
        }
		
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