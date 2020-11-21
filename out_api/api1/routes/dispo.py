from flask_restful import Api, Resource, reqparse
import os
from sqlalchemy.engine.url import make_url
import mysql.connector
try:
	url = make_url(os.getenv('DATABASE_URL'))
	mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)
except:
	pass

dispo1_post_args = reqparse.RequestParser()
dispo1_post_args.add_argument("token",type=str,required=True)
dispo2_post_args = reqparse.RequestParser()
dispo2_post_args.add_argument("token",type=str,required=True)
dispo2_post_args.add_argument("nom_eleve",type=str,required=True)
dispo2_post_args.add_argument("prenom_eleve",type=str,required=True)
dispo2_post_args.add_argument("heure_debut",type=int,required=True)
dispo2_post_args.add_argument("heure_fin",type=int,required=True)
dispo3_post_args = reqparse.RequestParser()
dispo3_post_args.add_argument("token",type=str,required=True)
dispo3_post_args.add_argument("id_disponibilite",type=int,required=True)

class dispo1(Resource):
	def post(self): #recuperer_les_disponibilites
		body = dispo1_post_args.parse_args()
		return {"retour":body}


class dispo2(Resource):
	def post(self): #ajouter_une_disponibilite
		body = dispo2_post_args.parse_args()
		return {"retour":body}


class dispo3(Resource):
	def post(self): #supprimer_une_disponibilite
		body = dispo3_post_args.parse_args()
		return {"retour":body}


