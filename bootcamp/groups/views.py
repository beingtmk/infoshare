from django.shortcuts import render
from .models import Group
from bootcamp.users.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.

class CreateGroupView(LoginRequiredMixin, CreateView):
    """Basic CreateView implementation to create new articles."""
    model = Group
    message = _("Your article has been created.")
    # form_class = ArticleForm
    fields = ('name', 'image', 'description', 'members')
    template_name = 'groups/group_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse('groups:list')

class GroupsListView(LoginRequiredMixin, ListView):
    """Basic ListView implementation to call the published articles list."""
    model = Group
    paginate_by = 15
    context_object_name = "groups"
    template_name = 'groups/group_list.html'

    def get_queryset(self, **kwargs):
        return Group.objects.all()

class GroupDetailView(LoginRequiredMixin, DetailView):
    """Basic DetailView implementation to call an individual article."""
    model = Group
    template_name = 'groups/group_detail.html'
    context_object_name = "group"

    def get_context_data(self, *args, **kwargs):
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        group = Group.objects.get(pk = self.kwargs.get('pk'))
        context['is_joined'] = False
        print(self.request.user)
        print(group.members.first)
        if self.request.user in group.members.all():
            context['is_joined'] = True
        print(context['is_joined'])
        return context

def request_membership(request, pk):
    user = request.user
    group = Group.objects.get(pk=pk)
    if user in group.requests.all():
        return HttpResponse('You have already a requested to be part of the group')
    else:
        group.requests.add(user)
        return HttpResponse('Your request has been registered')

def request_handler(request, pk):
    user = request.user
    group = Group.objects.get(pk=pk)

    group.requests.remove(user)
    group.members.add(user)
    return HttpResponse('Your approval has been saved to database')
