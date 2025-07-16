from django.contrib import admin

# Register your models here.
from .models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'date_created', 'last_updated')
    search_fields = ('name', 'email', 'phone_number')
