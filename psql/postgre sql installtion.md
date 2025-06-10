# first update download packages: // preference to the 1st one:
sudo apt upgrade -y OR sudo apt update

# postgre sql installtion commands:
sudo apt install postgresql postgresql-contrib -y

# check postgre-Sql is active or not:
sudo systemctl status postgresql

# enter in the main postgres user:
sudo -i -u postgres

# to make changes with postgres-client inside the postgres-user:
psql

# create super user : // keep name same as you laptop's original username.
create user pratham with superuser password '  ';
// a superuser role is created and now we have to give it attributes.
// making 2 super superusers with all access- easy for us to remember.

# check for superuser created ?:
\du

# assign roles to the newly created superuser:
ALTER ROLE new_superuser WITH 
    SUPERUSER
    CREATEDB
    CREATEROLE
    REPLICATION
    BYPASSRLS;

