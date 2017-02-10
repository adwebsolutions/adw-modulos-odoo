from openerp.osv import fields, osv

class pagos_custom_fields(osv.osv):

  _inherit = "account.voucher"

  _columns = {
    'adw_pay_departamento': fields.selection([('administracion','Administracion'),
    																					('oficina','Oficina'),
    																					('ventas','Ventas'),
    																					('impuestos','Impuestos'),
    																					('facturas','Facturas'),
    																					('hosting','Hosting'),
    																					('marketing','Marketing'),
    																					('proyectos','Proyectos'),
    																					('facebook','Facebook'),
    																					('adwords','ADWORDS'),
    																					('crm','CRM'),
    																					('soporte','Soporte')], 
    																						'Departamento', required=True),
    'adw_pay_pago1': fields.boolean('Pago Inicial'),    																						
    'adw_pay_oficina': fields.selection([('matriz','Matriz'),
    																					('providencia','Providencia'),
    																					('chapultepec','Chapultepec'),
    																					('cursos','Cursos')], 
    																					'Oficina', required=True, default="matriz"),
  }

pagos_custom_fields()