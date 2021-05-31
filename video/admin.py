from django.contrib import admin
from .models import sport,motivation,stand_up
# Register your models here.
from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(sport, MyModelAdmin)
admin.site.register(motivation, MyModelAdmin)
admin.site.register(stand_up, MyModelAdmin)