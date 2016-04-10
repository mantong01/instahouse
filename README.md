# instahouse
Instahouse.org




# install packages

sudo easy_install pip
pip install virtualenv
pip install virtualenvwrapper
brew install mysql


export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source /Library/Frameworks/Python.framework/Versions/2.7/bin/virtualenvwrapper.sh


# create virtualenv
mkvirtualenv instahouse


# activate virtualenv
workon instahouse

# install python dependencies
pip install django
pip install mysql-python



