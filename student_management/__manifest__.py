{
    'name': "Student Management",
    'version': '13.1.0',
    'depends': ['website'],
    'author': "Socius Trainee",
    'category': 'Category',
    'description': "Student Management module",
    # data files always loaded at installation
    'data': [

        'security/ir.model.access.csv',
        'views/students.xml',
        'views/hallticket.xml',

        'views/students.xml',
        'views/staff_info.xml',
        'security/ir.model.access.csv',
        'reports/report.xml',
        'reports/student_report.xml',

        'views/front_end/webpages/first_page.xml'


    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable': True
}
