from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static

class HomePage(object):

    def home(self, request):

        context = {
            'meta': {
                'title': 'Axel Jacobsen',
                'description': 'The Website of Axel Jacobsen',
                'url': 'axeljacobsen.com'
            },
        }

        return render(request, 'homepage.html', context)