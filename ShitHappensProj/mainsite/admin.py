from django.contrib import admin
from .models import Story, Users_LikeStories, Users_DisLikeStories


# Register your models here.
#admin.site.register(Story)
admin.site.register(Users_LikeStories)
admin.site.register(Users_DisLikeStories)





@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('pk','user_id', 'create_date', 'expire_date')
    # inlines = [StoryInline]

