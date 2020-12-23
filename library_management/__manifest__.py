
{
    'name': "Library Management",
    'version': '13.1',
    'depends': ['base',],
    'author': "Socius Trainee",
    'category': 'Category',
    'description': "Library management module",
    # data files always loaded at installation
    'data': [
        'views/book_view.xml',
        'views/book_registration.xml',
        'security/ir.model.access.csv',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable': True

}
