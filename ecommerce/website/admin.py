from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Customer)
admin.site.register(Specs)
admin.site.register(ProductOrder)
