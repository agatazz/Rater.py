from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


# Create your models here.
class Service(models.Model):
    service_Name=models.CharField(max_length=200)
    description=models.TextField(max_length=360)

    def no_of_ratings(self):
        ratings =Rating.objects.filter(service=self)
        return len(ratings)
    def avg_rating(self):
        sum=0
        ratings = Rating.objects.filter(service=self)
        for rating in ratings:
            sum+=rating.stars
        if len(ratings) > 0:
           return sum / len(ratings)
        else:
            return 0
class Rating(models.Model):
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    class Meta:
        unique_together= (('user','service'),)
        index_together= (('user','service'),)