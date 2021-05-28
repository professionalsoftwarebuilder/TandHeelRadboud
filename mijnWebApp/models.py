from django.db import models

class Artikel(models.Model):
    art_Nm = models.CharField('Artikel naam', max_length=85)
    art_Omschr = models.TextField('Omschrijving', blank=True, null=True)
    art_Image = models.ImageField('Afbeelding', max_length=250, blank=True, null=True)
    art_Prijs = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True)

    class Meta:
        verbose_name_plural = 'artikelen'

    def __str__(self):
        return str(self.art_Nm) + ": €" + str(self.art_Prijs)


class PoetsMoment(models.Model):
    ptm_Moment = models.DateTimeField('Poetsmoment', auto_now_add=True)
    ptm_Interval = models.DurationField('Poetsinterval', null=True)
