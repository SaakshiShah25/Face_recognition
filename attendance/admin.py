from django.contrib import admin
from .models import Account,New,Manual
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm


# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_form=UserCreationForm
    list_display=('username','email','sapid','department','is_admin')
    list_filter=['is_admin']

    fieldsets=(
        (None,{'fields':('username','email','sapid','department','password')}),
        ('Permissions',{'fields':('is_admin',)})
    )
    search_fields=('username','email','sapid','department')
    ordering=('username','email','sapid','department')


admin.site.register(Account,UserAdmin)
admin.site.register(New)
admin.site.register(Manual)