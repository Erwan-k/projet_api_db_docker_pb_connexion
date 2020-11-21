from flask_restful import Api, Resource, reqparse
import os
from sqlalchemy.engine.url import make_url
import mysql.connector
try:
	url = make_url(os.getenv('DATABASE_URL'))
	mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)
except:
	pass

message1_post_args = reqparse.RequestParser()
message1_post_args.add_argument("pseudo",type=str,required=True)
message1_post_args.add_argument("message",type=str,required=True)

class message1(Resource):
	def post(self): #envoyer_un_message
		body = message1_post_args.parse_args()
		return {"retour":body}


