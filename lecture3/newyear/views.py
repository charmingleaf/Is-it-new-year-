from django.shortcuts import render
from datetime import date
today = date.today()
# Create your views here.
def newyear(request):
    
    if today.month == 4 and today.day == 14:
        return render(request, "newyear/yes.html")
    else :
        return render(request, "newyear/no.html")

