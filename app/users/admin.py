from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Home, CustomUser


class CustomUserAdmin(UserAdmin):
    # Custom admin for NNA model
    model = CustomUser
    list_display = ('id', 'email', 'name', 'surname', 'document', 'date_of_birth', 'home', 'status', 'created_at',)
    list_filter = ('is_active', 'home', 'roles')

    # Fieldsets for admin page
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal Info', {'fields': ('name', 'surname', 'document', 'date_of_birth', 'home', 'roles', 'status',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'surname',
                       'document', 'date_of_birth', 'home', 'roles', 'status'),
        }),
    )
    search_fields = ('id', 'email', 'name', 'surname', 'document', 'date_of_birth', 'home', 'roles', 'status')
    ordering = ('id',)


class HomeAdmin(admin.ModelAdmin):
    # Custom admin for Location model
    model = Home
    list_display = ('id', 'name', 'address')
    search_fields = ('id', 'name', 'address')
    ordering = ('id',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.site_header = 'Sirio App Administration'
