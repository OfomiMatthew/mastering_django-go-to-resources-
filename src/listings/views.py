from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from listings.models import Band, Listing
from listings.forms import ContactForm

# Create your views here.

# get all band

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
  form = ContactForm()
  return render(request,'listings/contact.html',{'form':form})
  
