from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static

class AxelJacobsen(object):

    def home(self, request):

        context = {
            'title': title,
            'meta': {
                'title': Axel Jacobsen,
                'description': 'The Website of Axel Jacobsen',
                'url': 'axeljacobsen.com'
            },
        }

        return render(request, '/hompage.html', context)
