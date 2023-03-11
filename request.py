import requests

# url = 'http://localhost:5000/predict_api'
url = 'http://localhost:http://127.0.0.1/:80'
r = requests.post(url,json={'potential':89, 'value_eur':98, 'wage_eur':456005, 'age': 89, 'height_cm':155,
'weight_kg': 68, 'pace':87, 'shooting':79, 'passing':97, 'dribbling': 75, 'defending':77, 'physic': 66, 
'attacking_crossing':55, 'attacking_finishing': 75, 'attacking_heading_accuracy': 59, 'attacking_short_passing': 83,
'attacking_volleys': 67, 'skill_dribbling':87, 'skill_curve':53, 'skill_fk_accuracy':79, 'skill_long_passing':53,
'skill_ball_control':72, 'movement_acceleration':91, 'movement_sprint_speed': 67, 'movement_agility':82, 'movement_reactions': 79,
'movement_balance': 64, 'power_shot_power': 40, 'power_jumping': 72, 'power_stamina':63, 'power_strength': 89, 'power_long_shots':61,
'mentality_aggression':75, 'mentality_interceptions': 76, 'mentality_positioning':73, 'mentality_vision':67, 'mentality_penalties':55,
'mentality_composure': 87, 'defending_marking_awareness': 78, 'defending_standing_tackle': 52, 'defending_sliding_tackle':67,
'goalkeeping_diving':56, 'goalkeeping_handling':67, 'goalkeeping_kicking':45, 'goalkeeping_positioning': 65, 'goalkeeping_reflexes':34
})

print(r.json())