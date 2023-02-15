from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class createuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class createproductorderform(ModelForm):
    class Meta:
        model = ProductOrder
        fields = "__all__"

class createorderform(ModelForm):
    class Meta:
        model =Orders
        fields = "__all__"
        exclude = ['status','customer']


class createproductform(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
class createspecsform(ModelForm):
    class Meta:
        model = Specs
        fields = '__all__'

class createcustomerform(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']