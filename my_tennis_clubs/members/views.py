from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

from .forms import NameForm


def members(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        forma = Member()
        forma.firstname = request.POST.get("firstname")
        forma.lastname = request.POST.get("lastname")
        forma.save()

        form = NameForm()
        mymembers = Member.objects.all().values()
        template = loader.get_template('all_members.html')
        context = {
          'mymembers': mymembers,
          'form':form,
        }

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        mymembers = Member.objects.all().values()
        template = loader.get_template('all_members.html')
        context = {
          'mymembers': mymembers,
          'form':form,
        }

    return HttpResponse(template.render(context, request))


def details(request, slug):
    mymember = Member.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['apple', 'orange']
    }
    return HttpResponse(template.render(context, request))
