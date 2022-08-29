from django.contrib import admin
from import_export.admin import ExportMixin

from .models import Glucose, UserProfile


class GlucoseImportExport(ExportMixin, admin.ModelAdmin):
    model = Glucose

    list_display = [
        "id",
        "user",
        "gerät",
        "seriennummer",
        "aufzeichnungstyp",
        "glukosewert",
        "gerätezeitstempel",
    ]


admin.site.register(Glucose, GlucoseImportExport)
admin.site.register(UserProfile)
