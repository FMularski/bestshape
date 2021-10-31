from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Shape, Vote


class ShapeAdmin(admin.ModelAdmin):
    list_display = 'name', 'image' 


class VoteAdmin(admin.ModelAdmin):
    list_display = 'user', 'shape'


admin.site.register(User, UserAdmin)
admin.site.register(Shape, ShapeAdmin)
admin.site.register(Vote, VoteAdmin)

