# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_contact(app):
    app.contact.create(Contact(fname="somename", mname="somemname", lname="somelname"))

