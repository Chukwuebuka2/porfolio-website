from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import About, Home, Profiles, Category
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def index(request):

    # This brings the latest home info
    home = Home.objects.latest("updated")

    # This brings the lastest about
    about = About.objects.latest("updated")

    # the profile section ensures that it is up to date 
    profiles = Profiles.objects.filter(about=about)

    # for the categories
    categories = Category.objects.all()

    

    # To handle the sending of mails 
    if request.method == 'POST':
        # get the details for the email

        # name of sender
        full_name = request.POST.get("full_name")

        # email of sender
        email = request.POST.get("email")

        # message
        message = request.POST.get("message")

        if full_name and message and email:
            try:
                send_mail(
                    subject='A message from ' + full_name, 
                    message=message, 
                    from_email=email, 
                    recipient_list=['nwokporochukwuebuka@gmail.com']
                )

                # handle possible error messages
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return HttpResponseRedirect('/')
        
        else:
            return HttpResponse("Make sure all fields entered are valid.")


    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        # 'full_name': full_name
    }

    return render(request=request, template_name='index.html', context=context)