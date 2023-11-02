from django.contrib import admin
from User.models import User,Task
from Admin.models import Admin

# Register your models here.
mymodels = [User,Admin,Task]
admin.site.register(mymodels)