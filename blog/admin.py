from django.contrib import admin
from django.contrib.auth.models import Group
from rangefilter.filters import DateRangeFilter
from .models import (
    User,
    Post,
    Comment,
    Reaction
)


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    fields = (
        'first_name',
        'last_name',
        'email',
        'username',
        'password',
        'is_staff',
        'is_superuser',
        'is_active',
    )

    readonly_fields = (
        'date_joined',
        'last_login'
    )

    list_display = (
        'id', 
        'first_name',
        'last_name',
        'username',
        'email',
        'is_staff',
        'is_superuser',
        'is_active',
        'date_joined',
    )

    list_display_links = (
        'id',
        'first_name',
        'last_name',
        'username',
    )

    list_filter = (
        'is_staff',
        'is_superuser',
        'is_active',
        ('date_joined', DateRangeFilter)
    )

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'body',
        'author',
        'created_at',
    )

    readonly_fields = (
        'created_at',
        'get_body'
    )

    list_display = (
        'id', 
        'author',
        'title',
        'get_body',
        'get_comment_count',
        'created_at',
    )

    list_display_links = (
        'id',
        'title',
        'get_body',
    )

    search_fields = (
        'title',
        'get_body'
    )

    def get_body(self, obj):
        max_length = 70
        if len(obj.body) > max_length:
            return obj.body[:65] + ',,,'
        return obj.body
        
    get_body.short_description = 'body'

    def get_comment_count(self, obj):
        return obj.comments.count()

    get_comment_count.short_description = 'comments'

    list_display_links = (
        'id',
        'title',
        'get_body',
    )
    
    list_filter = (
        ('created_at', DateRangeFilter),
    )


@admin.register(Comment)
class CommmentModelAdmin(admin.ModelAdmin):
    fields = (
        'author',
        'post',
        'body',
        'created_at',
    )

    readonly_fields = (
        'get_body',
        'created_at',
    )

    list_display = (
        'id', 
        'author',
        'get_body',
        'post',
        'created_at',
    )

    list_display_links = (
        'id',
        'get_body',
    )

    search_fields = (
        'title',
        'get_body'
    )



    def get_body(self, obj):
        max_length = 70
        if len(obj.body) > max_length:
            return obj.body[:65] + ',,,'
        return obj.body




@admin.register(Reaction)
class ReactionModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'author',
        'post',
    )


admin.site.unregister(Group)
