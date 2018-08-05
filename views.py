from django.shortcuts import render
import datetime
from .models import User
import random


def output():
    sitetype = User.site_type

    # probabilistic algorithm here.

    # total number of visits
    a = User.objects.all().count()
    print(a)

    numberofostypes = User.objects.filter(name)

    # total_user = len(a.Objects.all())
    # print(inp.id)
    # print(inp.browser)
    # print(inp.os)
    # print(inp.device)
    # print(inp.site_type)
    # print(inp.present)

    return sitetype


# Create your views here.

def index(request):
    type = ["Electronics", "Fashion", "Furniture", "Chemical", "Ride"]

    # tem = loader.get_template('home/index.html')
    inp = User()
    inp.os = request.user_agent.os.family
    inp.device = request.user_agent.device.family
    inp.save()

    # inp.id = random.randrange(0, 100000000)
    # inp.browser = request.user_agent.browser.family
    # inp.present = datetime.datetime.now().strftime('%H:%M:%S')
    # inp.site_type = random.choice(type)

    out = output()

    info = {'output': out, }

    return render(request, 'home/index.html', info)
