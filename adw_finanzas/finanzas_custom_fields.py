from openerp.osv import fields, osv

class finanzas_custom_fields(osv.osv):

  _inherit = "account.invoice"

  _columns = {
    'adw_fin_departamento': fields.selection([('administracion','Administracion'),
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
    																						'Departamento'),
    'adw_fin_factura': fields.char('Factura Fiscal'),    																						
    'adw_fin_standby': fields.boolean('Proyecto StandBy'),    																						
    'adw_fin_oficina': fields.selection([('matriz','Matriz'),
    																					('providencia','Providencia'),
    																					('chapultepec','Chapultepec'),
    																					('cursos','Cursos')], 
    																					'Oficina', required=True, default="matriz"),
  }

finanzas_custom_fields()