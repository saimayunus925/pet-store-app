
# this is basically where we configure/initialize our database

from flask_pymongo import PyMongo # importing PyMongo() obj for interfacing with our MongoDB database

from pets_app import pets_app # importing our app obj

pets_db = PyMongo(pets_app) # instantiating our DB obj for use with our app