{
    'name': "Student Management",
    'version': '13.1.0',
    'depends': ['base'],
    'author': "Socius Trainee",
    'category': 'Category',
    'description': "Student Management module",
    # data files always loaded at installation
    'data': [
        'views/students.xml',
        'views/staff_info.xml'
        'security/ir.model.access.csv',

    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable': True
}
