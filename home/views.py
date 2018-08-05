from django.shortcuts import render
import datetime
from . import models


# Create your views here.
def index(request):
    # tem = loader.get_template('home/index.html')
    browser = request.user_agent.browser.family
    os = request.user_agent.os.family
    device = request.user_agent.device.family
    present = datetime.datetime.now().strftime('%H:%M:%S')

    info = {'browser': browser,
            'os': os,
            'device': device,
            'time': present,
            }
    return render(request, 'home/index.html', info)

def output(request):
    a = models.User()

    total_user = len(a.Objects.all())



