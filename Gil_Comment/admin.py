from django.contrib import admin

from .models import Comments


class CommentAdmin(admin.ModelAdmin):
    list_display = ["__str__", "product", "message", "postedTime", 'active']

    class Meta:
        model = Comments


admin.site.register(Comments, CommentAdmin)
