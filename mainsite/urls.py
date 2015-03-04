from django.conf.urls import patterns, url
from mainsite.views import *

urlpatterns = patterns('',

		url(r'^watch/(?P<video_id>\d+)/$',watch_video,name='single video page'),
		url(r'^hot/$',hot,name='hot and trending videos'),
		url(r'^latest/$',latest,name='latest_videos'),
		url(r'^category/(?P<category>Laughs|Life|Music|Shocking!|Geeky)/$',category_wise,name='category wise videos in chronological order'),
		url(r'^$',home,name='website home page'),

)
