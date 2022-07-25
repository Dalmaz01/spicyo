from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category')

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.CharField
    title = models.CharField(max_length=150, verbose_name='Title of post')
    image = models.ImageField(verbose_name='Image of post')
    text = models.TextField(verbose_name='Text')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_at = models.DateField(verbose_name='Date of create')

    def __str__(self):
        return self.title


class Recipes(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name of recipe')
    cook_time = models.IntegerField(default=0, verbose_name='Time of cooking')
    ingredients = models.TextField(verbose_name='Ingredients')
    directions = models.TextField(verbose_name='Directions')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name of food')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=150, verbose_name='Description')
    price = models.FloatField(verbose_name='price of food')
    rating = models.IntegerField(default=0, verbose_name='raiting')

    def __str__(self):
        return self.name
