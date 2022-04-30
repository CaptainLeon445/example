from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(Request):
    return HttpResponse('''<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>My Second App</title>
  </head>
  <body>
    <em>My Second App</em>
  </body>
</html>''')

def help(Request):
    my_dict={"Insert_Me":"I am from Help.Page"}
    return render(Request,'AppTwo/help.html',context=my_dict)