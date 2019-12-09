from django.db import models
from django.contrib.auth.models import User  


class UserProfile(models.Model):  
  
    age = models.IntegerField()  
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')


class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    def __str__(self):  
        return self.full_name


class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    copy_count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    redaction = models.ForeignKey('Redaction', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    book_img = models.ImageField(upload_to='media/%Y/%m/%d', blank=True)

# 
    borrower = models.ManyToManyField(
        'Friend',
        through='Rent',
        through_fields=('book', 'friend'),
        )

    can_be_borrowed = models.IntegerField(default=0)
# 


    def __str__(self):  
        return self.title


class Redaction(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

# ------------------------------------------------------------

class Friend(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Rent(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    num = models.IntegerField(default=1)