from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from .forms import PageForm
from django.http import HttpResponseRedirect

from wiki.models import Page


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })

class NewWikiView(CreateView):
    model = Page

    def get(self, request):
        form = PageForm()
        context = {'form': form,}
        return render(request, "new_wiki.html", context)

    def post(self, request):
        if request.method == "POST":
            form = PageForm(request.POST)
            if form.is_valid():
                # wiki.title  = request.POST.get('title', '')
                # wiki.slug = request.POST.get('slug', '')
                # wiki.content = request.POST.get('content', '')
                # wiki.modified = request.POST.get('modified', '')
                wiki = form.save()

                txt_message = wiki.title+" has been successfully created"
                # messages.success(request, txt_message)

                return render(request, 'page.html', {'page': wiki})
            else:

                errors = "Wiki was not created"
                # messages.error(request, errors, extra_tags='alert')
        else:
            form = PageForm()

        context = {'form': form}

        return render(request, 'wiki/page.html', context)
