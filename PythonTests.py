capitals = {"France": "Paris", "Germany": "Berlin", "Italy": "Rome", "Spain": "Madrid" }

# travel_log = {
#     "France": ["Paris", "Lyon", "Marseille"], 
#     "Germany": ["Berlin", "Munich", "Frankfurt"],
#               }
travel_log = {
    "France": {
        "Cities_Visited": ["Paris", "Lyon", "Marseille"],
        "Num_times_Visited" :5,} ,
        
    "Germany": {
        "Cities_Visited": ["Berlin", "Munich", "Frankfurt"],
        "Num_times_Visited" :3,
    },
              }

#nested_list = ["a", "b", ["c", "D"]]
               
print (travel_log["Germany"]["Cities_Visited"][2])
print (travel_log['France']["Num_times_Visited"])