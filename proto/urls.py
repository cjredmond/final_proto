from django.conf.urls import url, include
from django.contrib import admin
from app.views import IndexView, TeamUpdateView, LeagueDetailView, LeagueCreateView, \
                      SquadDetailView, UserCreateView, LeagueUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index_view",),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^team/(?P<pk>\d+)/draft/$', TeamUpdateView.as_view(), name="team_update_view"),
    url(r'^league/(?P<pk>\d+)/home/$', LeagueDetailView.as_view(), name="league_detail_view"),
    url(r'^league/(?P<pk>\d+)/start/$', LeagueUpdateView.as_view(), name="league_update_view"),
    url(r'^league/create/$', LeagueCreateView.as_view(), name="league_create_view"),
    url(r'^squad/(?P<pk>\d+)/$', SquadDetailView.as_view(), name="squad_detail_view")
]
