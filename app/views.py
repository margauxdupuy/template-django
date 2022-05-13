from django.shortcuts import render

from django.views.generic import TemplateView



class TemplateDjangoView(TemplateView):
    template_name = 'hello.html'

    def get(self, request, *args, **kwargs):
        response = "Hello world"

        return render(request, 'hello.html', {'response': response})
