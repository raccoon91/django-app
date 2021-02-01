from django.shortcuts import render

posts = [
    {
        "author": "raccoon",
        "title": "blog post 1",
        "content": "first post content",
        "date_posted": "August 27, 2018",
    },
    {
        "author": "raccoon",
        "title": "blog post 2",
        "content": "second post content",
        "date_posted": "August 27, 2018",
    },
    {
        "author": "raccoon",
        "title": "blog post 3",
        "content": "third post content",
        "date_posted": "August 27, 2018",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
