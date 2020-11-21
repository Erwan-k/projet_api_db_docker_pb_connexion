from flask_restful import Api, Resource, reqparse
import os
from sqlalchemy.engine.url import make_url
import mysql.connector
try:
	url = make_url(os.getenv('DATABASE_URL'))
	mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)
except:
	pass

cours1_post_args = reqparse.RequestParser()
cours1_post_args.add_argument("token",type=str,required=True)
cours2_post_args = reqparse.RequestParser()
cours2_post_args.add_argument("token",type=str,required=True)
cours2_post_args.add_argument("id_cours",type=int,required=True)
cours3_post_args = reqparse.RequestParser()
cours3_post_args.add_argument("code",type=str,required=True)
cours3_post_args.add_argument("reponse",type=int,required=True)
cours3_post_args.add_argument("message",type=str,required=True)

class cours1(Resource):
	def post(self): #recuperer_la_liste_des_cours
		body = cours1_post_args.parse_args()
		return {"retour":body}


class cours2(Resource):
	def post(self): #supprimer_un_cours
		body = cours2_post_args.parse_args()
		return {"retour":body}


class cours3(Resource):
	def post(self): #repondre_a_une_proposition_de_cours
		body = cours3_post_args.parse_args()
		return {"retour":body}


