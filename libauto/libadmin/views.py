from django.shortcuts import render
from libadmin.models import book_info
# Create your views here.
import datetime
def bkinfo(request):
	if request.method == 'POST':
		book_author = request.POST.get('book_author','')
		book_name = request.POST.get("book_name", '')
#		print(book_name)
		book_infos = book_info(book_author = book_author, book_name = book_name)
		book_infos.save()
	return render(request,'new_book.html')
def bk_issue(request):
	if request.method == 'POST':
		book_id = request.POST.get('book_id','')
		book_stud_id = request.POST.get("student_id", '')
		book = book_info.objects.get(book_id = book_id)
		print(book)
		book.bk_student_id = book_stud_id
		today = datetime.date.today()
		book.bk_issue = today
		book.book_submission = today + datetime.timedelta(days = 7)
		book.save()	
	return render(request, 'bkinfo.html')
def retrn(request):
	if request.method=='POST':
		book_id=request.POST.get('book_id','')
		book_stud_id = request.POST.get("student_id", '')
		book = book_info.objects.get(book_id = book_id)
		print(book)
		book.bk_student_id = -1
		today = datetime.date.today()
		book.bk_issue = today
		book.book_submission = today
		book.save()
	return render(request, 'return.html')
		



