from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(User)




@admin.register(Hospital)
class RoleAdmin(admin.ModelAdmin):
    """
        Register Role model with specific fields
    """
    list_display = ("name", "category")

@admin.register(Banks)
class RoleAdmin(admin.ModelAdmin):
    """
        Register Role model with specific fields
    """
    list_display = ("name", "category")




@admin.register(Education)
class RoleAdmin(admin.ModelAdmin):
    """
        Register Role model with specific fields
    """
    list_display = ("name", "category")

@admin.register(Park)
class RoleAdmin(admin.ModelAdmin):
    """
        Register Role model with specific fields
    """
    list_display = ("name", "category")

@admin.register(Cafes)
class RoleAdmin(admin.ModelAdmin):
    """
        Register Role model with specific fields
    """
    list_display = ("name", "category")

@admin.register(Shopping)
class RoleAdmin(admin.ModelAdmin):
    """
        Register Role model with specific fields
    """
    list_display = ("name", "category")


@admin.register(Messages)
class RoleAdmin(admin.ModelAdmin):
    """
        Register Role model with specific fields
    """
    list_display = ("name", "subject")



@admin.register(Rating)
class RoleAdmin(admin.ModelAdmin):
    """
    Register Role model with specific fields
    """
    list_display = ("post", "user")