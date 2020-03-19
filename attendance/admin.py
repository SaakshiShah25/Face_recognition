from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm

# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_form=UserCreationForm
    list_display=('username','email','is_admin')
    list_filter=['is_admin']

    fieldsets=(
        (None,{'fields':('username','email','password')}),
        ('Permissions',{'fields':('is_admin',)})
    )
    search_fields=('username','email')
    ordering=('username','email')


admin.site.register(Account,UserAdmin)