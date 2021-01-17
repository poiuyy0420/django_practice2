from django.contrib import admin
from .models import Fcuser

# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('email', )

admin.site.register(Fcuser, FcuserAdmin)
admin.site.site_header = '캠퍼스'
admin.site.index_title = '캠퍼스'
admin.site.site_title = '캠퍼스'

