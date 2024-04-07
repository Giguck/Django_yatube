from django.contrib import admin
from .models import Post, Group
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'short_text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'

    def short_text(self, obj):
        return obj.text[:120] if len(obj.text) > 120 else obj.text


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author')
    search_fields = ('title', 'author')
    list_filter = ('author',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
