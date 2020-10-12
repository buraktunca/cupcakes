from django.contrib import admin

# Register your models here.
from store.models import TopCategory,AltCategory,Product

class categoryadmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = (
    'pk',
    'name',
    'slug',
    'is_active'
    )
    list_filter = ('name','is_active',)
    list_editable = ('name','slug','is_active',)

class productadmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = (
    'pk',
    'name',
    'slug',
    'is_active',
    'is_bestseller',
    'categories'

    )
    list_filter = ('name','is_active',)
    list_editable = ('name','slug','is_active','is_bestseller')


admin.site.register(TopCategory,categoryadmin)
admin.site.register(AltCategory,categoryadmin)
admin.site.register(Product,productadmin)
