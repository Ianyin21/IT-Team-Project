import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django

django.setup()
from rango.models import Category, Page


def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'https://pic.qqtn.com/up/2019-9/15690311636958128.jpg',
         'views': 1,
         'content': "nothing"},
        {'title': 'How to Think like a Computer Scientist',
         'url': 'https://pic.qqtn.com/up/2019-9/15690311636958128.jpg',
         'views': 2,
         'content': "nothing"},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'https://pic.qqtn.com/up/2019-9/15690311636958128.jpg',
         'views': 3,
         'content': "nothing"}]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://pic.qqtn.com/up/2019-9/15690311636958128.jpg',
         'views': 4,
         'content': "nothing"},

        {'title': 'Django Rocks',
         'url': 'https://pic.qqtn.com/up/2019-9/15690311636958128.jpg',
         'views': 5,
         'content': "nothing"},

        {'title': 'Nuvemshop, a Shopify Rival in Latin America, Valued at $2 Billion by Tiger Global',
         'url': 'https://tii.imgix.net/production/articles/6045/5ee60554-8471-43f1-a05a-05e68e2f08b9.jpeg?w=400&fm=webp&auto=compress',
         'views': 6,
         'content': "Nuvemshop, a Latin American e-commerce startup similar to Shopify, is raising a new round of funding led by Tiger Global Management that could value the company at $2 billion including the new capital, according to a person familiar with the matter."}]

    other_pages = [
        {'title': 'Amazon Installed Cameras to Track Drivers',
         'url': 'https://tii.imgix.net/production/articles/6035/989ee68c-e232-49c0-8e0e-e62dd488e8a3.jpg?w=400&fm=webp&auto=compress',
         'views': 7,
         'content': 'Amazon raised privacy hackles earlier this year with a plan to put high-tech video cameras in delivery vans to keep tabs on its drivers’ attention to safety. Now confidential documents viewed by The Information show how Amazon is using the devices to collect safety data about drivers that can affect the profits of the independent companies that employ them. The data can even determine whether drivers keep their jobs.'
         },

        {'title': 'SoftBank, Insight Top List of 10 Fastest-Growing Tech Investors',
         'url': 'https://tii.imgix.net/production/articles/6047/98e90547-0b19-4d5a-a74f-16b447063e48.jpg?w=400&fm=webp&auto=compress',
         'views': 8,
         'content': 'U.S. VC firms have raised $74 billion so far this year, nearly topping last year’s record of $81 '
                    'billion. At the current pace, the total raised will clear $100 billion for the first time this '
                    'year, according to PitchBook’s estimate. That’s nearly the total raised in 2011, 2012, '
                    '2013 and 2014 combined.'}]

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['content'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page(cat, title, url, content, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.content = content
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
