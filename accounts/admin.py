from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'company', 'is_staff']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields':('company',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields':('company',)}),)

admin.site.register(CustomUser, CustomUserAdmin)