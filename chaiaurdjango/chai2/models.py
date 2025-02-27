from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML','MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI')
    ]
    

    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="chais/")
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES, default='ML')
    description=models.TextField(default='')

    def __str__(self):
        return self.name


## 1. One-to-many relationship
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
# Here we have one ChaiVariety object and many ChaiReview objects

## 2. Many-to-many relationship
class Store(models.Model):
    name=models.CharField(max_length=100)
    locatotion = models.CharField(max_length=100)
    chai_varities = models.ManyToManyField(ChaiVariety, related_name="stores")

    def __str__(self):
        return self.name

# Here a Chai variety can be featured in multiple stores, and each store can feature multiple chai varieties.

## 3. One-to-one relationship   
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name="certificate")
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Certificate for {self.chai.name}'

# Here we have one ChaiVariety object and one ChaiCertificate object and each ChaiVariety object has one ChaiCertificate object


##### -> NOW REGISTER THE MODELS IN admin.py