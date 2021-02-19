from django.contrib import admin

# Register your models here.
from .models import Category,Rubric,Type,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

class RubricAdmin(admin.ModelAdmin):

    list_display = ['name','slug', 'category']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Rubric, RubricAdmin)

class TypeAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Type,TypeAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display =['name','price']

    prepopulated_fields = {'slug':('name',)}
    list_editable = ['price']
admin.site.register(Product,ProductAdmin)
