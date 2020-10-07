from django.contrib import admin

# Register your models here.
from store.models import Category

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



admin.site.register(Category,categoryadmin)
