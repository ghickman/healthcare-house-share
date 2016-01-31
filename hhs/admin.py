from django.contrib import admin

from .models import Contract, House, User

admin.site.register(Contract)
admin.site.register(House)
admin.site.register(User)
