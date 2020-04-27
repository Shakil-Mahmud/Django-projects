from django import forms
from .models import TicketPrice
from .models import Train
from .models import Booking
from .models import Station
from django.forms import ModelForm


class TicketPriceForm(forms.ModelForm):
	test = forms.CharField(max_length=60)
	class Meta:
		model = TicketPrice
		fields= ['test', 'train', 'sourceStation', 'destStation']


class ScheduleForm(forms.Form):
	class Meta:
		model = Train
		fields= ['train_name']

class BookingForm(forms.Form):
	sourceStation = forms.ModelMultipleChoiceField(queryset = Station.objects.all())

