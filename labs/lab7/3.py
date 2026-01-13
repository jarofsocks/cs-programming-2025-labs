personnel = [
    {"name": "Dr. Klein", "clearance": 2},
    {"name": "Agent Brooks", "clearance": 4},
    {"name": "Technician Reed", "clearance": 1}
]
access_levels = {
    '1' : "Restricted" ,
    '2' : "Confidential",
    '3' : "Confidential", 
    '4' : "Top Secret",
    '5' : "Top Secret",
    '6' : "Top Secret",
}

clearence_personnel = map(lambda a : {'name' : a['name'], "clearance" : access_levels[f"{a["clearance"]}"]}, personnel)
for i in clearence_personnel:
    print(i)
