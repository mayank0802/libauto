from django.db import models
import datetime
class book_info(models.Model):
	book_id = models.AutoField(primary_key = True)
	book_name = models.CharField(max_length = 50)
	book_author = models.CharField(max_length = 50)
	bk_student_id = models.IntegerField(default = -1)
	book_submission = models.DateField(default=datetime.date.today)
	book_issue = models.DateField(default=datetime.date.today)
	def __str__(self): 
		return self.book_name