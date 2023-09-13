from django.contrib import admin
from .models import login, user_page,report

# Register your models here.

admin.site.register(login)
admin.site.register(user_page)
admin.site.register(report)
