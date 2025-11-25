from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

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
  # La siguiente consulta es incorrecta, se debe usar el nombre del campo directamente.
  # records_uribe = Member.objects.filter(column_firstname='uribe').values()
  records_uribe = Member.objects.filter(firstname='uribe').values()
  record_uribe_westcol = Member.objects.filter(firstname='uribe', lastname='Westcol').values()
  record_OR_andres_maria= Member.objects.filter(Q(firstname='Andres') | Q(firstname='Maria')).values()
  record_like_start_L = Member.objects.filter(firstname__istartswith='L').values()
  record_like_ends_s = Member.objects.filter(firstname__iendswith='s').values()
  record_like_contains_ez = Member.objects.filter(lastname__icontains='ez').values()
  order_by_asc = Member.objects.all().order_by('firstname').values()
  order_by_desc = Member.objects.all().order_by('-firstname').values()
  context = {
    'mymembers': mymembers,
    'records_uribe': records_uribe,
    'record_uribe_westcol': record_uribe_westcol,
    "record_OR_andres_maria": record_OR_andres_maria,
    'record_like_start_L': record_like_start_L,
    'record_like_ends_s': record_like_ends_s,
    'record_like_contains_ez': record_like_contains_ez,
    'order_by_asc': order_by_asc,
    'order_by_desc': order_by_desc,
    # Las siguientes variables no estaban definidas en tu código original:
    # 'miembros', 'column_firstname', 'records_andres', 'record_andres_sandoval'
  }
  return HttpResponse(template.render(context, request))