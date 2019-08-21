from django.db import models

# Create your models here.

class Aigo(models.Model):
    message = models.CharField(max_length=100)
    # date = models.DateTimeField(auto_now=True)
    # ID = models.IntegerField(primary_key=True)
    # class Meta:
    #     db_table = 'test'
    #     managed = False

    def __str__(self):
        return self.message