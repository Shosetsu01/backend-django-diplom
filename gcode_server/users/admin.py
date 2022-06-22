from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Faculties, Groups, News, DuelParticipatingNow, CommandParticipatingNow, LastWinners, Archive

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


class FacultiesAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Faculties, FacultiesAdmin)


class GroupsAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


admin.site.register(Groups, GroupsAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['date', 'title', 'text']
    list_filter = ['date']


admin.site.register(News, NewsAdmin)


class DuelParticipatingNowAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstPeople', 'groupFirst', 'secondPeople', 'groupSecond', 'acceptDuel']


admin.site.register(DuelParticipatingNow, DuelParticipatingNowAdmin)


class CommandParticipatingNowAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group', 'firstPeople', 'secondPeople',
                    'thirdPeople', 'fourthPeople', 'fifthPeople']


admin.site.register(CommandParticipatingNow, CommandParticipatingNowAdmin)


class LastWinnersAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'lineOne', 'lineTwo',
                    'lineThree', 'lineFour', 'lineFive']


admin.site.register(LastWinners, LastWinnersAdmin)


class ArchiveAdmin(admin.ModelAdmin):
    list_display = ['year', 'semester', 'musketeers', 'duel',
                    'groups']


admin.site.register(Archive, ArchiveAdmin)
