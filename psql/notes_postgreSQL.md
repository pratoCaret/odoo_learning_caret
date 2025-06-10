# Enter in Postgres user :- postgres@pratham-HP-EliteBook-840-G3:~$
sudo -i -u postgres

# Enter in postgres client:
psql
# Exit from postgres client:
\q //But will remain in the same postgre client

# list all the existing roles in the sql:
\du

# create superuser:
create user pratham with superuser password '  ';
# create user:
create user pratham
# drop user:
drop user pratham

# Create a DB:
createdb db_name
# Enter in the Database to edit:
psql -d db_name
# Get information about the connection :
\connifo // will give socket an port information

