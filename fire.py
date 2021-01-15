import os
from firebase import firebase
from player_db import player_db

URL = "https://cnam-a8ae6-default-rtdb.europe-west1.firebasedatabase.app/"
firebase = firebase.FirebaseApplication(URL, None)


def create_game(nb_players):
    data = {}
    for i in range(nb_players):
        data["j"+str(i+1)] = player_db.copy()
    # print("data", data)
    result = firebase.post("/pyams/", data)
    # print("firebase:", result)
    print (result["name"]," game created with",nb_players,"players !\n")
    return result["name"]


def get_list_games():
    result = firebase.get("/pyams/", "")
    # print(result,'\n')
    # print("nb games:", len(result),'\n')
    # print("Game list:", list(result),'\n')
    return list(result)


def read_game(game_id):
    result = firebase.get("/pyams/" + game_id, "")
    print("Current game:", result,'\n')


def update_game(game_id, data):
    for k, v in data.items(): # update key, value for all players in data
        firebase.put("/pyams/" + game_id, k, v)
    print(game_id,"updated\n")


def delete_game(game_id):
    firebase.delete("/pyams/", game_id)
    print(game_id,"game deleted\n")


def delete_all_games():
    i = 0
    result = firebase.get("/pyams/", "")
    if (result == None): 
        print("No game to delete")
        return
    for db in list(result):
        firebase.delete("/pyams/", db)
        print(db,"deleted !")
        i += 1
    print(i, "game(s) deleted !\n")


os.system('clear')  # attention, sur ubuntu, remplacer par os.system('clear')

delete_all_games() # efface tous les jeux de la db
create_game(6) # crée un jeu à 6 joueurs
game_list = get_list_games() # récupére la liste des jeux de la db
current_game = game_list[len(game_list) - 1] # le jeu en cours est le dernier de la liste
print("current game:", current_game)
read_game(current_game) # affichage des données du jeu en cours

# nouvelles données
data = {}
j1 = player_db.copy()
j1["name"] = "joueur 1"
data["j1"] = j1
j2 = player_db.copy()
j2["name"] = "joueur 2"
data["j2"] = j2
update_game(current_game, data) # update du jeu en cours

read_game(current_game) # vérification de l'update
# delete_game(current_game) # effacement du jeu en cours