import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django

django.setup()

import random
from first_app.models import WebPage, AccessRecord, Topic
from faker import Faker

fakegen = Faker()
topics = ['Games', 'Education', 'MarketPlace', 'News']


def add_topic():
    topic = Topic.objects.get_or_create(Name=random.choice(topics))[0]
    topic.save()
    return topic

def populate(N=5):
    for i in range(1,N):
        topic = add_topic()
        name = fakegen.company()
        url = fakegen.url()
        date = fakegen.date()
        webpage = WebPage.objects.get_or_create(Name=name,Url=url,Topic=topic)[0]
        accessRecord = AccessRecord.objects.get_or_create(Date=date,WebPage=webpage)[0]



if __name__  == '__main__':
    populate(20)
