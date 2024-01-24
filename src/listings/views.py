from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from listings.models import Band, Listing
from listings.forms import ContactForm
from listings.forms import BandForm
from django.core.mail import send_mail

# Create your views here.

# get all band
def email(request):
  return render(request,'listings/email.html')


def homePage(request):
  band = Band.objects.all()
  context ={'band':band}
  return render (request,'listings/base.html',context)
def band_list(request):
  band = Band.objects.all()
  return render(request,'listings/band_list.html',context={'bands':band})

# get a particular band
def band_detail(request,band_id):
  
  
  try:
    band = Band.objects.get(id=band_id)
    return render(request,'listings/band_detail.html',{'bands':band,"id":band_id})
  
  except Band.DoesNotExist:
    return HttpResponseNotFound(f"Oops! Data with id of {band_id} Not found")
  
  
def lists(request):
  list = Listing.objects.all()
  return render(request,'listings/listing_list.html',context={'lists':list})

def list_detail(request,list_id):

  
  try:
    list = Listing.objects.get(id=list_id)
    return render(request,'listings/listing_detail.html',context={'lists':list})
  except Listing.DoesNotExist:
    return HttpResponseNotFound("No Listing found")
    
def contact(request):
  if request.method == 'POST':
    
    
    form = ContactForm(request.POST)
    if form.is_valid():
      send_mail(
        subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via MerchEx Contact us form',
        message=form.cleaned_data['message'],from_email=form.cleaned_data['email'],
        recipient_list=['ofomimatthew7@gmail.com']
        
        )
      return redirect('email-sent')
  
  
  
  else:
    form = ContactForm()
    
    
    
  # print('method: ', request.method)
  # print('posting: ', request.POST)
  
  return render(request,'listings/contact.html',{'form':form})
  

# create bands
def band_create(request):
  form = BandForm()
  return render(request,'listings/band_create.html',{'form':form})