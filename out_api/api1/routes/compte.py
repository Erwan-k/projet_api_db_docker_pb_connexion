from flask_restful import Api, Resource, reqparse
import os
from sqlalchemy.engine.url import make_url
import mysql.connector
try:
	url = make_url(os.getenv('DATABASE_URL'))
	mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)
except:
	pass

compte1_post_args = reqparse.RequestParser()
compte1_post_args.add_argument("nom_parent",type=str,required=True)
compte1_post_args.add_argument("prenom_parent",type=str,required=True)
compte1_post_args.add_argument("adresse_mail",type=str,required=True)
compte1_post_args.add_argument("mot_de_passe",type=str,required=True)
compte2_post_args = reqparse.RequestParser()
compte2_post_args.add_argument("adresse_mail_parent",type=str,required=True)
compte2_post_args.add_argument("mot_de_passe_parent",type=str,required=True)
compte3_post_args = reqparse.RequestParser()
compte3_post_args.add_argument("adresse_mail_parent",type=str,required=True)
compte3_post_args.add_argument("code_de_verification",type=str,required=True)
compte4_post_args = reqparse.RequestParser()
compte4_post_args.add_argument("adresse_mail_parent",type=str,required=True)
compte5_post_args = reqparse.RequestParser()
compte5_post_args.add_argument("adresse_mail_parent",type=str,required=True)
compte6_post_args = reqparse.RequestParser()
compte6_post_args.add_argument("adresse_mail_parent",type=str,required=True)
compte6_post_args.add_argument("code",type=str,required=True)
compte6_post_args.add_argument("nouveau_mdp",type=str,required=True)
compte7_post_args = reqparse.RequestParser()
compte7_post_args.add_argument("adresse_mail_parent",type=str,required=True)
compte7_post_args.add_argument("ancien_mdp",type=str,required=True)
compte7_post_args.add_argument("nouveau_mdp",type=str,required=True)
compte8_post_args = reqparse.RequestParser()
compte8_post_args.add_argument("token",type=str,required=True)

class compte1(Resource):
	def post(self): #s_inscrire
		body = compte1_post_args.parse_args()
		return {"retour":body}


class compte2(Resource):
	def post(self): #se_connecter
		body = compte2_post_args.parse_args()
		return {"retour":body}


class compte3(Resource):
	def post(self): #verifier_son_adresse_mail
		body = compte3_post_args.parse_args()
		return {"retour":body}


class compte4(Resource):
	def post(self): #demander_nouvel_email_confirmation
		body = compte4_post_args.parse_args()
		return {"retour":body}


class compte5(Resource):
	def post(self): #demander_code_pour_changer_de_mdp
		body = compte5_post_args.parse_args()
		return {"retour":body}


class compte6(Resource):
	def post(self): #changer_son_mdp_a_l_aide_d_un_code
		body = compte6_post_args.parse_args()
		return {"retour":body}


class compte7(Resource):
	def post(self): #changer_son_mdp_a_l_aide_de_l_ancien
		body = compte7_post_args.parse_args()
		return {"retour":body}


class compte8(Resource):
	def post(self): #recuperer_les_informations_de_compte
		body = compte8_post_args.parse_args()
		return {"retour":body}


