from django.shortcuts import render

# Create your views here.

import time
from django.shortcuts import render
from django.http import HttpResponse
import time



def fibonacci(request):
	return render(request,'Home.html',{'name' : 'Fibonacci Series'})
def add(request):
	start_time = float(time.time())
	val1 = int(request.GET["num1"])

	l=[]
	for i in range(val1+1):
		if i>1:
			l.append(l[i-2]+[i-1])
		else:
			l.append(i)
	res = l[-1]
	time_res = time.time() - start_time
	return render(request,'result.html',{'result':res,'time':time_res})


