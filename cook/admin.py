from django.contrib import admin
from .models import Dish, Product, Employee, WaiterTask, CookTask, Category, DishPrice, Currency, RestaurantDetail,LoginLog,WaiterOrder, CookOrder
from .models import Language, DishTranslation, ProductTranslation, CategoryTranslation, Notification
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(WaiterTask)
admin.site.register(CookTask)
admin.site.register(DishPrice)
admin.site.register(Currency)
admin.site.register(RestaurantDetail)
admin.site.register(LoginLog)
admin.site.register(WaiterOrder)
admin.site.register(CookOrder)
admin.site.register(Language)
admin.site.register(CategoryTranslation)
admin.site.register(ProductTranslation)
admin.site.register(DishTranslation)
admin.site.register(Notification)


