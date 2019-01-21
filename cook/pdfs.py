from wkhtmltopdf.views import PDFTemplateView

from django.utils.html import format_html
import django_tables2 as tables
from .models import Product

from django.utils.translation import gettext as _
class ProductTable(tables.Table):
	id = tables.Column(verbose_name =_('id'), attrs={'td': {'class': 'small id'},'th': {'class': 'small'}})
	av = tables.Column( verbose_name='',attrs={'td': {'class': 'small'},'th': {'class': 'small'}})
	name = tables.Column(verbose_name = _('name'), attrs={'td': {'class': 'name'},'th': {'class': 'name'}})
	stock = tables.Column( verbose_name='',attrs={'td': {'class': 'small22'},'th': {'class': 'small22'}})
	edit = tables.Column(empty_values=(), verbose_name=_('edit'), attrs={'td': {'class': 'edit'},'th': {'class': 'edit'}})

	def render_edit(self, value):
		return renderEdit(value)
	def render_av(self, value):
		return render_av(value)	
	def render_stock(self, value, record):
		return format_html(str(value)+' '+str(record.unit),value)
class ProductPDF(PDFTemplateView):
    filename = 'product-filename'+'.pdf'
    template_name = 'pdfs/product.html'
    cmd_options = {
        'productTable': ProductTable(Product.objects.all()),
    }