from django.contrib import admin
from .models import Advertisement

# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display=['title','description','user','price','created_date','updated_date', 'auction','mini_photo']
    list_filter=['auction','creation_date','update_date']
    actions=['forbid_the_auction','permit_the_auction']
    fieldsets=(
        ('Общее', {
            'fields':('title','description','category','user','photo')
        }),
        ('Финансы', {
            'fields':('price','auction'),
            'classes':['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def forbid_the_auction(self, request, queryset):
        queryset.update(auction=False)
        
    @admin.action(description='Добавить возможность торга')
    def permit_the_auction(self, request, queryset):
        queryset.update(auction=True)
        
    

admin.site.register(Advertisement, AdvertisementAdmin)