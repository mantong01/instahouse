# instahouse
Instahouse.org




# install packages

sudo easy_install pip
pip install virtualenv
pip install virtualenvwrapper

export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source /Library/Frameworks/Python.framework/Versions/2.7/bin/virtualenvwrapper.sh


# create virtualenv
mkvirtualenv instahouse


# activate virtualenv
workon instahouse

# install python dependencies
pip install -r requirements.txt


#build react
cd instahouse/instahouse/basic_rendering
npm install
node render_server.js
python example.py

# beautiful soup needed for redfin parser
pip install beautifulsoup
