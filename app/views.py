from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from app.models import Team, Squad, League, Schedule
from django.urls import reverse, reverse_lazy

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        leagues = League.objects.all()
        context['leagues'] = leagues
        return context

class TeamUpdateView(UpdateView):
    model = Team
    fields = []
    def get_success_url(self, **kwargs):
        return reverse_lazy('squad_detail_view', args=str(self.request.user.squad.id))
    def form_valid(self, form):
        instance = form.save(commit=False)
        if instance.squad == self.request.user.squad:
            instance.squad = None
        else:
            instance.squad = self.request.user.squad
        return super().form_valid(form)

class LeagueDetailView(DetailView):
    model = League
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        baseball = Team.objects.filter(sport="b", league=self.kwargs['pk'])
        football = Team.objects.filter(sport="f", league=self.kwargs['pk'])
        basketball = Team.objects.filter(sport="k", league=self.kwargs['pk'])
        squads = Squad.objects.filter(league=self.kwargs['pk'])
        context['schedule'] = Schedule.objects.get(league=self.kwargs['pk'])
        context['squads'] = squads
        context['standings'] = sorted(squads, key=lambda t: -t.total_proj)
        context['baseball'] = baseball
        context['football'] = football
        context['basketball'] = basketball
        return context

class LeagueCreateView(CreateView):
    model = League
    success_url = "/"
    fields = ("name","limit")
    def form_valid(self, form):
        instance = form.save(commit=False)
        #teams = Team.objects.all()
        #for team in teams:
            #Team.objects.create(city=team.city, name=team.name, league=instance, sport=team.sport, pts_last=team.pts_last, pts_proj=team.pts_proj)
        return super().form_valid(form)

class LeagueUpdateView(UpdateView):
    model = League
    success_url = "/"
    fields = []
    def form_valid(self, form):
        instance = form.save(commit=False)
        target = League.objects.get(id=self.kwargs['pk'])
        instance.live = True
        Schedule.objects.create(league=target)
        return super().form_valid(form)


class SquadDetailView(DetailView):
    model = Squad
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        target = Squad.objects.get(id=self.kwargs['pk'])
        baseball = Team.objects.filter(sport="b", league=target.league, squad=None)
        football = Team.objects.filter(sport="f", league=target.league, squad=None)
        basketball = Team.objects.filter(sport="k", league=target.league, squad=None)
        your_teams = Team.objects.filter(squad = target)
        context['baseball_checker'] = target.checker('b')
        context['football_checker'] = target.checker('f')
        context['basketball_checker'] = target.checker('k')
        context['your_teams'] = your_teams
        context['baseball'] = baseball.order_by('-pts_proj')
        context['football'] = football.order_by('-pts_proj')
        context['basketball'] = basketball.order_by('-pts_proj')
        return context
