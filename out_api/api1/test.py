import requests
url = "http://127.0.0.1:1234/"

def testeur(route,arguments,type_):
	global url
	if type_ == "get":
		response = requests.get(url+route,arguments)
	if type_ == "put":
		response = requests.put(url+route,arguments)
	if type_ == "post":
		response = requests.post(url+route,arguments)
	if type_ == "delete":
		response = requests.delete(url+route,arguments)
	return response.json()


##############################   commentaire   ##############################

s = testeur("commentaire1",{"rien":"string"},"post")
print(s)

s = testeur("commentaire2",{"token":"string","message":"string"},"post")
print(s)

s = testeur("commentaire3",{"token":"string","idCommentaire":1},"post")
print(s)

##############################   compte   ##############################

s = testeur("compte1",{"nom_parent":"string","prenom_parent":"string","adresse_mail":"string","mot_de_passe":"string"},"post")
print(s)

s = testeur("compte2",{"adresse_mail_parent":"string","mot_de_passe_parent":"string"},"post")
print(s)

s = testeur("compte3",{"adresse_mail_parent":"string","code_de_verification":"string"},"post")
print(s)

s = testeur("compte4",{"adresse_mail_parent":"string"},"post")
print(s)

s = testeur("compte5",{"adresse_mail_parent":"string"},"post")
print(s)

s = testeur("compte6",{"adresse_mail_parent":"string","code":"string","nouveau_mdp":"string"},"post")
print(s)

s = testeur("compte7",{"adresse_mail_parent":"string","ancien_mdp":"string","nouveau_mdp":"string"},"post")
print(s)

s = testeur("compte8",{"token":"string"},"post")
print(s)

##############################   messagerie   ##############################

s = testeur("messagerie1",{"token":"string"},"post")
print(s)

s = testeur("messagerie2",{"token":"string","message":"string"},"post")
print(s)

##############################   message   ##############################

s = testeur("message1",{"pseudo":"string","message":"string"},"post")
print(s)

##############################   eleve   ##############################

s = testeur("eleve1",{"token":"string"},"post")
print(s)

s = testeur("eleve2",{"token":"string","nom_eleve":"string","prenom_eleve":"string","classe_eleve":"string","lycee_eleve":"string","professeur_au_lycee":"string","spe_eleve":"string"},"post")
print(s)

s = testeur("eleve3",{"token":"string","nom_eleve":"string","prenom_eleve":"string","classe_eleve":"string","lycee_eleve":"string","professeur_au_lycee":"string","spe_eleve":"string"},"post")
print(s)

s = testeur("eleve4",{"token":"string","nom_eleve":"string","prenom_eleve":"string"},"post")
print(s)

##############################   dispo   ##############################

s = testeur("dispo1",{"token":"string"},"post")
print(s)

s = testeur("dispo2",{"token":"string","nom_eleve":"string","prenom_eleve":"string","heure_debut":1,"heure_fin":1},"post")
print(s)

s = testeur("dispo3",{"token":"string","id_disponibilite":1},"post")
print(s)

##############################   cours   ##############################

s = testeur("cours1",{"token":"string"},"post")
print(s)

s = testeur("cours2",{"token":"string","id_cours":1},"post")
print(s)

s = testeur("cours3",{"code":"string","reponse":1,"message":"string"},"post")
print(s)

