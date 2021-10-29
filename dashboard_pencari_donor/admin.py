from django.contrib import admin
from .models import Notifications, Report, Response

# Register your models here.
admin.site.register(Notifications)
admin.site.register(Report)
admin.site.register(Response)