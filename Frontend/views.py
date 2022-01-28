from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from MittaCutzz import settings
import os
from django.template import RequestContext
from Frontend import urls
from .models import prijzen, contact
from django.core.mail import send_mail

# Create your views here.



def makeMailMittacutzz(name, mail, sub, msg):
    data = {'name': name, 'mail': mail, 'sub': sub, 'msg': msg}
    MSG = '''
Webmail van:    {}
Mail adres :    {}

Message: 
{}
    '''.format(data['name'], data['mail'], data['msg'])
    contactForm = contact(name=name, email=mail, bericht=msg)
    contactForm.save()

    send_mail(data['sub'], MSG, 'webmail@mittacutzz.com', ['info@mittacutzz.com'],
              fail_silently=False, auth_user='webmail@mittacutzz.com', auth_password='ZweetSok070!')


def makeMailClient(mail):
    MSG = '''
Bedankt voor het invullen van ons contact formulier! Hierbij is bevestigd dat
wij uw mail ontvangen hebben. Wij zullen zo spoedig mogelijk contact met
u opnemen!
Vriendelijke groet,

mittacutzz.com
'''
    send_mail('Bevestiging WebForm mittacutzz', MSG, 'noreply@mittacutzz.com', [mail],
              fail_silently=False, auth_user='noreply@mittacutzz.com', auth_password='ZweetSok070!')

def indexView(request):
    homeSlidePath = settings.BASE_DIR / 'static/Frontend/IMG/Home-Slide'
    imgList = os.listdir(homeSlidePath)
    data = {
        'page': 'Frontend/home.html',
        'images': imgList,
        'imgCount': range(len(imgList)),
    }

    return render(request, 'Frontend/index.html', data)

def tarievenView(request):
    tarieven = prijzen.objects.all()
    data = {
        'page': 'Frontend/tarieven.html',
        'prijzen': tarieven,
    }

    return render(request, 'Frontend/index.html', data)

def contactView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        bericht = request.POST.get('bericht')
        makeMailMittacutzz(name, email, 'Contactformulier mittacutzz', bericht)
        makeMailClient(email)

        data = {
            'page': 'Frontend/contact-correct.html',
            'name': name,
        }
        return render(request, 'Frontend/index.html', data)

    else:

        data = {
            'page': 'Frontend/contact.html',
        }

        return render(request, 'Frontend/index.html', data)

def overMittacutzzView(request):
    data = {
        'page': 'Frontend/over-mittacutzz.html',
    }

    return render(request, 'Frontend/index.html', data)

def loginView(request):
    if request.method == 'POST' and 'login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/home')
            else:
                data = {
                    'page': 'registration/login.html',
                    'error': 'User account not activated',
                }
                return render(request, 'Frontend/index.html', data)
        else:
            data = {
                'page': 'registration/login.html',
                'error': 'Incorrect password and/or username',
            }
            return render(request, 'Frontend/index.html', data)

    data = {
        'page': 'registration/login.html',
        'error': '',
    }

    return render(request, 'Frontend/index.html', data)

def logoutView(request):
    logout(request)
    return redirect('Home')




def handler404(request, *args, **argv):
    if request.get_full_path != f"{path}":
        data = {
            'page': 'Frontend/404.html',
        }
        return render(request, 'Frontend/index.html', data)


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 499
    return response
