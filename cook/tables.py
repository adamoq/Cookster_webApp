from django.utils.html import format_html
import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

def renderSmallAv():
	return '<div class="small av-ico choosen"></div><div class="medium av-ico"></div><div class="large av-ico"></div>'
def renderMediumAv():
	return '<div class="small av-ico"></div><div class="medium av-ico choosen"></div><div class="large av-ico"></div>'
def renderLargeAv():
	return '<div class="small av-ico"></div><div class="medium av-ico"></div><div class="large av-ico choosen"></div>'
def renderEdit(value):
	return format_html('<img class="edit" src="/static/img/edit-icon.png" />',value)
def renderGps():
	return '<img class="gps-ico" src="/static/img/gps.png" />'
class ProductTable(tables.Table):
	id = tables.Column(verbose_name =_('Id'), attrs={'td': {'class': 'small id'},'th': {'class': 'small'}})
	name = tables.Column(verbose_name = _('Name'), attrs={'td': {'class': 'name'},'th': {'class': 'name'}})	
	av = tables.Column( verbose_name=_('Dostępność'),attrs={'td': {'class': 'av'},'th': {'class': 'av'}})
	edit = tables.Column(empty_values=(), verbose_name=_('Edit'), attrs={'td': {'class': 'small'},'th': {'class': 'small'}})
		
	def render_edit(self, value):
		return renderEdit(value)		
	def render_av(self, value):
		if value == "small":
			return format_html(renderSmallAv(),value)
		elif value == "medium":
			return format_html(renderMediumAv(),value)
		elif value == "large":
			return format_html(renderLargeAv(),value)
		else: return format_html(value,value)
		
class EmployeeTable(tables.Table):
	id = tables.Column(verbose_name = _('Id'), attrs={'td': {'class': 'small id'},'th': {'class': 'small'}})
	name = tables.Column(verbose_name = _('Imię'), attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})	
	surname = tables.Column( verbose_name=_('Nazwisko'),attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})
	position = tables.Column( verbose_name=_('Pozycja'),attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})
	phonenumber = tables.Column( verbose_name=_('Numer telefonu'),attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})
	status = tables.Column(verbose_name='', attrs={'td': {'class': 'small'},'th': {'class': 'small'}})
	#gps = tables.Column(empty_values=(), verbose_name='', attrs={'td': {'class': 'small gps'},'th': {'class': 'small gps'}})
	edit = tables.Column(empty_values=(), verbose_name='', attrs={'td': {'class': 'small'},'th': {'class': 'small'}})	
		
	def render_edit(self, value):
		return renderEdit(value)
	def render_gps(self, value):
		return format_html('<img src="/static/img/gps.png" />',value)
	def render_status(self, value):
		if value == "offline" : return format_html('<div class="small av-ico choosen"></div>',value)
		elif value == "nonactive" : return format_html(renderGps()+'<div class="medium av-ico choosen"></div>',value)
		elif value == "active" : return format_html(renderGps()+'<div class="large av-ico choosen"></div>',value)

class DishTable(tables.Table):
	id = tables.Column(verbose_name = _('Id'), attrs={'td': {'class': 'small id'},'th': {'class': 'small'}})
	name = tables.Column(verbose_name = _('Nazwa'), attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})	
	
	products = tables.Column( verbose_name=_('Produkty'))
	av = tables.Column( verbose_name=_('Dostępność'),attrs={'td': {'class': 'size22'},'th': {'class': 'size22'}})
	edit = tables.Column(empty_values=(), verbose_name=_('Edit'), attrs={'td': {'class': 'small'},'th': {'class': 'small'}})
	
	def render_edit(self, value):
		return renderEdit(value)
	
	def render_av(self, value):
		if value == "not available":
			return format_html(renderSmallAv(),value)
		elif value == "medium":
			return format_html(renderMediumAv(),value)
		elif value == "available":
			return format_html(renderLargeAv(),value)
		else: return format_html(value,value)
	def render_products(self, value):
		if value is not None:
			return ', '.join([category.name for category in value.all()])