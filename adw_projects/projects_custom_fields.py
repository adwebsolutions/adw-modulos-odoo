from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp
class projects_custom_fields(osv.osv):

  _inherit = "project.project"

  _columns = {
    'adw_proy_tipo_proyecto': fields.selection((('avanzado','Avanzado'),
    																						('tienda','Tienda Virtual'),
    																						('tienda_plantilla','Tienda Virtual Plantilla'),
    																						('catalogo','Catálogo'),
    																						('catalogo_plantilla','Catálogo Plantilla'),
    																						('avanzado_plantilla','Avanzado Plantilla'),
    																						('estandar','Estándar'),
    																						('desarrollo','Desarrollo a la Medida'),
    																						('intranet_crm','Intranet/CRM'),
    																						('identidad','Identidad Visual'),
    																						('mantenimiento','Mantenimiento'),
    																						('basico','Básico'),
    																						('emarketing','eMarketing')), 
    																						'Tipo de Proyecto', required=True),
	'adw_proy_fase': fields.selection((														('0-pendiente pago','Pendiente Pago'),
																							('1.1-nuevo','AMP - Nuevo'),
																							('1.2-cita inicial','AMP - Cita Inicial'),
																							('1.3-guia entregada','AMP - Guía Entregada'),
																							('1.4-documentando','AMP - Documentando'),
    																						('2-analisis','Análisis'),
    																						('3-diseno','Diseño'),
    																						('4-desarrollo','Desarrollo'),
    																						('5-captura','Captura'),
    																						('6-feedback','Feedbackd'),
    																						('7-calidad','Calidad'),
    																						('8-cierre','Cierre')),
    																						'Fase', required=True),																						
    'adw_proy_amp': fields.selection((														('Berenice Mejia','Berenice Mejia'),
    																						('Carmen Alfaro','Carmen Alfaro'),
    																						('Mayra Gutierrez','Mayra Gutierrez'),
    																						('Sofia Jauregui','Sofia Jauregui'),
    																						('Gaby Seimandi','Gaby Seimandi'),
    																						('Reina Diaz','Reina Diaz'),
																							('Fabiola Rangel','Fabiola Rangel'),),
    																						'AMP'),
    'adw_proy_resumen': fields.text('Resumen del Proyecto', required=True),
    'adw_proy_funcionalidades': fields.text('Adicionales', required=True),
    'adw_proy_propuestas_visuales': fields.text('Propuestas Visuales/Plantillas'),
    'adw_proy_link': fields.text('Link Desarrollo/Publicación'),
	'adw_proy_valor' : fields.float("Valor", digits_compute=dp.get_precision('Account'), required=True),
    'adw_proy_sin_respuesta': fields.boolean('Sin Respuesta'),
    'adw_proy_fecha_fin_info': fields.date('Fecha Fin Info'),
    'adw_proy_pendiente_pub': fields.boolean('Pendiente de Publicar'),
    'adw_proy_oficina': fields.selection([('matriz','Matriz'),
    																					('providencia','Providencia'),
    																					('chapultepec','Chapultepec'),
    																					('cursos','Cursos')], 
    																					'Oficina', required=True, default="matriz"),

	}

projects_custom_fields()