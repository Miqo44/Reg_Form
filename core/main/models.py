from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Category name', max_length=30)
    img = models.ImageField('Category image', upload_to='media')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Caregory'
        verbose_name_plural = 'Caregories'


class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='carcateg')
    name = models.CharField('Car name', max_length=50)
    about = models.TextField('Car about')
    img = models.ImageField('Car image', upload_to='media')
    price = models.IntegerField('Car price')
    history = models.TextField('Car history', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
