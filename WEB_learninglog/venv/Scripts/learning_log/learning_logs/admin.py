from django.contrib import admin

# Register your models here.

# from learning_logs.models import Topic,Entry
#
# admin.site.register(Topic)
# admin.site.register(Entry)

from django.contrib import admin

from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)


# superuser 用户名：Z_admin   密码：123



