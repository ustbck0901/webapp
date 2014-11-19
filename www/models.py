__author__ = 'Wang Xin'

import time,uuid

from transwrap.db import next_id
from transwrap.orm import Model,StringField,BooleanField,FloatField,TextField

def next_id():
	return '%015d%s000' % (int(time.time()*1000),uuid.uuid4().hex)

class User(Model):
	__table__ = 'users'

	id = StringField(primary_key=True,default=next_id,ddl='varchar(50)')
	email = StringField(primary_key=False,ddl='varchar(50)')
	password = StringField(ddl='varchar(50)')
	admin = BooleanField()
	name = StringField(ddl='varchar(50)')
	image = StringField(ddl='varchar(500)')
	create_at = FloatField(updatable=False,default=time.time)

class Blog(Model):
	__table__ = 'blogs'

	id = StringField(primary_key=True,default=next_id,ddl='varchar(50)')
	user_id = StringField(updatable=False,ddl='varchar(50)')
	user_name = StringField(ddl='varchar(50)')
	user_image = StringField(ddl='varchar(500)')
	name = StringField(ddl='varchar(50)')
	summary = StringField(ddl='varchar(200)')
	content = TextField()
	create_at = FloatField(updatable=False,default=time.time)

class Commit(Model):
	__table__ = 'comments'
	id = StringField(primary_key=True,default=next_id,ddl='varchar(50)')
	blog_id = StringField(updatable=False,ddl='varchar(50)')
	user_id = StringField(updatable=False,ddl='varchar(50)')
	user_name = StringField(ddl='varchar(50)')
	user_image = StringField(ddl='varchar(500)')
	content = TextField()
	create_at = FloatField(updatable=False,default=time.time)