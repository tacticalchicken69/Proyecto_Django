from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def testing(request):
  template = loader.get_template('template.html')
  mymembers = Member.objects.all().values()
  column_firstname = Member.objects.values_list('firstname')
  records_uribe = Member.objects.filter(column_firstname='uribe').values()
  record_uribe_westcol = Member.objects.filter(firstname='uribe', id=2).values()
  record_OR_andres_maria= Member.objects. filter(Q(firstname= 'Andres') | Q(firstname='Maria'))
  record_like_start_L = Member.objects. filter(firstname_istartswith='L'). values()
  record_like_ends_s= Member objects. filter(firstname_iendswith='s'). values ()
  Grecord_like_contains_ez= Member. objects filter(lastname_icontains='ez'). values()
  order_by_asc= Member. objects.all() order_by'firstname'). values ()
  order_by_des= Member objects.all). order _by('-firstname"). values ()
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'], 
    'mymembers': mymembers,  
    'column_firstname': column_firstname,  
    'records_andres': records_andres,
    'record_andres_sandoval': record_AND_andres_sandoval,
    "record_OR_andres_maria": record_oR_andres_maria,
    'record_like_start_L': record_like_start_L,
    'record_like_ends_s': record_like_ends_s,
    'record_like_contains_ez': record_like_contains_ez,
    'order_by_asc': order_by_asc,
    'order_by_desc": order_by_desc,
  }
  return HttpResponse(template.render(context, requrest))