level_match = {
 		"A1": 0,
 		"A2": 1,
 		"B1": 2,
 		"B2": 3,
 		"C1": 4,
 		"C2": 5,
 }

user = { 
        "user_id": "0000001",
        "full_name": "Vic Victorovich",
        "login": "Vic584",
        "mail": "apple@apple.com",
        "mobile": "+192738474",
        "level": level_match["B1"],
        "study_for_what": "Travel",
        "date_of_start": "18.05.2022",
 }
 
message = {"user": user,
		     "message_text": "different"}



sentences = [
		{"level": 0, 
			"text": "It's on a different level."},
		{"level": 1, 
			"text": "It is all at a completely different level, man!"},
		{"level": 2, 
			"text": "On a different level, however, it already exists."},
		{"level": 3, 
			"text": "A different level of aesthetic discourse comprises commentary on the riddimplus-voicing system as a whole."},
		{"level": 4, 
			"text": "Access to linguistic knowledge can proceed with different level of cognitive control."},
		{"level": 5, 
			"text": "The use of neuroimaging methods, however, has provided an altogether different level of analysis of plasticity."},
		{"level": 0, 
			"text": "Let's get in out of this cold wind."},
		{"level": 1, 
			"text": "It was cold in the cave."},
		{"level": 2, 
			"text": "One cold winter night I was alone in my room."},
		{"level": 3, 
			"text": "That familiar cold feeling washed over her again with a wave that was staggering."},
		{"level": 4, 
			"text": "At first she nodded agreement, and then a cold feeling clutched at her heart."},
		{"level": 5, 
			"text": "Several battalions of soldiers, in their shirt sleeves despite the cold wind, swarmed in these earthworks like a host of white ants; spadefuls of red clay were continually being thrown up from behind the bank by unseen hands."},
]

user_lvl = message.get("user").get("level")
user_message = message.get("message_text")
user_list = []
result_message = ""

for sentence in sentences:
	if user_lvl >= sentence.get("level") :
			if user_message in sentence.get("text"):
				user_list.append(sentence.get("text"))
			

if not user_list:
	result_message = "Sorry, no sentences for you!"
if len(user_list) == 1:
	result_message = user_list[0]
if len(user_list) > 1:
	for x in user_list:
		result_message += x + "\n...\n"


print(result_message)
