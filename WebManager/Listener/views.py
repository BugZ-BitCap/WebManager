from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

########################## Error Listerners ###################
# Listens to errors in apache log for stacks that use apache as a virtual host
def listenErrorApache(request):
	a=request.GET.get("test")
	print a
	return HttpResponse("Received OK")


