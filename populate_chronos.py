import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
    'Chronosal.settings')

import django

django.setup()

from chronos.models import Category, Task
from django.contrib.auth.models import User


def populate():

    user = User.objects.get(username='abinav')
    print(user)

    python_tasks = [
        'Complete Learn Python the Hardway',
        'Create a simple calculator'
    ]
        
    

    computer_tasks = [
        'Update roshi',
        'Finish 2520 Assignment',
        'Finish 2430 Assignment'
    ]
        
    

    cats = {
        'Python': python_tasks,
        'CIS': computer_tasks
    }


    for cat, tasks in cats.items():
        c = Category.objects.get_or_create(name=cat, user=user)[0]
        c.save()
        for task in tasks:
            t = Task.objects.get_or_create(name=task, category=c)[0]
            t.save()
            print('Adding ' + cat + ': ' + task + ' for user ' + str(user))
        


if __name__ == '__main__':
    print('Populating the Categories and Tasks Tables')
    populate()



