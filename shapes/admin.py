from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Shape


class ShapeAdmin(admin.ModelAdmin):
    list_display = 'name', 'image' 


admin.site.register(User, UserAdmin)
admin.site.register(Shape, ShapeAdmin)

