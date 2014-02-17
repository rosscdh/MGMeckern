import os, sys, site

site.addsitedir('/home/rosscdh/.virtualenvs/mgm/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'mgmeckern.settings'

activate_this = os.path.expanduser("~/.virtualenvs/mgm/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

# Calculate the path based on the location of the WSGI script
project = '/home/rosscdh/webapps/mgm/mgmeckern/'
workspace = os.path.dirname(project)
sys.path.append(workspace)

sys.path = ['/home/rosscdh/webapps/mgm/mgmeckern', '/home/rosscdh/webapps/mgm/mgmeckern/apps', '/home/rosscdh/webapps/mgm'] + sys.path

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()