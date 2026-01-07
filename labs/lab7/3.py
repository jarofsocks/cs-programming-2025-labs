personnel = [
    {"name": "Dr. Klein", "clearance": 2},
    {"name": "Agent Brooks", "clearance": 4},
    {"name": "Technician Reed", "clearance": 1}
]
access_levels = {"Restricted" : [1], "Confidential" : [2,3], "Top Secret" : [4,5,6]}
personnel = map(lambda a, b : if a['clearance'] in b['to'], personnel, access_levels)