{
    'name': 'Sport ESI',
    'version': '1.0',
    'category': 'Services',
    'summary': 'TP PGI Sport ESI',
    'description': """
        TP EXAM 2 - SPORT ESI-  module qui permet de gérer l'affectation des séances dans la salle de sport de l'école
    """,
    'author': 'Achraf Abdelkebir SIT2',
    'website': 'https://esi.dz',
    'license': 'LGPL-3',
    'depends': ['base', 'calendar'],
    'data': [
        'security\sport_security.xml',
        'security\ir.model.access.csv',
        'views\sport_views.xml',  
        
    ],
    'demo': [
        'demo/sport_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'maintainer': 'Achraf Abdelkebir SIT2',
}
