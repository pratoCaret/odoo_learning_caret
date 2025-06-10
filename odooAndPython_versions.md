11 - pyenv virtualenv 3.5.10 odoo11_env
12 - pyenv virtualenv 3.6.15 odoo12_env  &  pyenv virtualenv 3.5.10 odoo12_env - both works
13 - pyenv virtualenv 3.6.15 odoo13_env
14 - pyenv virtualenv 3.6.15 odoo14_env
15 - python3.7 -m venv 15env
16 - python3.8 -m venv 16env
17 - python3.10 -m venv 17env


Ask ChatGPT what is ppa for python installation in ubuntu

Python commands 
| Python Version | Installation Command                                         |
| -------------- | ------------------------------------------------------------ |
| **3.7**        | `sudo apt install python3.7 python3.7-venv python3.7-dev`    |
| **3.8**        | `sudo apt install python3.8 python3.8-venv python3.8-dev`    |
| **3.9**        | `sudo apt install python3.9 python3.9-venv python3.9-dev`    |
| **3.10**       | `sudo apt install python3.10 python3.10-venv python3.10-dev` |
| **3.11**       | `sudo apt install python3.11 python3.11-venv python3.11-dev` |
🔁 Replace 3.X with the version you want to install.


Version 2.7, 3.5, 3.6 can be installed only by : pyenv  | discontinued in ppa since 2020.
1. Install Dependencies
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
libffi-dev liblzma-dev git
2. Install pyenv
curl https://pyenv.run | bash
3. Add pyenv to your shell config
echo -e '\n# Pyenv setup' >> ~/.bashrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc
4. Install Python 3.5 and 3.6
pyenv install 3.5.10
pyenv install 3.6.15
5. Verify Installation
pyenv versions
    You should see:
      3.5.10
      3.6.15
6. Create Virtual Environments
pyenv virtualenv 3.5.10 odoo11_env
pyenv virtualenv 3.6.15 odoo12_env
    Then activate one:
    pyenv activate odoo11_env

result:
Installed Python-3.5.10 to /home/pratham/.pyenv/versions/3.5.10


I have installed till py version 3.5 as i will work till odoo 11 only, as of now.



installed versions of python in my system :
3.12.3
3.11.12
3.10.17
3.9.22
3.8.20
3.7.17
3.6.15 - using pyenv
3.5.10 - using pyenv
