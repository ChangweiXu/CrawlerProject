from django.db import models

# Create your models here.

class DailyData(models.Model):
	pub_date = models.DateField('日期')
	nickname = models.CharField(max_length=10)

	# total_score = models.FloatField(default=0) # '总分'
	# read_score = models.FloatField(default=0) # '阅读数'
	# interact_score = models.FloatField(default=0) # '互动数'
	# social_score = models.FloatField(default=0) # '社会影响力'
	# close_score = models.FloatField(default=0) # '爱慕值'

	repost_num = models.IntegerField(default=0) # '转发数量'
	comment_num = models.IntegerField(default=0) # '评论数量'
	story_num = models.IntegerField(default=0) # '故事互动'
	interact_num = models.IntegerField(default=0) # '互动数量'
	search_num = models.IntegerField(default=0) # '搜索数量'

	mention_num = models.IntegerField(default=0) # '@数量'
	social_num = models.IntegerField(default=0) # '社会影响力数量'
	blog_num = models.IntegerField(default=0) # '发微博数量'
	read_num = models.IntegerField(default=0) # '阅读数量'

	flower_people_num = models.IntegerField(default=0) # '送花人数量'
	flower_count_num = models.IntegerField(default=0) # '送花次数量'
	close_num = models.IntegerField(default=0) # '爱慕值量'

	def __str__(self):
		return self.nickname
	# end def

# end class
