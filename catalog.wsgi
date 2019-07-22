#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/vagrant/catalog')

from catalog import app as application
from catalog.database_setup import create_db
from catalog.populate import populate_db

application.secret_key = 'super_secret_key'  # This needs changing in production env

application.config['DATABASE_URL'] = 'postgresql://catalog:PASSWORD@localhost/catalog'
application.config['OAUTH_SECRETS_LOCATION'] = '/vagrant/catalog/'

# Create database and populate it, if not already done so.
create_db(application.config['DATABASE_URL'])
populate()
