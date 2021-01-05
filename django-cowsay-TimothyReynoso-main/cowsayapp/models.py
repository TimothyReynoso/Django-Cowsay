from django.db import models

# Create your models here.


class Cowsay(models.Model):
    input_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.input_text