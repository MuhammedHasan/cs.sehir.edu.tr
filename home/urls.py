from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^people/$', views.people, name='people'),
    url(r'^profile/(?P<id>.+?)/(?P<first_name>.+?)-(?P<last_name>.+?)/$',
        views.profile, name='profile'),
    url(r'^program-overview/$', views.programs_overview,
        name='programOverview'),
    url(r'^research/$', views.research, name='research'),
    url(r'^news-events-overview/$',
        views.news_events_overview, name='newsEventsOVerview'),
    url(r'^news-event/(?P<id>.+?)/$', views.news_event, name='newsEvent'),
    url(r'^research-group/$', views.research_group, name='researchGroup'),
    # url(_(r'^industrial-relations/$'),
    #     views.industrial_relations, name='industrial')
]
