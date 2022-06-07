from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()


# @admin.action(description='Mark selected stories as published')
# def make_published(UserAdmin, request, queryset):
#     queryset.update(status='p')


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ('email', 'first_name', 'last_name', 'group',
                    'is_active', 'is_superuser',)
    list_filter = ('is_active', 'date_joined')
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Персональная информация', {'fields': ('first_name',
                                                'last_name',
                                                'group',
                                                'faculty',)
                                     }),
        ('Данные', {'fields': ('last_login',
                               'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name', 'group')
    ordering = ('-date_joined',)


admin.site.register(CustomUser, CustomUserAdmin)
