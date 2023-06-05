# The Last Of Us Escape Room

#to run the game: python escape_room.py

#### Libraries used

from PIL import Image           
from playsound import playsound
import streamlit as st

#To install library in terminal follow this https://pillow.readthedocs.io/en/stable/installation.html
#### Rooms

# * orphanage
# * quarantine zone
# * wilderness
# * fireflies lab

#### Common items and main rooms
# define rooms and items

outside = {
  "name": "outside"
}

orphanage = {                          #Sabir's code
    "name": "orphanage",
    "type": "room",
}

quarantine_zone = {                    #Flor's code
    "name": "quarantine zone",
    "type": "room",
}


wilderness = {                         #Geet's code
    "name": "wilderness", 
    "type": "room",
}
 
fireflies_lab = {                      #Andre's code
    "name": "fireflies lab",
    "type": "room",
}

#### Orphanage items
# define rooms and items

bunk_bed = {
    "name": "bunk bed",
    "type": "furniture"
}


doll = {
    "name": "doll",
     "type": "item"
}

door = {
    "name": "door",
    "type": "furniture"
}

window = {
    "name": "window",
    "type": "exit",
    "broken": False
}

hammer = {
    "name": "hammer",
    "type": "item"
}

#### Quarantine zone items
# define rooms and items

first_aid_kit = {
    "name": "first aid kit",
    "type": "furniture",
}

ammo = {
    "name": "ammo",
    "type": "item",
}

warehouse_door = {
    "name": "warehouse door",
    "type": "door",
}


warehouse_key = {
    "name": "key for warehouse door",
    "type": "key",
    "target": warehouse_door,
}

safe = {
    "name": "safe",
    "type": "item",
}

#### Wilderness items
tommys_hideout = {
    "name": "tommys hideout",
    "type": "location",
}

henry_and_sams_hideout = {
    "name":"henry and sams hideout",
    "type": "location",
}

bill_and_franks_place = {
    "name":"bill and franks place",
    "type": "location",
}


infected = { 
    "name": "infected",
    "type": "item",
}

bag = {
    "name": "bag", 
    "type": "item"
}

gun = {
    "name": "gun",
    "type": "weapon",
}

death = {
    "name": " death",
    "type": 'item'
}

knife = {
    "name": "knife",
    "type": "weapon",
}

garage = {
    "name": "fireflies lab garage",
    "type": "door",
}

car = {
    "name": "car to drive to fireflies",
    "type": "item", 
}

car_key = {
    "name": "car with control key to access fireflies lab garage",
    "target": garage, 
}

#### Fireflies lab items
# define rooms and items

labs_door = {
    "name": "lab's door",
    "type": "door",
}

labs_key = {
    "name": "key for lab's door",
    "type": "key",
    "target": labs_door,
}

marlene = {
    "name": "Marlene",
    "type": "person",
}

wooden_box = {
    "name": "wooden box",
    "type": "furniture",
}


grey_box = {
    "name": "grey_box",
    "type": "gun",
    "target": marlene,
}


medical_table = {
    "name": "medical table",
    "type": "furniture",
}

surgical_bed = {
    "name": "surgical bed",
    "type": "furniture",
}

#### Relationships between elements
# define which items/rooms are related

all_rooms = [orphanage , quarantine_zone, wilderness, fireflies_lab, outside]

all_doors = [window, warehouse_door, garage, labs_door] 


object_relations = {
    "orphanage": [doll, door, window, bunk_bed],         
    "hammer": [window],
    "bunk bed": [hammer],
    
    "quarantine zone": [window, first_aid_kit, ammo, warehouse_door, safe],
    "open safe": [warehouse_key],
    
    "wilderness": [henry_and_sams_hideout, bill_and_franks_place, infected, garage, tommys_hideout], 
    "tommys hideout": [car, car_key],
    "henry_and_sams_hideout":[infected],
    "bill_and_franks_place": [bag],
    "infected": [death],
    "bag": [knife, gun],
    
    "fireflies lab": [medical_table, wooden_box, labs_door, surgical_bed], 
    "medical table": [],
    "wooden box": [grey_box],
    "grey box": [marlene],
    "surgical bed": [labs_key],
    "outside": [labs_door],
    
    "window": [orphanage, quarantine_zone],
    "warehouse door": [quarantine_zone, wilderness],
    "fireflies lab garage": [wilderness, fireflies_lab],
    "lab's door": [fireflies_lab, outside],
}

#### Initialize game
# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": orphanage,
    "keys_collected": [],
    "items_collected": [],
    "target_room": outside
}

#### In-game actions
def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    print("Ellie wakes up on a bunk bed in the orphanage. She wants to escape this place as she feels a danger is incoming, but realizes that the door is locked from the outside, so she needs to find another way out.")
    with Image.open("./assets/1_ellie_initial.jpeg") as img: img.show()
    play_room(game_state["current_room"])
    
def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if (game_state["current_room"] == game_state["target_room"]):
        print("You escaped the room, but... Marlene, the leader of the Fireflies, is here and she has a gun!")
        with Image.open("./assets/2_Marlene1.jpg") as img: img.show()
        choice = input("Do you want to speak or shoot her? Quick! (speak/shoot)")
        end_game(choice)                                                                                           #The end of the game is activated
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 1 for 'explore' or 2 for 'examine'?").strip()
        if intended_action == "1":
            explore_room(room)
            play_room(room)
        elif intended_action == "2":
            examine_item(input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean. Type '1' or '2'.")
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))


def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if (not current_room == room):
            return room


def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None

    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if(item["name"] == "safe"):                                                                #Additional interactions with elements
                    open_safe(item_name)
                    return 
                elif(item["name"] == "wooden box"):                                                        #Additional interactions with elements
                    open_box(item_name)
                    return 
                elif(item["name"] == "medical table"):                                                     #Additional interactions with elements
                    open_note(item_name)
                    return 
                elif(item["name"] == "surgical bed"):                                                      #Additional interactions with elements
                    find_ellie(item_name)
                    return
                elif(item["name"] == "window"):
                    if item["broken"]:
                        intended_action = input("The window is broken. Do you want to go through? 'yes' or 'no'")
                        if intended_action == 'yes':
                            next_room = get_next_room_of_door(item, current_room)
                            play_room(next_room)
                            return
                        elif intended_action == 'no':
                            play_room(current_room)
                            return
                    else:
                        if hammer in game_state["items_collected"]:    
                            break_window(item)
                            return
                        else:
                            print("Maybe I can find something to break it with")
                            play_room(current_room)
                            return
                elif(item["name"] == "doll"):
                    print("Looks like a teddy bear")
                    play_room(current_room)
                    return
                elif(item["name"] == "door"):
                    print("The door is locked from the outside, no way to open it")
                    play_room(current_room)
                    return
                elif(item["name"] == "bunk bed"):
                    print("An uncomfortable bed Ellie used to sleep in.")
                    intended_action = input("Do you want to look under the bed. 'yes' or 'no'")
                    if intended_action == "yes":
                        pickup_hammer(item_name)
                        return
                    elif intended_action == "no":
                        play_room(current_room)
                    else:
                        print("Invalid choice. Please enter 'yes' or 'no'.")
                        play_room(current_room)
                                          
                elif(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                    with Image.open("./assets/3_key.jpeg") as img: img.show()
                    playsound("./sounds/car.wav")
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")
    
    if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes'):
        if (game_state["current_room"]['name'] == "quarantine zone"):
            playsound("./sounds/warehousekey.mp3")
            print("This place is plagued with infected people. You need to find out safe place to protect yourself and plan your next step.")
            with Image.open("./assets/4_Ellie_Joel.jpg") as img: img.show()
        elif (game_state["current_room"]['name'] == "wilderness"):
            print("Ellie and Joel finally arrived at the Fireflies' lab, but suddenly… Joel was attacked by some Fireflies members and wakes up in a hospital bed. \nHe was informed that the Fireflies planned to operate on Ellie in order to find a cure for the virus. However, they warned Joel that the chances of Ellie's survival were low. \nSo, Joel made the decision to rescue Ellie!!!")
            with Image.open("./assets/5_FirleFliesLab.jpeg") as img: img.show()
        play_room(next_room)
    else:
        play_room(current_room) 


#### Additional interactions

def pickup_hammer(item_name):
    item_found = object_relations[item_name].pop()
    game_state["items_collected"].append(item_found)
    print("You have found "+item_found["name"]+".")
    with Image.open("./assets/6_hammer.jpeg") as img: img.show()
    play_room(game_state["current_room"])
    
def break_window(item):
    intended_action = input("The found hammer might be able to break the window. Do you want to try and break it? 'yes' or 'no'").strip()
    if intended_action == 'yes':
        window["broken"] = True
        playsound("./sounds/glassbreak.mp3")
        intended_action_2 = input("You broke the window. Do you want to go through? 'yes' or 'no'")
        if intended_action_2 == 'yes':
            with Image.open("./assets/7_warehouse.jpeg") as img: img.show()
            print("After going through the window, Ellie enters a big warehouse where she can read the words 'Quarantine Zone' on the wall, she hides behind a pallet of boxes. \nShe hears a familiar voice, it's her friend Marlene! but oh no!... she is hurt, they were supposed to escape together, but now Marlene needs to get medical attention so she asks Ellie to escape with Joel that was with her. \nEllie doesn't trust him, and she doesn't want to leave Marlene behind, but Marlene asks her to go with him, now they need to decipher a way to get out this place.")
            next_room = get_next_room_of_door(item, game_state["current_room"])
            play_room(next_room)
        elif intended_action_2 == 'no':
            play_room(game_state["current_room"])
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            play_room(game_state["current_room"])
    elif intended_action == 'no':
         play_room(game_state["current_room"])
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        play_room(game_state["current_room"])
        
def open_safe(item_name):
    'The safe contains a key, but to access it you have to open the safe by completing the missing code'
    current_room = game_state["current_room"]
    print("You find a safe. To open it, you have to figure out the missing digits in the pasword. See if there is a pattern behind the numbers shown.")
    intended_action = input("Do you want to try? Enter 'yes' or 'no'").strip()
    if intended_action == "yes":
        with Image.open("./assets/8_safe.jpeg") as img: img.show()
        #print('| 4 | 3 | 9 | 4 | 5 | 7 |')
        #print('| 1 | 0 | 6 | ? | ? | 4 |')
        print("What are the missing digits?")
        first_digit = input('indicate first missing digit ').strip()
        second_digit =  input('indicate second missing digit ').strip() 
        if first_digit == "1" and second_digit == "2":
            playsound("./sounds/safe.mp3")
            playsound("./sounds/keys.mp3")
            safe = {
                "name": "open safe",
                "type": "item",
            }
            item_found = object_relations['open safe'].pop()
            game_state["keys_collected"].append(item_found)
            output = "You opened the safe and found " + item_found["name"] + "."
            with Image.open("./assets/3_key.jpeg") as img: img.show()
            print(output)
            play_room(current_room)
        else:
            print("Incorrect password, safe did not open.")
            play_room(current_room)
    else:
        print('we can check it later then')
        play_room(current_room)
        
def open_box(item_name):
    'You have to decide between two boxes and open one, one explodes and you die, and the other one contains a gun to use later'
    current_room = game_state["current_room"]
    print("You found a wooden box. Inside there are two boxes, a grey one and a black one.")
    with Image.open("./assets/9_wooden_box.jpeg") as img: img.show()
    choice = input("Which box do you want to open? (grey/black)")
    if (choice == "grey"):
        print("You open the grey box and find a gun inside. You add it to your items collection.")
        with Image.open("./assets/10_gun_lab.jpg") as img: img.show()
        item_found = object_relations["grey box"].pop()
        game_state["items_collected"].append(item_found)
        play_room(current_room)
    elif (choice == "black"):
        print("You open the black box and it explodes! You die! - \n YOU LOST")
        playsound("./sounds/explosion.wav")
        with Image.open("./assets/11_bomb.jpeg") as img: img.show()
        game_over()
    else:
        print("Invalid choice.")
        play_room(current_room)
        
def open_note(item_name):
    current_room = game_state["current_room"]
    print("There is a note! \n She is too important for us! We will do everything to protect her!")
    with Image.open("./assets/12_medical_bed.jpeg") as img: img.show()
    play_room(current_room)


def find_ellie(item_name):
    current_room = game_state["current_room"]
    item_found = object_relations["surgical bed"].pop()
    game_state["keys_collected"].append(item_found)
    print("You found Ellie! Now she is with you! And there is also a key for lab's door!")
    with Image.open("./assets/assets/13_Surgical_Table.jpeg") as img: img.show()
    play_room(current_room)              

def end_game (choice):
    current_room = game_state["current_room"]
    if (choice == "speak"):
        print("She does not want to chat! Marlene killed you and she is tacking Ellie with her! - \n YOU LOST")
        with Image.open("./assets/14_Marlene_killed2.jpeg") as img: img.show()
        game_over()
    elif (choice == "shoot"):
        have_gun = False
        for item in game_state["items_collected"]:
            if (item["name"] == "Marlene"):
                have_gun = True
                if (have_gun):
                    playsound("./sounds/gunshot2.mp3")
                    print("You killed Marlene and saved Ellie! Our mission just started... Let´s go! - \n YOU WON")
                    with Image.open("./assets/15_victory_image.jpg") as img: img.show()
                    game_over()
                else:
                    print("You have no bullets! F***! Marlene killed you and she is tacking Ellie with her!! - \n YOU LOST.")
                    with Image.open("./assets/14_Marlene_killed2.jpeg") as img: img.show()
                    game_over()

    else:
        print("Invalid choice. Please enter 'speak' or 'shoot'.")
        play_room(current_room) 
        

def game_over():
    intended_action = input("Want to start over? 'yes' or 'no'")
    if intended_action == 'yes':
        INIT_GAME_STATE = {
            "current_room": orphanage,
            "keys_collected": [],
            "items_collected": [],
            "target_room": outside
        }
        print("Ellie wakes up on a bunk bed in the orphanage. She wants to escape this place as she feels a danger is incoming, but realizes that the door is locked from the outside, so she needs to find another way out.")
        play_room(orphanage)
    else:
        print('Thanks for playing!')

    
    
#### Play
game_state = INIT_GAME_STATE.copy()

start_game()



