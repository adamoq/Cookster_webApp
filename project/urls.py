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
from cook.views import main, products, administration, employers, menu, orders, login_user, category, dish, orders_waiter, login_mobile, changepassword,changephone, changeproduct
from django.contrib import admin
from cook.api import ProductResource, EmployeeResource, DishResource, CategoryResource, OrderResource, OrderCookResource, DishOrderResource
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
	url(r'^orders-waiter/$', orders_waiter),
	url(r'^orders/$', orders, name = 'orders'),
	url(r'^category/$', category),
	url(r'^dish/$', dish),
	url(r'^api/', include(ProductResource().urls)),
	url(r'^api/', include(EmployeeResource().urls)),
	url(r'^api/', include(DishResource().urls)),
	url(r'^api/', include(CategoryResource().urls)),
	url(r'^api/', include(OrderResource().urls)),
	url(r'^api/', include(OrderCookResource().urls)),
	url(r'^api/', include(DishOrderResource().urls)),
	url(r'^mobileapi/$', login_mobile),
	url(r'^mobilereset/password/$', changepassword),
	url(r'^mobilereset/phone/$', changephone),
	url(r'^mobilereset/product/$', changeproduct),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]