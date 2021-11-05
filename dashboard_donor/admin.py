from django.contrib import admin
from .models import Notifications, Report, Response
from dashboard_pencari_donor.models import Donor

# Register your models here.
admin.site.register(Notifications)
admin.site.register(Report)
admin.site.register(Response)
admin.site.register(Donor)