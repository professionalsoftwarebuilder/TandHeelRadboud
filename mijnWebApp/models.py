from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Man'),
        ('F', 'Vrouw'),
    )
    prf_User = models.OneToOneField(User,  on_delete=models.CASCADE, null=True, blank=True)
    prf_BirthDate = models.DateField('Geboortedatum', blank=True, null=True)
    prf_Gender = models.CharField('Geslacht', max_length=1, choices=GENDER_CHOICES)
    prf_DentalRating = models.IntegerField('Tandheelkundige beoordeling', default=0)

    def __str__(self):
        return self.prf_User.username


class PoetsMoment(models.Model):
    TYPE_TANDPASTA = (
        ('F', 'Met Fluor'),
        ('N', 'Normaal')
    )
    ACTIVITY_CHOICE = (
        ('P', 'Poetsen'),
        ('R', 'Raggen'),
        ('F', 'Flossen'),
        ('M', 'Mondwater')
    )
    ptm_User = models.ForeignKey(Profile, verbose_name='Bij Gebruiker', on_delete=models.CASCADE, default=1)
    ptm_Moment = models.DateTimeField('Poetsmoment', auto_now_add=True)
    ptm_Interval = models.DurationField('Poetsinterval', blank=True, null=True)
    ptm_Toothpaste = models.CharField('Type Tandpasta', max_length=1, choices=TYPE_TANDPASTA, default='F')
    ptm_Activity = models.CharField('Activiteit', max_length=1, choices=ACTIVITY_CHOICE, default='P')
    ptm_Notes = models.TextField('Notities', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'poetsmomenten'

    def __str__(self):
        return '%s %s' % (self.get_ptm_Activity_display(), self.ptm_Moment.strftime("%Y-%m-%d %H:%M"))

    def get_absolute_url(self):
        return reverse('mijnApp:list_PoetsMomenten', kwargs={'usr_id': self.ptm_User_id})
