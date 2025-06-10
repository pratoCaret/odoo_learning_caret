{
    "name": "HMS",
    "author": "pratham vyas",
    "licence": "LGPL-3",
    "version": "17.0.1.2",
    "depends": [
        'mail', 'base', 'website'
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/groups_access_rights_record_rules.xml",
        # "security/group.xml",
        # "security/access_rights.xml",
        # "security/record_rules.xml",

        # "data/sequence.xml",
        "data/hospital_appointment_type_data.xml", # here si some error

        # these are added views while learning -action
        "data/cron_job_trial.xml",

        "views/user_form_inherit.xml",
        "views/patient_views.xml",
        "views/appointment_views.xml",

        "views/doctor_views.xml",

        # these are added views while learning -action
        # "report/patient_report_template.xml",
        # "views/url_action.xml",

        #wizard_trial
        "views/wizard_view.xml",
        #controllers_trial
        # "views/controllers_website_trial_template.xml",

        #controller_for_creating_a_view_in_website_side
        "views/patient_registration_form_view_website.xml",
        "views/web_controllers_rendering_template.xml",

        #web_menu_Creation
        "views/web_menu_patient_registration_form.xml",
        "views/web_menu_patient_regi_form.xml",

        #snippets:
        "views/snippets/custom_snippet.xml",

        "views/menu.xml"
    ],
    'demo': [
        'data/demo_patient_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # 'house-md/static/src/css/css_style.css',
            # 'house-md/static/src/scss/scss_style.scss',
            # 'house-md/static/src/scss/patient_registration_form_scss.scss',

        ]
    }

}
