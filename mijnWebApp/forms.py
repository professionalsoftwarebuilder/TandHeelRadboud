from django import forms
from django.forms.fields import DurationField

from .models import *
from django.forms.widgets import TextInput
from django.utils.dateparse import parse_duration
from datetime import datetime, timezone, timedelta
from django.utils.duration import _get_duration_components


class DurationInput(TextInput):

    def _format_value(self, value):
        duration = parse_duration(value)

        seconds = duration.seconds

        hours = 0
        remseconds = 0

        if seconds > 3600:
            # Floor division
            hours = seconds // 3600

            # Remaining seconds
            remseconds = seconds % 3600
        else:
            remseconds = seconds
            minutes = remseconds // 60
            remseconds = remseconds % 60

        return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, remseconds)





def duration_string(duration):
    # Removing the milliseconds of the duration field
    days = duration.days
    seconds = duration.seconds
    microseconds = duration.microseconds

    minutes = seconds // 60
    seconds = seconds % 60

    hours = minutes // 60
    minutes = minutes % 60

    string = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
    if days:
        string = '{} '.format(days) + string
    # if microseconds:
    #     string += '.{:06d}'.format(microseconds)

    return string


# class CustomDurationField(forms.DurationField):
#     def prepare_value(self, value):
#         if isinstance(value, timedelta):
#             return duration_string(value)
#         return value
#


class CustomDurationField(DurationField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val is None:
            return ''

        days, hours, minutes, seconds, microseconds = _get_duration_components(val)
        return '{} days, {:02d} hours, {:02d} minutes'.format(
            days, hours, minutes)




class PoetsMomentForm(forms.ModelForm):
    #work_time_interval = CustomDurationField()

    class Meta:
        model = PoetsMoment
        fields = '__all__'
        #fields = ['ptm_Interval', 'ptm_Toothpaste', 'ptm_Activity', 'ptm_Notes']
        #widgets = {'ptm_Interval': CustomDurationField()}
        #widgets = {'ptm_Interval': DurationInput()}
