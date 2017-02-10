from openerp.osv import fields, osv
  
class partner_custom_fields(osv.osv):

  _inherit = "res.partner"

  _columns = {
    'lw_pasaporte': fields.char('Pasaporte'),
    'lw_pasaporte_vence': fields.date('Fecha de vencimiento Pasaporte'),
    'visa_americana': fields.boolean('Visa Americana'),
    'lw_visa_vence': fields.date('Fecha de vencimiento Visa'),
    'lw_entero': fields.char('Como se enteró de nosotros', required="True"),
    'lw_fecha_nac': fields.date('Fecha de nacimiento'),

  }

partner_custom_fields()