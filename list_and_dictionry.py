scores = {
    "Player1": {"score": 1000, "level": 5, "time_played": 30},
    "Player2": {"score": 500, "level": 3, "time_played": 20},
    "Player3": {"score": 2000, "level": 7, "time_played": 45},
    "coch_nname":["jhon","dilsan","boult","jdeja"]
}

# to acces items in list inside dictioanry

print(scores['coch_nname'][2])

# to add new items to  list inside dictionary

scores['coch_nname'].insert(2,"hello")
print(scores["coch_nname"])

# add new list to the dictionary

scores.update({"bowling_choch":['sheda','jado','gamber']})

# to update value in list inside dictionary

print("**********update value*************")
scores["coch_nname"][1]="jakabooo"
print(scores["coch_nname"])

print("********print overrall***********")
print(scores)

