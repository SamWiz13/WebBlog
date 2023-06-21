from django.contrib import admin
from .models  import Category, Pizza, PizzaNumbers, Chef

class CategoryAdmin(admin.ModelAdmin):
    list_display =['name', 'slug']
    prepopulated_fields ={'slug' : ("name", )}


admin.site.register(Category, CategoryAdmin) 


class PizzaAdmin(admin.ModelAdmin):
    list_display =['title', 'slug', 'price', 'created_at']
    prepopulated_fields ={'slug' : ("title", )}


admin.site.register(Pizza, PizzaAdmin) 



class PizzaNumbersAdmin(admin.ModelAdmin):
    list_display =['branches', 'awards', 'customer', 'staff']



admin.site.register(PizzaNumbers, PizzaNumbersAdmin) 


class ChefAdmin(admin.ModelAdmin):
    list_display =['first_name', 'last_name', 'specialist', 'created_at']



admin.site.register(Chef, ChefAdmin) 