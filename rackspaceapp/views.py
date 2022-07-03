from django.shortcuts import render
from django.contrib import messages
from .forms import TimezoneForm
import requests
import json



# Create your views here.
"""
Get matching records
:jsondata : Dataset value which is JSON object
:requiredValue : String value for seaching the Matching records
"""
def getMatch(jsondata,requiredValue):
    timezoneText = None
    for timeZone in jsondata:
        if requiredValue in timeZone["value"]:
            timezoneText = str(timeZone['text'])
            break
    return timezoneText

"""
Get offset records
:jsondata : Dataset value which is JSON object
:requiredValue : String value for seaching the offset records
"""
def getOffset(jsondata,requiredValue):
    timezoneText = None
    for timeZone in jsondata:
        if float(requiredValue) == timeZone["offset"]:
            timezoneText = str(timeZone['text'])
            break
    return timezoneText


"""
index funcation is the default page for Django
:request : handling the request
"""
def index(request):
    response = requests.get('https://raw.githubusercontent.com/dmfilipenko/timezones.json/master/timezones.json').json()
    jsonData = response
    fm = TimezoneForm()
    applyFilter,searchString = '',''
    matchValue,offsetValue = '',''
    # return render(request,'rackspaceapp/timezone.html',{'filterForm':fm})
    if request.method=='POST':
        form = TimezoneForm(request.POST)
        if form.is_valid():
            filterType = form.cleaned_data.get('filterType')
            searchString = form.cleaned_data['searchString']
            if 'match' in filterType:
                try:
                    matchValue = getMatch(jsonData,searchString)
                    if matchValue is not None:
                        messages.info(request,matchValue)
                    else:
                        messages.info(request,f"matching record not found : {searchString}")
                except Exception as e:
                    messages.error(request,f"Exception in getting the match value : {e}")
            elif 'offset' in filterType:
                try:
                    offsetValue = getOffset(jsonData,searchString)
                    if offsetValue is not None:
                        messages.info(request,offsetValue)
                    else:
                        messages.info(request,f"offset record not found : {searchString}")
                except Exception as e:
                    messages.error(request,f"Exception in getting the offset value : {e}")
    return render(request,'rackspaceapp/home.html',{'response':response,'filterForm':fm})
