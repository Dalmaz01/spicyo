from django.contrib import admin
from .models import (
    Category,
    Post,
    Recipes,
    Food
)
# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Recipes)
admin.site.register(Food)