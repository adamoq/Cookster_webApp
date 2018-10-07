from django.contrib.auth.models import User 

def get_restaurant_name(self):
    return 'Restauracja testowa'

User.add_to_class("get_restaurant_name",get_restaurant_name)