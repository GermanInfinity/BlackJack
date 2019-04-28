from django.db import models

from djongo import models
from djongo.models import forms


class xts(models.Model):
	text = models.CharField(max_length=40)
	complete = models.BooleanField(default=False)
	class Meta: 
		abstract = True

class xts_contentForm(forms.ModelForm):
    class Meta:
    	model = xts
    	fields = ('text')

class xtsPost(models.Model):
	h1 = models.CharField(max_length=100)
	content = models.EmbeddedModelField(
					model_container=xts,
					model_form=xts_contentForm)