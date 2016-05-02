from django.shortcuts import render

def footer_email(request):
    return render(request, 'footer_email/base.html')
