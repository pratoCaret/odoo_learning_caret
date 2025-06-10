import logging
from odoo import fields,models,api
from odoo.exceptions import ValidationError, UserError, RedirectWarning

class HospitalOrmModel(models.Model):
    _name = "hospital.ormexample"
    _description = 'ORM Example for Patients'
    _rec_name = 'name'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="Gender")

    # def action_notify(self, title, message):
    #     return {
    #         'type': 'ir.actions.client',
    #         'tag': 'display_notification',
    #         'params': {
    #             'title': title,
    #             'message': message,
    #             'sticky': True,  # if True, notification won't disappear automatically
    #             'type': 'success',  # can be 'success', 'danger', 'warning', 'info'
    #         }
    #     }
    #   self.action_notify('Done Successfully', 'User created') # this will go in the function

    # 1. create
    def create(self, vals):
        print("\n")
        print("calling create.....")
        print("\n")
        vals['name'] = (vals.get('name') or 'Patient').title()
        vals['age'] = (vals.get('age') or '6')
        vals['gender'] = (vals.get('gender') or 'male')
        if int(vals['age']) < 0:
            raise ValidationError("CREATE . No -ve")
        print("\n")
        print(self," - CREATE self")
        print("\n")
        print(vals," - CREATE vals")
        print("\n")
        rtn = super(HospitalOrmModel,self).create(vals)
        print("\n")
        print(rtn," - CREATE rtn")
        print("\n")
        return rtn

    # 2. write - does not require @api.model from 17 and @api.multi from 13 onwards.
    def write(self, vals):
        # it can also be used for the same as above - capitalizing the names that are saved using .title()
        print("\n")
        print("calling write.....")
        print(vals," - WRITE vals")
        print("\n")
        for rec in self:
            # 1. Logging old and new values
            old_age = rec.age
            new_age = vals.get('age', old_age)
            # _logger = logging.info(f"Updating patient '{rec.name}': Age {old_age} → {new_age}")

            print("\n")
            print(rec," - WRITE rec")
            print("\n")
            # 2. Validating conditionally
            if 'age' in vals and new_age == 0:
                raise ValidationError("WRITE. ! ZERO")
            elif 'age' in vals and new_age < 0:
                raise ValidationError("WRITE. No -ve")
        print(self," - WRITE self")
        rtn = super(HospitalOrmModel, self).write(vals)
        print("\n")
        print(rtn," - WRITE rtn")
        print("\n")
        return rtn

    # 3. unlink
    def unlink(self):
        for rec in self:
            print("\n")
            print("unlink :    ",rec)
            print("\n")
            if rec.age < 5:
                raise ValidationError("Cannot delete underage patient")
        # return super().unlink() # no need to write class name and self from python 3 and +, it takes the self automatically
        rtn = super().unlink()
        print("\n")
        print(rtn, "     unlink rtn")
        print("\n")
        return rtn

    # 4. search
    def get_adults(self):
        print("\n")
        print("search self:  ",self)
        # rtn = self.env['hospital.ormexample'].search([('age', '>=', 18)])
        rtn = super().search([('age', '>=', 18)])
        print(rtn,' search return')
        print(type(rtn),"  search return type")
        print("\n")
        # raise UserError(f'search result: {rtn}')
        return rtn

    # 5. browse
    def browse_orm_method(self):
        print("\n")
        print("browse self:   ", self)
        print("\n")
        rtn = super().browse([1,2,50])
        print("browse rtn:   ", rtn)
        print("\n")
        for name in rtn:
            print(name.name)
        # print("browse rtn:   ", rtn.name)
        print("\n")
        # raise UserError(f"Browse result:   {rtn.name}")
        return rtn

    # 6. read
    def read_patients(self):
        print("\n")
        print("\n")
        rtn = super().search([('age', '>=', 18)]).read(['name', 'age'])
        # for i in rtn:
        #     print(f"Read self  {i}")
        # raise UserError(f"Read rtn result: {rtn}")
        return rtn

    # 7. copy
    # def copy(self, default=None):
    #     default = dict(default or {}, name=f"{self.name} (Copy)")
    #     return super().copy(default)

    # odoo mates
    # def copy(self, default=None):
    #     # default['name'] = "Copy("+self.name+")"
    #     print("\n")
    #     print(f"copy rtn, default value :    {default}")
    #     # print(f"copy rtn, before self :    {self}")
    #     rtn = super().copy(default=default)
    #     print(f"copy rtn, after rtn :    {rtn}")
    #     rtn.name="Copy("+self.name+")"
    #     print("\n")
    #     # raise UserError(f"Copy rtn result: {rtn}")
    #     return rtn

    # karan bhai
    # @api.model
    # def copy(self, default=None):
    #     default = dict(default or {})
    #
    #     if 'name' not in default:
    #         default['name'] = self.name + ' (Copy)'
    #     print("called copy ................")
    #     print("\n")
    #     print("copy applying")
    #     rtn = super().copy(default)
    #     print("copy applied")
    #     for i in rtn:
    #         print(f"{self.name}   ::::::::::::>>>   {i.name}")
    #     print(f"copy rtn :     {rtn}")
    #     print("\n")
    #     return rtn

    # my copy version
    def copy(self, default=None):
        print("\n copy start")
        rtn = super().copy(default={"name":f"{self.name} (copy)"})  # calls create orm method
        print(f"\n {self} - my copy self \n {default} - my copy default \n {rtn} - my copy rtn \n")
        print(" copy created  \n")
        rtn.name=f'{rtn.name} ( edit after create ! )' # calls write orm method
        print(" copy end \n")
        return rtn

    # 8. search_read
    def get_patient_data(self):
        print(f"\n {self}       SR self")
        rtn =super().search_read([('age', '>=', 65)], ['name', 'age'])
        print(f"\n{rtn}       SR rtn \n\n {len(rtn)} - number or records fetched. \n")
        return rtn

    # 9. read_group
    def group_by_gender(self):
        print(f"\n {self}       ReadGroup self")
        # rtn = super().read_group(domain=[('age', '>=', 18)],fields=['age:avg'],groupby=['gender'])
        # print(f"\n with domain declared \n {rtn}       ReadGroup rtn \n {len(rtn)} - number or records fetched. \n")
        rtn = super().read_group([('age', '>=', 18)],['age:avg'],['gender']) # domain, fields, groupby, offset, limit, orderby, lazy diff types
        print(f"\n without domain declared \n{rtn}       ReadGroup rtn \n {len(rtn)} - number or records fetched. \n")
        return rtn

    # 10. name_search
    # def name_search(self, name='', args=None, limit=10):
    #     name=input("\nenter the name:")
    #     args = list(args or [])
    #     if name:
    #         args += [('name', 'ilike', name)]
    #     rtn = super().name_search(name, args, limit=limit)
    #     print(f"\n {self}, {self.name}, {self.age}     name search self\n {rtn}     name search rtn\n")
    #     return rtn

    # another trial
    def name_search(self, name='', args=None, limit=10):
        name=input("\nenter the name:")
        args = list(args or [])
        if name:
            args += [('name', 'ilike', name)]
        rtn = super().name_search(name, args, limit=limit)
        print(f"\n {self}, {self.name}, {self.age}     name search self\n {rtn}     name search rtn\n")
        return rtn

    # another variation fpund on web.
    # def name_search(self, name='', args=None, operator='ilike', limit=100):
    #     args = args or []
    #     domain = []
    #     if name:
    #         domain = ['|', ('name', operator, name), ('phone', operator, name)]
    #     return self.search(domain + args, limit=limit).name_get()

    # 11. name_get
    def name_get(self):
        print(f"\n {self}, {self.name}, {self.age}     name search self \n")
        rtn = [(rec.id, f"{rec.name} ({rec.age} yrs)") for rec in self]
        print(f"\n {rtn}     name search rtn \n")
        return rtn

    # 12. default_get
    @api.model
    def default_get(self,fields):
        print(f"\n {fields} is default of default_get \n")
        rtn = super().default_get(fields) # for this to work a default ' ' (space) field should be given.
        print(f"\n {self}, {self.name}     default get self \n {rtn}     default get rtn\n")
        rtn['name'] = 'falana dhimkana'
        print(f"\n {self}, {self.name}     default get self \n {rtn}     default get rtn\n")
        print(f"\n {fields} is default of default_get \n")
        return rtn

    # variation
    # @api.model
    # def default_get(self, fields):
    #     res = super().default_get(fields)
    #     if 'age' in fields:
    #         res['age'] = 30
    #     return res

    # EXCEPTION HANDELLING
    # Validation error - done
    # User error - done

    # Redirect error
    def redirecterrorfunction(self):
        raise RedirectWarning(
            message="🚨 This is a test warning.",
            action = self.env.ref('house-md.action_hospital_doctor').id,
            button_text="Go to Doctors"
        )

    # Custom warning  - method depricated from odoo v17+
    # def custom_warning_method(self):
    #     raise Warning("⚠️ This is just a warning for demonstration purposes.")