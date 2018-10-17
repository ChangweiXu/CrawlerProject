from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
'''
def index(request):
	return HttpResponse("The stats index page.")
# end def
'''
from stats.models import DailyData

import json

def index(request):
	'''
	raw_read = [60000000,50000000,40000000,80000000,60000000,90000000,70000000]
	raw_post = [3,2,4,5,6,3,2]
	# storeData()
	'''
	# get date list
	# TODO: use time.localtime(time.time()-i*86400)
	dateList = ['2018-09-03','2018-09-04','2018-09-05','2018-09-06','2018-09-07','2018-09-08','2018-09-09']
	repost = []
	comment = []
	story = []
	interact = []
	search = []
	mention = []
	mention_search = []
	send_blog_count = []
	blog_read_count = []
	give_flower_person_count = []
	give_flower_time = []
	close = []

	for date in dateList:
		##############################
		# 搜索语句
		##############################
		dd = DailyData.objects.all().filter(pub_date=date, nickname='紫宁')[0]
		# repost.append(dd.repost_num)
		# comment.append()
		# story.append()
		# interact.append()
		# search .append()
		# mention.append()
		# mention_search.append()
		send_blog_count.append(dd.blog_num)
		blog_read_count.append(dd.read_num)
		# give_flower_person_count.append()
		# give_flower_time.append()
		# close.append()
	# end for

	context = {
		'read_num': json.dumps(blog_read_count),
		'post_num': json.dumps(send_blog_count),
	}

	return render(request, 'stats/index.html', context)
# end def



def storeData(request):
	date = ['2018-09-03','2018-09-04','2018-09-05','2018-09-06','2018-09-07','2018-09-08','2018-09-09']
	repost = [743047,1131480,1234079,1407941,1145384,1449542,677931]
	comment = [387702,649746,911095,1159663,941717,1229476,578144]
	story = [0,0,0,15111,12193,0,3796]
	interact = [1130749,1781226,2145174,2582715,2099294,2679018,1259871]
	search = [2224,2440,2895,2810,2843,2468,2282]
	mention = [69120394,82365979,77544447,56927662,71106082,55905858,51192480]
	mention_search = [69122618,82368419,77547342,56930472,71108925,55908326,51194762]
	send_blog_count =[0,2,1,1,0,1,1]
	blog_read_count =[54129441,65338463,58859012,65844670,71226881,61778082,61220097]
	give_flower_person_count = [586,515,927,1491,516,476,397]
	give_flower_time = [722,619,1154,2144,723,579,450]
	close = [41716,45908,49628,59134,39314,25558,6248]

	list_to_insert = []

	for i in range(7):
		list_to_insert.append(DailyData(
					pub_date=date[i],
					nickname='紫宁',
		
					# total_score=0,
					# read_score=0,
					# interact_score=0,
					# social_score=0,
					# close_score=0,
		
					repost_num=repost[i],
					comment_num=comment[i],
					story_num=story[i],
					interact_num=interact[i],
					search_num=search[i],
		
					mention_num=mention[i],
					social_num=mention_search[i],
					blog_num=send_blog_count[i],
					read_num=blog_read_count[i],
		
					flower_people_num=give_flower_person_count[i],
					flower_count_num=give_flower_time[i],
					close_num=close[i]
			)
		)	
	# end for

	# DailyData.objects.bulk_create(list_to_insert)

	return HttpResponse("数据储存完毕！")

# end def
