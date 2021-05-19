from django.contrib import admin
from .models import studmarks


# Register your models here.
class studmarksAdmin(admin.ModelAdmin):
    list_display = ("name", "roll","math","phy","chem","total","percentage")


admin.site.register(studmarks,studmarksAdmin)
