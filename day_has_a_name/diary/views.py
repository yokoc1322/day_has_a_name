from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from . import forms, models

LOGIN_URL = reverse_lazy('diary:login')


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'diary/index.html'
    login_url = LOGIN_URL

    def get(self, request, *args, **kwargs):
        return redirect(reverse_lazy('diary:write'))


class WriterLoginView(LoginView):
    form_class = forms.WriterLoginForm
    template_name = 'diary/login.html'


class WriteView(LoginRequiredMixin, generic.FormView):
    template_name = 'diary/write.html'
    success_url = reverse_lazy('diary:index')
    form_class = forms.WriteForm
    login_url = LOGIN_URL

    def form_valid(self, form):
        writer = self.request.user
        content = form.cleaned_data['content']
        title = form.cleaned_data['title']
        date = form.cleaned_data['date']

        form.record(writer, content, title, date)
        return redirect(reverse_lazy('diary:index'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["old_records"] = models.Record.objects.filter().order_by('-date')
        return context


def error_400(request, exception=None):
    return render(request, 'diary/400.html')


def error_403(request, exception=None):
    return render(request, 'diary/403.html')


def error_404(request, exception=None):
    return render(request, 'diary/404.html')


def error_500(request, exception=None):
    return render(request, 'diary/500.html')
