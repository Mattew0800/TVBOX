from django.contrib import admin
from .models import Canal10,Canal26,C5N,TN,LN,DTV,Cronica,Telefe,TVP

# Register your models here.


class Canal10_Admin(admin.ModelAdmin):
    pass
class Canal26_Admin(admin.ModelAdmin):
    pass
class C5N_Admin(admin.ModelAdmin):
    pass

class Cronica_Admin(admin.ModelAdmin):
    pass

class DTV_Admin(admin.ModelAdmin):
    pass
class LN_Admin(admin.ModelAdmin):
    pass
class Telefe_Admin(admin.ModelAdmin):
    pass
class TN_Admin(admin.ModelAdmin):
    pass
class TVP_Admin(admin.ModelAdmin):
    pass

admin.site.register(Canal10, Canal10_Admin)
admin.site.register(Canal26, Canal26_Admin)
admin.site.register(TN, TN_Admin)
admin.site.register(TVP, TVP_Admin)
admin.site.register(C5N, C5N_Admin)
admin.site.register(Telefe, Telefe_Admin)
admin.site.register(LN, LN_Admin)
admin.site.register(DTV, DTV_Admin)
admin.site.register(Cronica, Cronica_Admin)
