from flask_restful import Api, Resource, reqparse
import os
from sqlalchemy.engine.url import make_url
import mysql.connector
try:
	url = make_url(os.getenv('DATABASE_URL'))
	mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)
except:
	pass

eleve1_post_args = reqparse.RequestParser()
eleve1_post_args.add_argument("token",type=str,required=True)
eleve2_post_args = reqparse.RequestParser()
eleve2_post_args.add_argument("token",type=str,required=True)
eleve2_post_args.add_argument("nom_eleve",type=str,required=True)
eleve2_post_args.add_argument("prenom_eleve",type=str,required=True)
eleve2_post_args.add_argument("classe_eleve",type=str,required=True)
eleve2_post_args.add_argument("lycee_eleve",type=str,required=True)
eleve2_post_args.add_argument("professeur_au_lycee",type=str,required=True)
eleve2_post_args.add_argument("spe_eleve",type=str,required=True)
eleve3_post_args = reqparse.RequestParser()
eleve3_post_args.add_argument("token",type=str,required=True)
eleve3_post_args.add_argument("nom_eleve",type=str,required=True)
eleve3_post_args.add_argument("prenom_eleve",type=str,required=True)
eleve3_post_args.add_argument("classe_eleve",type=str,required=True)
eleve3_post_args.add_argument("lycee_eleve",type=str,required=True)
eleve3_post_args.add_argument("professeur_au_lycee",type=str,required=True)
eleve3_post_args.add_argument("spe_eleve",type=str,required=True)
eleve4_post_args = reqparse.RequestParser()
eleve4_post_args.add_argument("token",type=str,required=True)
eleve4_post_args.add_argument("nom_eleve",type=str,required=True)
eleve4_post_args.add_argument("prenom_eleve",type=str,required=True)

class eleve1(Resource):
	def post(self): #recuperer_la_liste_des_eleves
		body = eleve1_post_args.parse_args()
		return {"retour":body}


class eleve2(Resource):
	def post(self): #ajouter_un_eleve
		body = eleve2_post_args.parse_args()
		return {"retour":body}


class eleve3(Resource):
	def post(self): #modifier_un_eleve
		body = eleve3_post_args.parse_args()
		return {"retour":body}


class eleve4(Resource):
	def post(self): #supprimer_un_eleve
		body = eleve4_post_args.parse_args()
		return {"retour":body}


