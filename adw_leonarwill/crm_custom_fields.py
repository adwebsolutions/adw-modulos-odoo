import logging
from openerp.osv import fields, osv

_logger = logging.getLogger(__name__)

class crm_pago_proveedor(osv.osv):
    _name = 'crm.pago.proveedor'
    _columns = {
        'name': fields.char('Name', default=''),
        'crm_reserva_id' : fields.many2one('crm.lead', ondelete='cascade', string="Lead", required="True"),
        'clave_resevacion': fields.char('Clave de reservación'),
        'proveedor': fields.char('Proveedor'),
        'hotel': fields.char('Hotel'),
        'tiempo_limite': fields.char('Tiempo Limite'),
        'lw_crm_quien_atendio': fields.char('Quién Atendió'),
        'lw_crm_email_operador': fields.char('Email Operador'),
        'lw_crm_tarifa_neta': fields.float('Tarifa Neta'),
        'lw_crm_comision': fields.float('Comisión'),       
        'lw_crm_pago_a_proveedor': fields.float('Pago al proveedor'),
        'lw_crm_anticipo': fields.char('Anticipo'), 
        'lw_crm_comentario': fields.text('Comentarios'),
        'lw_crm_quiere_factura': fields.boolean('El cliente quiere Factura?'),
        'lw_crm_nombre_pasajero': fields.char('Nombre del pasajero'),
    }
    
    def crm_solicitar_pago(self, cr, uid, ids, context=None):
        if not context:
            context = {}
        email_template_pool = self.pool.get('email.template')		
        # Set your template search domain
        search_domain = [('name', '=', 'Solicitud de Pago Directa')]
        # Get template id
        template_id = email_template_pool.search(cr, uid, search_domain, context=context)[0]
        #template_id.send_mail(self.id, force_send=True)
        for pago in self.browse(cr, uid, ids, context):
            return self.pool['email.template'].send_mail(
                cr, uid, template_id, pago.id, force_send=True,
                context=context)  

    
class crm_reserva(osv.osv):
    _name = 'crm.reserva'
    _columns = {
        'name': fields.char('Name', default=''),
        'crm_reserva_id' : fields.many2one('crm.lead', ondelete='cascade', string="Lead", required="True"),
        'clave_resevacion': fields.char('Clave de reservación'),
        'proveedor': fields.char('Proveedor'),
        'hotel': fields.char('Hotel'),
        'tiempo_limite': fields.char('Tiempo Limite'),
        'lw_crm_quien_atendio': fields.char('Quién Atendió'),
        'lw_crm_plan_alimentos': fields.char('Plan de Alimentos'),
        'lw_crm_categoria': fields.char('Categoría'),
        'lw_crm_anticipo': fields.char('Anticipo'),
        'lw_crm_forma_pago_agencia': fields.char('Forma de pago Agencia'), 
        'lw_crm_tarifa_neta': fields.float('Tarifa Neta'),
        'lw_crm_comision': fields.float('Comisión'),           
        'lw_crm_pago_a_proveedor': fields.float('Pago al proveedor'),
        'lw_crm_quiere_factura': fields.boolean('El cliente quiere Factura?'),
        'lw_crm_nombre_pasajero': fields.char('Nombre del pasajero'),
        'lw_crm_comentario': fields.text('Comentarios'),
        

    }    

            
    def crm_crear_solicitud_de_pago(self, cr, uid, ids, context=None):
        if not context:
            context = {}
        pago_pool = self.pool.get('crm.pago.proveedor')
        lead_pool = self.pool.get('crm.lead')
        for reserv in self.browse(cr, uid, ids, context):
            data_payment = {}
            data_payment['clave_resevacion'] = reserv.clave_resevacion
            data_payment['proveedor'] = reserv.proveedor
            data_payment['crm_reserva_id'] = reserv.crm_reserva_id.id            
            data_payment['hotel'] = reserv.hotel
            data_payment['tiempo_limite'] = reserv.tiempo_limite
            data_payment['lw_crm_quien_atendio'] = reserv.lw_crm_quien_atendio
            #data_payment['lw_crm_email_operador'] =  reserv.lw_crm_email_operador
            data_payment['lw_crm_tarifa_neta'] =  reserv.lw_crm_tarifa_neta
            data_payment['lw_crm_comision'] =  reserv.lw_crm_comision
            data_payment['lw_crm_pago_a_proveedor'] =  reserv.lw_crm_pago_a_proveedor
            data_payment['lw_crm_anticipo'] =  reserv.lw_crm_anticipo
            data_payment['lw_crm_comentario'] = reserv.lw_crm_comentario   
            data_payment['lw_crm_quiere_factura'] =reserv.lw_crm_quiere_factura
            data_payment['lw_crm_nombre_pasajero'] = reserv.lw_crm_nombre_pasajero   
     
            id_payment = pago_pool.create(cr, uid, data_payment, context=context)
#            lead_pool.write(cr, uid, reserv.crm_reserva_id, {'lw_crm_pago_proveedor': [(4, id_payment)]})
#            if id_payment:
#                if reserv.lead_ids:
#                    lead_ids = [lead.id for lead in reserv.lead_ids]
#                    if lead_ids:
#                        lead_pool.write(cr, uid, lead_ids, {'lw_crm_pago_proveedor': [(4, id_payment)]})
            
    
    
class crm_custom_fields(osv.osv):

  _inherit = "crm.lead"

  _columns = { 
    'lw_crm_origen': fields.char('Origen', required=True),
    'lw_crm_destino': fields.char('Destino', required=True),
    'lw_crm_motivoviaje': fields.char('Motivo del viaje'),
    'lw_crm_fsalida': fields.date('Fecha de salida', required=True),
    'lw_crm_fregreso': fields.date('Fecha de regreso', required=True),
    'lw_crm_nPersonas': fields.integer('Número de personas', required=True, default=1),
    'lw_crm_nNinnos': fields.integer('Cantidad de niños'),
    'lw_crm_rango_edad': fields.char('Rango de edades'),
    'lw_crm_quiere_factura': fields.boolean('Quieren factura ?'),
    'lw_crm_rfc': fields.char('RFC'),
    'lw_crm_concepto': fields.char('Concepto'),
    'lw_crm_rsocial': fields.char('Razón Social'),
    'lw_crm_subtotal': fields.float('Subtotal'),
    'lw_crm_iva': fields.float('IVA'),
    'lw_crm_total': fields.float('Total'),
    'lw_crm_domicilio': fields.char('Domicilio Fiscal'),
    'lw_crm_nocuenta': fields.char('Número de Cuenta'),
    'lw_crm_forma_pago': fields.selection((('efectivo','Efectivo'),
    											('tarjeta','Tarjeta'),
                                                ('credito','Crédito'),
                                                ('cheque', 'Cheque'),
                                                ('transferencia', 'Transferencia')),
    											'Forma de pago', default="efectivo"),
    'lw_crm_reserva': fields.one2many('crm.reserva',
                                        'crm_reserva_id',
                                        'Reservas'),
    'lw_crm_pago_proveedor': fields.one2many('crm.pago.proveedor',
                                        'crm_reserva_id',
                                        'Pagos a Proveedores'),              
    }

  def solicitar_factura(self, cr, uid, ids, context=None):
    if not context:
        context = {}    
    email_template_pool = self.pool.get('email.template')    
    lead = self.browse(cr, uid, ids[0], context=context)    
    # Set your template search domain
    search_domain = [('name', '=', 'Solicitud de Factura')]
    # Get template id
    template_id = email_template_pool.search(cr, uid, search_domain, context=context)[0]
    #template_id.send_mail(self.id, force_send=True)
    return self.pool['email.template'].send_mail(
        cr, uid, template_id, lead.id, force_send=True,
        context=context)         

crm_custom_fields()
