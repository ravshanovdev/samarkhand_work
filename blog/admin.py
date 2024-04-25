from django.contrib import admin
from .models import MyResume, Test, Variants


admin.site.register([MyResume, Test, Variants])



