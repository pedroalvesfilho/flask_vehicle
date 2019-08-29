#!/usr/bin/env python

import os.path

from catalog import app
from catalog.database_setup import create_db
from catalog.populate_db import populate

"""
When you start your app by running `flask run`
the `if __name__ == '__main__':` block gets skipped.
If you don't want to skip it, run with `python <script.py>`.
"""

 
if __name__ == '__main__':
    # App configuration
    app.config['DATABASE_URL'] = 'sqlite:///itemcatalog.db'
    # Or for PostgreSQL:
    #app.config['DATABASE_URL'] = 'postgresql://catalog:PASSWORD@localhost/catalog'    
    app.config['OAUTH_SECRETS_LOCATION'] = ''    
    app.secret_key = 'super_secret_key'  # This needs changing in production env

    if app.config['DATABASE_URL'] == 'sqlite:///itemcatalog.db':
        if os.path.isfile('itemcatalog.db') is False:
            create_db(app.config['DATABASE_URL'])
            populate()
    else:  # for postgresql
        create_db(app.config['DATABASE_URL'])
        populate()

    app.debug = True
    app.run(host='0.0.0.0', port=5000)
