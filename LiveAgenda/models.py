from django.db import models


class appointment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    # appointment_id = models.CharField(max_length=20, default='', unique=True)
    Naam = models.CharField(max_length=20, help_text='Name of the person', default='')
    Achternaam = models.CharField(max_length=20, help_text='Surname of the person', default='')
    Nummer = models.CharField(null=True, max_length=20, help_text='Contact phone number', default='+31 6')

    TIME_CHOICES = [
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
    ]

    OTHER_CHOICES = [
        ('ALLEEN HAAR', 'ALLEEN HAAR'),
        ('ALLEEN BAARD', 'ALLEEN BAARD'),
        ('HAAR + BAARD', 'HAAR + BAARD'),
    ]

    ANONIEM_CHOICE = [
        ('JA', 'JA'),
        ('NEE', 'NEE'),
        ]

    Tijd = models.CharField(max_length=20, choices=TIME_CHOICES, default='11:00', unique=True)
    keuze = models.CharField(max_length=20, choices=OTHER_CHOICES, default='ALLEEN HAAR')
    anoniem = models.CharField(max_length=20, choices=ANONIEM_CHOICE, default='NEE')


    def __str__(self):
        return self.Naam


    class Meta:
        verbose_name_plural = "appointments"
