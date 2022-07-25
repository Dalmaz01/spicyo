from django.shortcuts import render

# Create your views here.


def about_page(request):
    print("request is accepted")
    return render(request, 'main/about.html', {})


def blog_page(request):
    return render(request, 'main/blog.html', {})


def contact_page(request):
    return render(request, 'main/contact.html', {})


def index_page(request):
    return render(request, 'main/index.html', {})


def recipe_page(request):
    return render(request, 'main/recipe.html', {})


def foods_page(request):
    return render(request, 'main/foods.html', {})
