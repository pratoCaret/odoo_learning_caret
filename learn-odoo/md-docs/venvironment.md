# Terminal ki settings change in ubuntu:
nano ~/.bashrc


# Odoo installations and environment
first clone the main odoo files with 

git clone https://www.github.com/odoo/odoo --depth 1 --branch 17.0

Then navigate to the folder you have just cloned - in terminal

cd ~/projectsOdoo/odoo - goes to the file where the odoo's particular version is available.

#Start the Environment and install all the dependencies: 

python3 -m venv venv  # Create virtual environment

source venv/bin/activate  # Activate it

deactive # To deactive and exit the venv

rm -rf ~/Projects/myproject/venv_name # delete venv

# Odoo dependencies
pip install -r requirements.txt  # Install dependencies # 'requirements.txt' is a file inside the odoo folder that has all the dependencies listed for the project/odoo to run.


git clone https://www.github.com/odoo/odoo --depth 1 --branch 17.0 17.0
cd 17.0
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt






# Configure Odoo
Create a configuration file:

sudo nano /etc/odoo.conf

Paste the following:

[options]

admin_passwd = admin

db_host = False

db_port = False

db_user = odoo

db_password = odoo

addons_path = /opt/odoo/odoo/addons

logfile = /var/log/odoo/odoo.log

Save and exit (Ctrl + X, then Y, then Enter).

# Run Odoo
sudo su - odoo

cd odoo

source venv/bin/activate # activate venv 

python3 odoo-bin --config=/etc/odoo.conf

Odoo will start at http://localhost:8069.



python3.12 odoo-bin --addons=/home/pratham/projectsOdoo/odoo17/addons, -d dbname_v18 -p 1888 # given manually for terminal to run.

python3.12 odoo-bin --addons=addons -d dbname_v18 -p 3000 
    # addons given dynamically  --dev=all (to add allchanges without restarting the server / dynamic adding)

python3.12 odoo-bin --addons=addons,project-task-trainee/learn-odoo/17.0/customAddons -d learning_v17 -p 3000 --dev=all


Odoo 17: Requires Python 3.10.​

Odoo 16: Requires Python 3.8.​

Odoo 15: Requires Python 3.7.​

Odoo 14: Requires Python 3.6.​

Odoo 13: Requires Python 3.6.​

Odoo 12: Supports both Python 3.5 and 3.6.​

Odoo 11: Supports both Python 2.7 and 3.5.​

Odoo 10: Requires Python 2.7.​

Odoo 9: Requires Python 2.7.​

Odoo 8: Requires Python 2.7.
