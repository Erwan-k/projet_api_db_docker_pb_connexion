from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

from routes.commentaire import commentaire1,commentaire2,commentaire3
from routes.compte import compte1,compte2,compte3,compte4,compte5,compte6,compte7,compte8
from routes.messagerie import messagerie1,messagerie2
from routes.message import message1
from routes.eleve import eleve1,eleve2,eleve3,eleve4
from routes.dispo import dispo1,dispo2,dispo3
from routes.cours import cours1,cours2,cours3

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(commentaire1,"/commentaire1") #&2
api.add_resource(commentaire2,"/commentaire2") #&2
api.add_resource(commentaire3,"/commentaire3") #&2
api.add_resource(compte1,"/compte1") #&2
api.add_resource(compte2,"/compte2") #&2
api.add_resource(compte3,"/compte3") #&2
api.add_resource(compte4,"/compte4") #&2
api.add_resource(compte5,"/compte5") #&2
api.add_resource(compte6,"/compte6") #&2
api.add_resource(compte7,"/compte7") #&2
api.add_resource(compte8,"/compte8") #&2
api.add_resource(messagerie1,"/messagerie1") #&2
api.add_resource(messagerie2,"/messagerie2") #&2
api.add_resource(message1,"/message1") #&2
api.add_resource(eleve1,"/eleve1") #&2
api.add_resource(eleve2,"/eleve2") #&2
api.add_resource(eleve3,"/eleve3") #&2
api.add_resource(eleve4,"/eleve4") #&2
api.add_resource(dispo1,"/dispo1") #&2
api.add_resource(dispo2,"/dispo2") #&2
api.add_resource(dispo3,"/dispo3") #&2
api.add_resource(cours1,"/cours1") #&2
api.add_resource(cours2,"/cours2") #&2
api.add_resource(cours3,"/cours3") #&2

if __name__ == "__main__":
	app.run(debug=True,port=5000,host='0.0.0.0')