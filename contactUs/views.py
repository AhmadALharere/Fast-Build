from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import contact_link
# Create your views here.

def contact_us(request):

    ContactLink = contact_link.objects.first() 

    if request.method=='POST':
        subject = request.POST['subject']
        massage = request.POST['message']
        email = request.POST['email']
        
        mod_massage1 = f'new massage:\n\nfrom:\n{email}\n\nmassage:\n {massage}'
        mod_massage2 = f'hello {request.user.username},\n\n  you massage with subject:( {subject} ) has successfully sending to our supported team, we will see your email and send an answer in maximum 48h, thank you for your massage!!\n\n your massage: {massage} '
        
        send_mail(
			subject,
			mod_massage1,
			settings.EMAIL_HOST_USER,
			['almanym781@gmail.com'],
			fail_silently=False,
			)


        send_mail(
			subject,
			mod_massage2,
			settings.EMAIL_HOST_USER,
			[email],
			fail_silently=False,
			)
        
    return JsonResponse({"statues":"Done!!"})


