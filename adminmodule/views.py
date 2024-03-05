from django.shortcuts import render

# Create your views here.
def projecthomepage(request):
    return render(request,'projecthomepage.html')

def employerhomepage(request):
    return render(request, 'employerhomepage.html')

def jobseekerhomepage(request):
    return render(request, 'jobseekerhomepage.html')

