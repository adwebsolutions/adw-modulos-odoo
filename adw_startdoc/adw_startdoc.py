# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
import openerp.tools
import re



class startdoc_doc(models.Model):
    _name = 'adw.startdoc.doc'
    _description = 'Project Starting Document'


    company_name = fields.Char(string = 'Nombre de la empresa', required=True)
    page_count = fields.Integer('Cantidad de páginas', required=True)
    cms = fields.Boolean('Administrador de Contenidos')
    desing_type = fields.Selection([('plantilla','Plantilla'),('alamedida','A la Medida')], string='Tipo de diseño', required=False)
    product_catalog = fields.Boolean('Catálogo de Productos')
    online_sell = fields.Boolean('Venta en línea')
    domain_name = fields.Char(string = 'Nombre de dominio', required=True)
    tobuy_domain_name = fields.Boolean('Comprar nombre de dominio')
    hosting = fields.Selection([('externo', 'Externo'), ('adweb', 'Adweb')], string='Hosting')
    business_desc = fields.Text(string='Descripción del negocio')
    competitive_adv = fields.Char(string='Ventajas Competitivas')
    target_market = fields.Char(string='Mercado Meta')
    competition = fields.Char(string='Principal Competencia')
    has_logo = fields.Boolean('Tiene logo')
    logo = fields.Many2one(comodel_name="ir.attachment", string="Adjuntar Logo")
    prefered_color = fields.Char(string='Preferencia de color')
    reference_page = fields.Text('Páginas de Referencia')
    home_layout_desc = fields.Text('Descripción de estructura del home')
    home_layout_screenshoot = fields.Many2one(comodel_name="ir.attachment", string="Adjuntar Screenshoot")
    internal_layout_desc = fields.Text('Descripción de estructura del Páginas internas')
    internal_layout_screenshoot = fields.Many2one(comodel_name="ir.attachment", string="Adjuntar Screenshoot")
    products_csv = fields.Many2one(comodel_name="ir.attachment", string="CSV de Productos")
    payment_methods = fields.Char(string='Métodos de pago')
    shippment_methods = fields.Char(string='Métodos de envío')
    chat = fields.Boolean('Chat online')
    extra_functionality = fields.Html('Descripción de Funcionalidades adicionales')

    page_ids = fields.One2many(comodel_name = 'adw.startdoc.page', inverse_name = 'doc_id', string = 'Paginas')
    project_id = fields.Many2one(comodel_name = 'project.project', string = 'Project', ondelete='set null', select=True, track_visibility='onchange',
        change_default=True, required=True, help="Proyecto asociado.")

class startdoc_page(models.Model):
    _name = 'adw.startdoc.page'
    _description = 'Paginas del proyecto'

    name = fields.Char(string='Nombre de la Página', required=True)
    keywords = fields.Char(string='Listado de palabras claves')
    contenido = fields.Html(string='Contenido', required=True)
    resources = fields.Many2many(comodel_name="ir.attachment", string="Asociar recursos")
    doc_id = fields.Many2many(comodel_name = 'adw.startdoc.doc', string = 'Documento de arranque')

class project(models.Model):
    _inherit = 'project.project'

    startdoc_ids = fields.Many2many(comodel_name = "adw.startdoc.doc", inverse_name = "project_id", string = "Documento de Arranque")
#    defined_startdoc = fields.Integer(compute = '_stardoc_count')
	
#    def _stardoc_count(self):    # method that calculate how many user stories exist
#        for p in self:
#            p.defined_startdoc = len(p.startdoc_ids)