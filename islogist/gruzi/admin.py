from django.contrib import admin
from .models import SprMarka, Ttn, Schetopl, Actovipoln, Schetfact, Putlist, Dogovor, Zaiavka, Uchastnik, SprVidharts, \
    SprOrg, SprTovar, SprVidts, SprGruza, SprTipgruza, SprDolgn, SprUlici, SprGorod, SprSotr, Trsredstvo, SprModel, \
    Otchpodog

# Register your models here.


admin.site.register(SprMarka)
admin.site.register(SprModel)
admin.site.register(Trsredstvo)
admin.site.register(SprSotr)
admin.site.register(SprGorod)
admin.site.register(SprUlici)
admin.site.register(SprDolgn)
admin.site.register(SprTipgruza)
admin.site.register(SprGruza)
admin.site.register(SprVidts)
admin.site.register(SprTovar)
admin.site.register(SprOrg)
admin.site.register(SprVidharts)
admin.site.register(Uchastnik)
admin.site.register(Zaiavka)
admin.site.register(Dogovor)
admin.site.register(Putlist)
admin.site.register(Schetfact)
admin.site.register(Actovipoln)
admin.site.register(Schetopl)
admin.site.register(Ttn)
admin.site.register(Otchpodog)

