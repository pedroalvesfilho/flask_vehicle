"""Defines JSON API endpoints."""
from flask import jsonify, redirect, url_for, flash
from sqlalchemy.orm.exc import NoResultFound

from catalog import app
from catalog.database_setup import Category, Item
from catalog.connect_to_database import connect_to_database

@app.route('/catalog.json/')
def items_json():
    session = connect_to_database()
    categories = session.query(Category).all()
    serialised_catergories = [i.serialise for i in categories]
    session.close()
    return jsonify(Category=serialised_catergories)


@app.route('/catalog/<category_name>/<item_name>/JSON/')
@app.route('/catalog/<item_name>/JSON/')
def item_json(item_name, category_name=None):
    session = connect_to_database()
    try:
        item = session.query(Item).filter_by(name=item_name).one()
    except NoResultFound:
        session.close()
        flash("JSON error: The item '%s' does not exist." % item_name)
        return redirect(url_for('show_homepage'))

    session.close()
    return jsonify(Item=item.serialise)
