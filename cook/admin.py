from django.contrib import admin
from .models import Dish, Product, Employee, WaiterTask, CookTask, Category
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(WaiterTask)
admin.site.register(CookTask)
