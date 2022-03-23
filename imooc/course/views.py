from django.shortcuts import render

from django.http import JsonResponse
from course import tasks

# Create your views here.
from course.tasks import CourseTask

def do(request):
    print("start to do request")
    # tk.CourseTask()
    # tk.delay()   #这种不成功
    ans = tasks.djtask.delay()

    print("task done")
    return JsonResponse({'result':'ok'})

def hello(request):
    return JsonResponse({'msg': 'Hello world'})
