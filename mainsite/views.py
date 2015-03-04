from models import *
from django.template import RequestContext 
from django.shortcuts import render_to_response
from mainsite.models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import random
import datetime
from django.utils import timezone
#------------------------------------------------------------------------------ big hack

default_video = Video.objects.get(id=1)



def latest_books(request,template = 'latest_books.html',
				  page_template = 'latest_books_page.html' ):

	handpicked_videos = HandpickedVideo.objects.all()
	context = {'handpicked_videos':handpicked_videos}    
	book_list = BadaTest.objects.all()

	context.update( {'book_list': book_list, 'page_template': page_template,} )

	# override the template and use the 'page' style instead.
	if request.is_ajax():
		template = page_template

	return render_to_response(
		template, context, context_instance=RequestContext(request) )

def similar_content(display_video):
	display_video_tags = display_video.tags.all()
	all_related = []
	for x in display_video_tags:
		for y in x.video_set.all():
			if y not in all_related and y != display_video:
				all_related.append(y)

	all_related = list(set(all_related))
	if len(all_related) >=4:
		return random.sample(all_related,4)
	else:
		return all_related
def hot_videos(display_video):
	#returns 6 videos
	videos_by_votes = Video.objects.all().order_by('-votes')
	six_hot_videos = []
	for x in videos_by_votes:
		if x.was_published_recently() and x != display_video:
			six_hot_videos.append(x)
		if len(six_hot_videos) >= 6:
			break
	return six_hot_videos

def latest_videos(display_video):
	all_videos = Video.objects.all().order_by('-pub_date')
	if len(all_videos)>=15:
		return random.sample(all_videos[:15],4) 
	else:
		return random.sample(all_videos[:],4) 
	 

def watch_video(request,video_id):
	try:
		display_video = Video.objects.get(id=video_id)
	except:
		return HttpResponse('Video Not Found') #Generate proper error page
	related_videos = similar_content(display_video)
	hot_videos_list = hot_videos(display_video)
	return render_to_response('watch.html', {'display_video':display_video,'related_videos':related_videos,'hot_videos_list1':hot_videos_list[:3],'hot_videos_list2':hot_videos_list[3:]}, RequestContext(request))

def home(request):
	temp = latest_videos(default_video)
	latest_videos_list = temp[1:]
	first_latest = temp[0]
	hot_videos_list = hot_videos(default_video)[:3]
	handpicked_videos = [x.video for x in HandpickedVideo.objects.all()]
	return render_to_response('home.html', {'handpicked_videos':handpicked_videos, 'first_latest':first_latest,'latest_videos_list':latest_videos_list,'hot_videos_list':hot_videos_list}, RequestContext(request))

def category_wise(request,category,template = 'category_base.html',
				  page_template = 'category_content.html' ):

	hot_videos_list = hot_videos(default_video)[:4]
	context = {'hot_videos_list':hot_videos_list, 'category_selected':category}
	try:
		category_selected = Category.objects.get(name=category)
	except:
		return HttpResponse('Invalid Video Category') #Create Proper error page    
	video_list = category_selected.video_set.all().order_by('-pub_date')

	context.update( {'video_list': video_list, 'page_template': page_template,} )

	# override the template and use the 'page' style instead.
	if request.is_ajax():
		template = page_template

	return render_to_response(template, context, context_instance=RequestContext(request))

def hot(request,template = 'category_base.html',
				  page_template = 'category_content.html' ):

	hot_videos_list = latest_videos(default_video)
	context = {'hot_videos_list':hot_videos_list, 'category_selected':'Hot & Trending'}
	videos_by_votes = Video.objects.all().order_by('-votes')
	video_list = []
	for x in videos_by_votes:
		if x.was_published_recently():
			video_list.append(x)

	context.update( {'video_list': video_list, 'page_template': page_template,} )

	# override the template and use the 'page' style instead.
	if request.is_ajax():
		template = page_template

	return render_to_response(template, context, context_instance=RequestContext(request) )

def latest(request,template = 'category_base.html',
				  page_template = 'category_content.html' ):
	hot_videos_list = hot_videos(default_video)[:4]
	context = {'hot_videos_list':hot_videos_list, 'category_selected':'The Latest Buzz'}   
	video_list = Video.objects.all().order_by('-pub_date')

	context.update( {'video_list': video_list, 'page_template': page_template,} )

	# override the template and use the 'page' style instead.
	if request.is_ajax():
		template = page_template

	return render_to_response(template, context, context_instance=RequestContext(request) )