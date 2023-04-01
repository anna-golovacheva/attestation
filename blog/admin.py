from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('header', 'body', 'user_link', 'pic', 'created', 'updated')
    readonly_fields = ('user_link',)

    list_filter = [
        "created",
    ]

    def user_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:users_user_change", args=(obj.author.pk,)),
            obj.author.email
        ))

    user_link.short_description = 'user'

