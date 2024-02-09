from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from listings.models import Band, Listing

from listings.forms import BandForm, ListingForm,ContactForm
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
  
  
  
  
# --------------- BANDS SECTION-------------

# create bands
def band_create(request):
  if request.method =='POST':
    form = BandForm(request.POST)
    if form.is_valid():
      band = form.save()
      
      
      return redirect('band-detail',band.id)
  else:
    form = BandForm()
    
  
  return render(request,'listings/band_create.html',{'form':form})

# update band
def update_band(request,id):
  band = Band.objects.get(id=id)
  if request.method == "POST":
    form = BandForm(request.POST,instance=band)
    if form.is_valid():
      form.save()
      return redirect('band-detail',band.id)
  else:
    form = BandForm(instance=band)
    
  
  return render(request,'listings/band_update.html',{'form':form})
  




# ----------- LISTINGS SECTION ------------
# create listing
def list_create(request):
  if request.method == 'POST':
    form = ListingForm(request.POST)
    if form.is_valid():
      list = form.save()
      return redirect('list-detail', list.id)
  else:
    form = ListingForm()
  return render(request,'listings/listing_create.html',{'form':form})
    
def update_listing(request,id):
  lists = Listing.objects.get(id=id)
  if request.method == 'POST':
    form = ListingForm(request.POST,instance=lists)
    if form.is_valid():
      form.save()
      return redirect('list-detail',lists.id)
  else:
    form = ListingForm(instance=lists)
  return render(request,'listings/list_update.html',{'form':form})
  
  