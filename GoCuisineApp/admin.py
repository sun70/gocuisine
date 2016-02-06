from django.contrib import admin

# Register your models here.
from GoCuisineApp.models import hotel_details_table, cab_book_table, reservation_table

class HotelView(admin.ModelAdmin):
    list_display = ('hotel_name','hotel_address','rating','cab_available','review_count','special_reservation',
                    'hotel_environment', 'breakfast','lunch','dinner','image1','image2','image3')


class ReservationView(admin.ModelAdmin):
    list_display = ('hotel_name','hotel_address','firstname','lastname','email_address','phone_number','cab_required',
                    'cab_required_location','review','check_in_time','reservation_sts','special_reservation','no_of_person','username')

class CabView(admin.ModelAdmin):
    list_display = ('id','total_cab','available_cab')

admin.site.register(hotel_details_table, HotelView)
admin.site.register(cab_book_table,CabView)
admin.site.register(reservation_table,ReservationView)