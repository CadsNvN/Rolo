from django.contrib import admin
from .models import Profile, Garment, Schedule, Payment

admin.site.register(Profile)
admin.site.register(Garment)
admin.site.register(Schedule)
admin.site.register(Payment)
