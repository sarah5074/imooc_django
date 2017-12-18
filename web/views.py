from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import json
def Login(request):
    if request.method == 'POST' :
        result = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        #data = request.GET.get('data')
        result['user'] = username
        result['password'] = password
        #result['data'] = data
        result = json.dumps(result)
        return HttpResponse(result,content_type='application/json;charset=utf-8')
    else:
        return render_to_response('login.html')


def index(request):
    if request.method == 'GET':
        return render_to_response('index.html')
        #return HttpResponse("对不起，请加上参数来访问")
