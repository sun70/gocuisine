from django.db import models

# Create your models here.
class hotel_details_table(models.Model):
    hotel_name = models.CharField(max_length=500)
    hotel_address = models.CharField(max_length=800)
    rating = models.IntegerField(default=1)
    cab_available = models.CharField(max_length=10)
    review_count = models.IntegerField(default=0)
    special_reservation = models.CharField(max_length=10)
    hotel_environment = models.CharField(max_length=10)
    breakfast = models.CharField(max_length=10)
    lunch = models.CharField(max_length=10)
    dinner = models.CharField(max_length=10)
    image1 = models.ImageField(upload_to="")
    image2 = models.ImageField(upload_to="")
    image3 = models.ImageField(upload_to="")

    def __unicode__(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}"\
            .format(self.id,self.hotel_name ,self.hotel_address,self.rating,self.cab_available,self.review_count,self.review_count,
                    self.special_reservation,self.hotel_environment,self.breakfast,self.lunch,self.dinner,
                    self.image1,self.image2,self.image3)

class cab_book_table(models.Model):
    hotel_id  = models.ForeignKey('hotel_details_table')
    total_cab = models.IntegerField()
    available_cab = models.IntegerField()

    def __unicode__(self):
        return "{0},{1},{2}".format(self.id,self.available_cab,self.total_cab)


class reservation_table(models.Model):
    hotel_name = models.CharField(max_length=500)
    hotel_address = models.CharField(max_length=800)
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    email_address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    cab_required = models.CharField(max_length=10)
    cab_required_location = models.CharField(max_length=500)
    review = models.CharField(max_length=5000)
    check_in_time = models.DateTimeField()
    reservation_sts = models.CharField(max_length=100)
    special_reservation = models.CharField(max_length=500)
    no_of_person = models.IntegerField(default=1)
    username = models.CharField(max_length=100)

    def __unicode__(self):
        return  "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}"\
            .format(self.id,self.hotel_name,self.hotel_address,self.firstname,self.lastname,self.email_address,self.phone_number
                    ,self.cab_required,self.cab_required_location,self.review,self.check_in_time,self.reservation_sts
                    ,self.special_reservation,self.no_of_person,self.username)



