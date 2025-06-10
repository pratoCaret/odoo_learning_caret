# Road map for me to remember learning odoo:

# odoo setup:
1. using git clone, clone the repo and add a virtual environment.
2. dynamicly deploy the odoo from terminal
3. start adding the thing

# day 1:
1. manifest and init -- both are very much required for a folder to become a custom addon module
2. module < model < object < attribute
3. understanding the model and how it works. (folder structure and file inheritance decleration)

# day 2:
1. classes - models, abstract, transient
2. class attributes: _name, _inherit, view(tree, form, kandan), tracking

# day 3:
1. class attributes: sequence, no update attribute, rec name
2. create method
3. task by ma'am:

    a. manifest will need name to create a table 

    b. _ and . difference in the _name key for the module

    c. module, model, object - difference in detail

    d. fields and attributes - difference and details

# day 4:
1. _name : used to give the name of the database like 'hospital.patient' where 'hospital' is the model and 'patient' is the name of the model, it is represented in the database as 'hospital_patient'
2. _inherit : inherits a model in another model | are of 2 types: classic(without _name) & prototype(with _name)
3. _order : Controls the default ordering of records when fetched. _order = 'create_date desc' # create_date is a column in the table in db  # Default order: latest first
4. _rec_name : Record name (title name) that will be used to display the records when fetched.
5. _description : Provides a human-readable description of the model (displayed in the UI and logs).
6. SQL Constraints : gives rules to view, store,.. data in the database 
7. Python Constraints (api constrains -decorators) : have the logic that is to be applied to the data in a model. like email validation, phone number validation, age not -ve,.. 

added a few more python constrains for the project like email, phone number 

# day 5:



left behind