""" 
class Cowsay(models.Model):
    input_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.input_text
"""

from django import forms

class CowsayAddForm(forms.Form):
    input_text = forms.CharField(max_length=100)
