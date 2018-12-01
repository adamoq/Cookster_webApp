"""cookster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from . import settings
from django.conf import settings
from django.conf.urls.static import static
from cook.views import main, products, administration, employers, menu, orders, login_user, category, dish, orders_waiter, login_mobile
from cook.views import changepassword,resetpassword,changephone, changeproduct, login_mobile_status, product_chart, trans, currencies
from cook.charts import category_chart_json,category_chart_json2, dish_chart_json,category_chart_json1
from django.contrib import admin
from cook.api import ProductResource, EmployeeResource, DishResource, CategoryResource, OrderResource, OrderCookResource, CookTaskResource, DishPriceResource, LanguageResource
from cook.api import ProductranslationResource, DishTranslationResource, CategoryTranslationResource, WaiterOrderDetailsResource, WaiterCookResource, OrderResourceGet,OrderResourceGet1,OrderResourceGet2, CurrencyResource
from django.contrib.auth import views as auth_views


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', auth_views.login, {'template_name': 'login.html','redirect_authenticated_user': True}),
	url(r'^accounts/profile/$', products),
	url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}),
	url(r'^products/$', products, name = 'products'),
	url(r'^administration/$', administration, name = 'administration'),
	url(r'^employers/$', employers, name = 'employers'),
	url(r'^menu/$', menu, name = 'menu'),
	url(r'^trans/$', trans, name = 'trans'),
	url(r'^orders-waiter/$', orders_waiter),
	url(r'^orders/$', orders, name = 'orders'),
	url(r'^currencies/$', currencies, name = 'currencies'),
	url(r'^category/$', category),
	url(r'^dish/$', dish),
	url(r'^api/', include(ProductResource().urls)),
	url(r'^api/', include(EmployeeResource().urls)),
	url(r'^api/', include(DishResource().urls)),
	url(r'^api/', include(CategoryResource().urls)),
	url(r'^api/', include(OrderResource().urls)),
	url(r'^api/', include(OrderCookResource().urls)),
	url(r'^api/', include(CookTaskResource().urls)),
	url(r'^api/', include(WaiterOrderDetailsResource().urls)),
	url(r'^api/', include(WaiterCookResource().urls)),
	url(r'^api/', include(OrderResourceGet().urls)),
	url(r'^api/', include(OrderResourceGet1().urls)),
	url(r'^api/', include(DishTranslationResource().urls)),
	url(r'^api/', include(ProductranslationResource().urls)),
	url(r'^api/', include(CategoryTranslationResource().urls)),
	url(r'^api/', include(DishPriceResource().urls)),
	url(r'^api/', include(LanguageResource().urls)),

	url(r'^api/', include(OrderResourceGet2().urls)),
	url(r'^api/', include(CurrencyResource().urls)),
	url(r'^mobileapi/$', login_mobile),
	url(r'^mobileapistatus/$', login_mobile_status),
	url(r'^mobilereset/password/$', changepassword),
	url(r'^reset/password/$', resetpassword),
	url(r'^mobilereset/phone/$', changephone),
	url(r'^mobilereset/product/$', changeproduct),


	url(r'^menu/raport/$', product_chart, name='product_chart'),
	url(r'^products/raport-json/$', dish_chart_json, name='dish_chart_json'),
	url(r'^category/raport-json/$', category_chart_json, name='category_chart_json'),
	url(r'^category/raport-json1/$', category_chart_json1, name='category_chart_json1'),
	url(r'^category/raport-json2/$', category_chart_json2, name='category_chart_json2'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]