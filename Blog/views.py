from django.shortcuts import render

# Create your views here.
def blogs(request):
    return render(request, "pages/frontend/Blog/blog.html")


def post(request):
    return render(request, "pages/frontend/Blog/blog_details.html")
