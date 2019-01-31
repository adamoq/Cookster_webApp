# -*- coding: utf-8 -*-
from django.utils.html import format_html
import django_tables2 as tables
from .models import Product

from django.utils.translation import gettext as _
class ProductTable(tables.Table):
	id = tables.Column(verbose_name =_('id'), attrs={'td': {'class': 'small id'},'th': {'class': 'small'}})
	av = tables.Column( verbose_name='',attrs={'td': {'class': 'small'},'th': {'class': 'small'}})
	name = tables.Column(verbose_name = _('name'), attrs={'td': {'class': 'name'},'th': {'class': 'name'}})
	stock = tables.Column( verbose_name='',attrs={'td': {'class': 'small22'},'th': {'class': 'small22'}})

	def render_av(self, value):
		return format_html('<img src="/static/img/edit-icon.png" />',value)
	def render_stock(self, value, record):
		return format_html(str(value)+' '+str(record.unit),value)
from django.views.generic import View
from django.utils import timezone
import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
def link_callback(uri, rel):
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path

def render_pdf_view(request):
    from .models import LoginLog
    template_path = 'pdfs/product.html'
    sales = Product.objects.all()

    context = {'logs': LoginLog.objects.all(),}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html.encode('UTF-8'), dest=response, link_callback=link_callback, encoding='UTF-8')
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
class Render:

    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response, encoding='UTF-8')
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)
class Pdf(View):
	def get(self, request):
		from .models import LoginLog
		from datetime import datetime
		employee = request.GET.get('id')
		date1 = datetime.strptime(request.GET.get('date1'), '%Y-%M-%d')
		date2 = datetime.strptime(request.GET.get('date2'), '%Y-%M-%d')
		params = {
		    'logs': LoginLog.objects.filter(employee__id = employee, time__range=[date1,date2]),
		    'request': request
		}
		return Render.render('pdfs/product.html', params)



