{
    'name': 'ADW Remover Links',
    'category': 'Website',
    'summary': 'Remover los links de bases de datos y login',
    'website': 'https://www.adweb.mx',
    'version': '1.0',
    'description': """
Modulo de ADWEB Links
===================

        """,
    'author': 'ADWEB',
    'depends': ['web'], 
    'external_dependencies': {},
    'data': ['views/webclient_templates.xml'],
    'js': ['static/src/js/adw_theme.js'],
    'css': ['static/src/css/adw_theme.css'], 
    'installable': True,
    'auto_install':False,
    'active':True,
}