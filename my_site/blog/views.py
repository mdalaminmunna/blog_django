from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "bird",
        "images": "bird.jpg",
        "author": "Crazy",
        "date": date(2021, 7, 21),
        "title": "Ulubulu",
        "excert": "This is ulubulu!",
        "content": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Consectetur suscipit, corporis voluptatum tenetur necessitatibus assumenda quod vero totam repellat, quidem dolores repellendus nobis eos recusandae doloremque eum dolorem vel culpa?"
    },
    {
        "slug": "character",
        "images": "anime.png",
        "author": "Witch",
        "date": date(2021, 10, 12),
        "title": "Ulubulu",
        "excert": "This is ulubulu!",
        "content": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Consectetur suscipit, corporis voluptatum tenetur necessitatibus assumenda quod vero totam repellat, quidem dolores repellendus nobis eos recusandae doloremque eum dolorem vel culpa?"
    },
    {
        "slug": "panda",
        "images": "panda.jpg",
        "author": "Lazy",
        "date": date(2022, 2, 15),
        "title": "Ulubulu",
        "excert": "This is ulubulu!",
        "content": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Consectetur suscipit, corporis voluptatum tenetur necessitatibus assumenda quod vero totam repellat, quidem dolores repellendus nobis eos recusandae doloremque eum dolorem vel culpa?"
    }
]

def get_date(posts):
    return posts["date"]

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
