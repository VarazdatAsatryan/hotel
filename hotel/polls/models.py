from django.db import models

# Create your models here.

class Room(models.Model):
    SINGLE = 'Single'
    DOUBLE = 'Double'
    PRESIDENTAL = 'Presidental'
    ROOM_TYPE_CHOICE = [
        (SINGLE,'Single'),
        (DOUBLE,'Double'),
        (PRESIDENTAL,'Presidental')
    ]
    room_type = models.CharField(max_length=100,choices=ROOM_TYPE_CHOICE,null=True)

    def __str__(self):
        return self.room_type

class Hotel(models.Model):
    HOTEL_1 = 'Ani Plaza'
    HOTEL_2 = 'Tufenkian'
    HOTEL_3 = 'The Alexander'
    HOTEL_CHOICE = [
        (HOTEL_1,'Ani Plaza'),
        (HOTEL_2,'Tufnekian'),
        (HOTEL_3,'The Alexander')
    ]
    hotels = models.CharField(max_length=100,choices=HOTEL_CHOICE,null=True)

    def __str__(self) :
        return self.hotels
    
class Booking(models.Model):
    name = models.CharField(max_length=100)
    surename = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    room_type = models.ForeignKey(Room,on_delete=models.CASCADE, null=True)
    hotels = models.ForeignKey(Hotel,on_delete=models.CASCADE,null = True)

    def __str__(self):
        return f'{self.name} {self.surename}'
    