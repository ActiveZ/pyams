from firebase import firebase


firebase = firebase.FirebaseApplication("https://pyams-f9702-default-rtdb.europe-west1.firebasedatabase.app/", None)
data = {
    "name": "joueur 1",
    "dice1" : 3,
    "full": True
}
result = firebase.post("/table-test", data)
print("firebase:", result)