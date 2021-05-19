from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class studmarks(models.Model):
    name = models.CharField(max_length=50, default="")
    roll = models.IntegerField()
    math = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    phy = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    chem = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    total = models.IntegerField()
    percentage=models.DecimalField(max_digits=5,decimal_places=2,)

    def save(self):
        self.total= int(self.math) + int(self.phy) + int(self.chem)
        self.percentage=float(self.total/300)*100
        return super(studmarks, self).save()

    def __str__(self):
        return self.name

 

