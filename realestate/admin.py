from django.contrib import admin
from .models import Properties,Realtor,Top_properties,Blog,Whoweare,Allinone,Contact,whyus,About,Start


class PropertiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published', 'RentOrBuy','price', 'date', 'realtor')
    list_display_links = ('id','RentOrBuy', 'title', 'realtor')
    list_filter = ('realtor',)
    list_editable = ('published',)
    search_fields = ('title', 'decription', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 5

admin.site.register(Properties, PropertiesAdmin)




class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'hire_date')
    list_display_link = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'fname', 'lname', 'phone', 'email')
    list_display_links = ('id', 'fname', 'lname')
    search_fields = ('fname', 'lname', 'phone', 'email')
    list_per_page = 10


admin.site.register(Contact, ContactAdmin)

admin.site.register(Blog)
admin.site.register(Whoweare)
admin.site.register(Allinone)
admin.site.register(whyus)
admin.site.register(About)
admin.site.register(Start)
