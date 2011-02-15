from django.conf.urls.defaults import *
from polls.models import Poll

info_dict = {
    'queryset': Poll.objects.all(),
}

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', info_dict, name="list"),
	url(r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict, name="detail"),
	url(r'^(?P<object_id>\d+)/results/$', 'django.views.generic.list_detail.object_detail', dict(info_dict, template_name='polls/results.html'), name='results'),
	url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote', name="vote"),
)
