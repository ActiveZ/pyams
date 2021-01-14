import os
from firebase import firebase
from player_db import player_db

URL = "https://cnam-a8ae6-default-rtdb.europe-west1.firebasedatabase.app/"
firebase = firebase.FirebaseApplication(URL, None)


def create_game(nb_players):
    data = {}
    for i in range(nb_players):
        data["j"+str(i+1)] = player_db
    # print("data", data)
    result = firebase.post("/pyams/scores", data)
    # print("firebase:", result)
    print (result["name"]," game created with",nb_players,"players !\n")
    return result["name"]


def read_game():
    result = firebase.get("/pyams/scores/", "")
    print(result,'\n')
    print("nb games:", len(result),'\n')
    print("Game list:", list(result),'\n')
    # print("db 1:",list(result)[0], '\n')


def update_game(game_id, data):
    data = {
        "name": "joueur 2",
        "dice2" : 6,
        "yams": True
        }
    firebase.put("/pyams/scores/" + game_id,"dice1",666)
    print(game_id,"Updated\n")


def delete_game(game_id):
    firebase.delete("/pyams/scores/", game_id)
    # firebase.delete("/pyams/scores/", "-MR0xxC5lBs9px_jLPvs")
    print(game_id,"Game Deleted\n")


def delete_all_games():
    result = firebase.get("/pyams/scores", "")
    if (result == None): return
    for db in list(result):
        firebase.delete("/pyams/scores/", db)
        print(db,"deleted !\n")


os.system('clear')  # attention, sur ubuntu, remplacer par os.system('clear')
delete_all_games()
create_game(6)
# read_game()
# update_game()
# read_game()
# delete_game()