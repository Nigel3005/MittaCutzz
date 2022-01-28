from django.db import models
# from djangoratings.fields import RatingField

class prijzen(models.Model):
    titel = models.CharField(max_length=200, default="Heren", unique=True)
    betaalWijze = [
        ('Contant', 'Contant'),
        ('Pin', 'Pin'),
        ('Pin of Contant', 'pin of Contant'),
    ]
    betaalWijze = models.CharField(max_length=20, choices=betaalWijze, default='Contant')

    extra = [
        ('Andere betaal wijze niet toegestaan', 'Andere betaal wijze niet toegestaan'),
        ('Andere betaal wijze toegestaan', 'Andere betaal wijze toegestaan'),
    ]
    extra = models.CharField(max_length=255, choices=extra, default='Andere betaal wijze niet toegestaan')

    vasteKlantPrijs = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    nieuweKlantPrijs = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    contourPrijs = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    tondeusePrijs = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    baardPrijs = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    waxPrijs = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.titel

    class Meta:
        verbose_name_plural = "Prijzen"


class contact(models.Model):
    name = models.CharField(max_length=200, default=" ")
    email = models.EmailField(max_length=200, default=" ")
    bericht = models.TextField(max_length=200, default=" ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact"




# class reacties(models.Model):
#     Naam = models.CharField(max_length=20, help_text='Name of the person', default='')
#     Email = models.CharField(max_length=100, help_text='Email of the person', default='')
#     reactie = models.CharField(max_length=200, help_text='Reactie', default='')
#     reactie_date = models.DateTimeField(auto_now_add=True)
#     Akkoord = models.BooleanField(help_text='Privacy akkoord', default=False)
#
#     def __str__(self):
#         return self.Naam
#
#     class Meta:
#         verbose_name_plural = "Reacties"



# class RatingField(models.Model):
#     rating = RatingField(range=10, weight=10) # 10 possible rating values, 1-10
