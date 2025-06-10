# Security Settings in possible hierarchy:
base user group has permission to read only.
# Groups: 
 # ADMIN:
   # Access Rights: On Doctor(crud-1111), Patient(crud-1111), Appointment(crud-1111)
   # Record Rules: Domain set to '1 = 1', so that everyone with admin tag can get to see everything. 
 # DOCTOR:
   # Access Rights: On Patient(crud-0100), Appointment(crud-0110)
   # Record Rules: On Appointment: domain_force=('doctor_id.user_id','=',user.id)
 # RECEPTIONIST:
   # Access Rights: On Patient(crud-1110), Appointment(crud-1110)
   # Record Rules: # no rules as on now ( commented-On Appointment: domain_force=('create_uid','=',user.id) )




doctor na rules verify karo and then try to take make another rule for read all.