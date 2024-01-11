from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Company

class UserPermissionMixin:
    def has_view_permission(self, request, obj=None):
        return request.user.is_staff

    def has_add_permission(self, request):
        return request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff

    def has_module_permission(self, request):
        return request.user.is_staff

class CustomUserAdmin(UserPermissionMixin, admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "email",
        "username",
        "is_staff",
        "user_type",
        "company",
    ]

    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'company')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'user_type')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super(CustomUserAdmin, self).get_form(request, obj, **kwargs)
        '''Company must not be null'''
        form.base_fields['company'].required = True
        return form

class CustomCompanyAdmin(UserPermissionMixin, admin.ModelAdmin):
    model = Company
    list_display = ['name', 'industry', 'created_by', 'updated_by']

    class Meta:
        model = Company
        fields = ['name', 'industry', 'created_by', 'updated_by']

admin.site.register(User, CustomUserAdmin)
admin.site.register(Company, CustomCompanyAdmin)