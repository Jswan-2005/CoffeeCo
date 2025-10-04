from django.db import models
from django.contrib.auth.models import User


class CoffeeType(models.Model):
    '''The type of coffee the user is recording about'''
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        verbose_name = "Coffee Type"

    def __str__(self):
        '''Return a string representation of the model'''
        return self.text

class CoffeeRecipeEntry(models.Model):
    '''A recipe for a chosen CoffeeType e.g (Latte Recipe)'''
    coffeeType = models.ForeignKey(CoffeeType, on_delete = models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Coffee Recipe Entries'

    def __str__(self):
        '''Return a string representation of the model'''
        return f"{self.text[:50]}"
