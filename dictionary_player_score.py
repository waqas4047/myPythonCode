scores = {
    "Player1": {"score": 1000, "level": 5, "time_played": 30},
    "Player2": {"score": 500, "level": 3, "time_played": 20},
    "Player3": {"score": 2000, "level": 7, "time_played": 45}
}
print(scores['Player1'])

scores.update({"player4":{"score":4000,"level":4,'time_played':55}})

# .items print the key and value of dictionary in below in play key will store and in score values will store

for player , detail in scores.items():
    print("\n\n")
    print(player)
    for key,value in detail.items():
        print ( f'{key} : {value}')