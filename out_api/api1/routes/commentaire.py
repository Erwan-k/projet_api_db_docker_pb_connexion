from flask_restful import Api, Resource, reqparse
import os
from sqlalchemy.engine.url import make_url
import mysql.connector

url = make_url(os.getenv('DATABASE_URL'))
mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)


url = make_url(os.getenv('DATABASE_URL'))
mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)



commentaire1_post_args = reqparse.RequestParser()
commentaire1_post_args.add_argument("rien",type=str,required=True)
commentaire2_post_args = reqparse.RequestParser()
commentaire2_post_args.add_argument("token",type=str,required=True)
commentaire2_post_args.add_argument("message",type=str,required=True)
commentaire3_post_args = reqparse.RequestParser()
commentaire3_post_args.add_argument("token",type=str,required=True)
commentaire3_post_args.add_argument("idCommentaire",type=int,required=True)

class commentaire1(Resource):
	def post(self): #recuperer_la_liste_des_commentaires
		body = commentaire1_post_args.parse_args()

		mycursor = mydb.cursor()
		try:
			mycursor.execute("SELECT * FROM commentaires WHERE visible = 1")
		except:
			return {"retour":"pb1"}
		try:
			resultats = mycursor.fetchall()
		except:
			return {"retour":"pb2"}
		mycursor.close()

		return {"retour":resultats}


class commentaire2(Resource):
	def post(self): #laisser_un_commentaire
		body = commentaire2_post_args.parse_args()
		return {"retour":body}


class commentaire3(Resource):
	def post(self): #supprimer_un_commentaire
		body = commentaire3_post_args.parse_args()
		return {"retour":body}


