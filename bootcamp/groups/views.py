from django.shortcuts import render
from .models import Group
from bootcamp.users.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView
from django.contrib import messages
from django.urls import reverse

# Create your views here.

class CreateGroupView(LoginRequiredMixin, CreateView):
    """Basic CreateView implementation to create new articles."""
    model = Group
    message = _("Your article has been created.")
    # form_class = ArticleForm
    fields = '__all__'
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
    context_object_name = "group"
    template_name = 'groups/group_detail.html'


def request_membership(request, pk):
    user = request.user
    group = Group.objects.get(pk=pk)
    if user in group.members:
        return False
    else:
        group.requests.add(user)
        return True

def request_handler(request, pk_u, pk_g):
    user = User.objects.get(pk=pk_u)
    group = Group.objects.get(pk=pk_g)

    group.requests.remove(user)
    group.members.add(user)
