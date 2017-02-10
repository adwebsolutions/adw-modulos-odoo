{
    'name': 'Leonarwill CRM campos adicioanles',
    'category': 'Tools',
    'summary': 'Incluir campos adicionales en el crm',
    'website': 'https://www.adweb.mx',
    'version': '1.0',
    'description': """
Modulo de ADWEB CRM
===================

        """,
    'author': 'ADWEB',
    'depends': ['crm'], 
    'external_dependencies': {},
    'data': ['views/crm_custom_fields.xml','views/crm_pago_proveedor.xml','views/partner_birthday_field.xml','views/partner_custom_fields.xml',],
    'installable': True,
    'auto_install':False,
    'active':True,
}
