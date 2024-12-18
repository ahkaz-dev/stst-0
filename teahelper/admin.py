from django.contrib import admin
from .models import *

class RequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'contact_info', 'tea', 'pay_type')
    list_filter = ('user', 'address', 'tea', 'pay_type')
    search_fields = ('user__username', 'address', 'tea', 'pay_type', 'tea__name')
    
    fieldsets = (
        (None, {
            "fields": (
                ('user', 'address', 'contact_info', 'tea', 'pay_type')
            ),
        }),
    )
    
admin.site.register(Request, RequestAdmin)
admin.site.register(Tea)