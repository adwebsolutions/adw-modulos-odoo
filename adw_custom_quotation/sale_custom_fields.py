# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class sale_custom_fields(osv.osv):

  _inherit = "sale.order"

  _columns = {
	'adw_sale_company_info': fields.text('Detalles del Proyecto'),
    'adw_sale_servicio': fields.selection((('avanzado','Avanzado'),
                                                ('tienda','Tienda Virtual'),
                                                ('tienda_plantilla','Tienda Virtual Plantilla'),
                                                ('catalogo','Catálogo'),
                                                ('catalogo_plantilla','Catálogo Plantilla'),
                                                ('avanzado_plantilla','Avanzado Plantilla'),
                                                ('estandar','Estándar'),
                                                ('estandar_cms','Web Estándar CMS'),                                                
                                                ('desarrollo','Desarrollo a la Medida'),
                                                ('intranet_crm','Intranet/CRM'),
                                                ('identidad','Identidad Visual'),
                                                ('mantenimiento','Mantenimiento'),
                                                ('basico','Básico'),
                                                ('emarketing','eMarketing'), 
                                                ('hosting','Hosting'),
                                                ('soporte','Soporte')), 
                                                'Servicio'),    
  }

sale_custom_fields()
