# -*- coding: utf-8 -*-
from openerp import models, fields
class AdwMtto(models.Model):
    _name = 'adw.mtto'
    name = fields.Char('Descripción', required=True)
    active = fields.Boolean('Activo?', required=True)
    is_done = fields.Boolean('Done?')
    fecha = fields.Date('Fecha programada')
    fecha_ejecucion = fields.Date('Fecha ejecución')
    client_id = fields.Many2one('res.partner', 'Cliente') 
    customer = fields.Many2one('res.partner', 'Cliente')
    product_id = fields.Many2one('product.product', "Moto")
    _defaults = { 'active': True }
