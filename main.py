import textwrap
from pathlib import Path
import pygame
from pygame import mixer

WIDTH, HEIGHT = 1275, 725

BACKGROUND = (255, 255, 255)

ASSETS = Path(__file__).parent / "assets"

class TextAdventure:

    def __init__(self):
        #pygame.mixer.init()
        self.current_input = ""
        self.game_over = False
        self.messages = []

        self.state = "name"

        self.player_name = ""
        self.symbol = None

        #self.background_music1 = pygame.mixer.Sound(
            #str(ASSETS / "music1.wav")
        #)

        #self.car_woosh = pygame.mixer.Sound(
            #str(ASSETS / "car woosh.wav")
        #)

        #self.buzz = pygame.mixer.Sound(
            #str(ASSETS / "buzzing.wav")
        #)

        #self.item = pygame.mixer.Sound(
            #str(ASSETS / "important item or selection.wav")
        #)

        #self.BC_Buzzing = pygame.mixer.Sound(
            #str(ASSETS / "BC_Buzzing.wav")
        #)

        #self.Enemy = pygame.mixer.Sound(
            #str(ASSETS / "enemy_audio.wav")
        #)
        
    def write(self, message=""):
            self.messages.append(str(message))

    FONT_FILE = ASSETS / "font.ttf"
    
    def play_music(self, audio):
        #audio.play()
        pass
    
    def stop_music(self, audio):
        #audio.stop()
        pass

    def handle_command(self, command):
        command = command.strip()

        if self.state == "name":
            self.player_name = command
            self.write(f"Hello {self.player_name}!")
            self.write("")
            self.write("Choose your symbol:")
            self.write("1 = A Sparkling Six-Leafed Clover")
            self.write("2 = A Sparkling Green Light")
            self.write("3 = A Sparkling Hammer")
            self.write("Type 1, 2, or 3 to select your symbol.")
            self.write()
            self.state = "symbol"
            return
        
        if self.state == "symbol":
            if command in ["1", "2", "3"]:
                self.symbol = command
                if command == "1":
                    self.write("A Sparkling Six-Leafed Clover")
                    self.write("Six Leaves? You must be quite lucky...")
                if command == "2":
                    self.write("A Sparkling Green Light")
                    self.write("Shine bright. You will never be alone when it's dark...")
                if command == "3":
                    self.write("A Sparkling Hammer")
                    self.write("Convenient and reliable. You stand strong against adversity...")
                self.write()
                self.write("Type 'Begin' to begin.")
                self.write()
                self.state = "start"
            else:
                self.write("Please type 1, 2, or 3.")
            return
        
        if self.state == "start":
            if command.upper() == "BEGIN":
                self.beginning_p1()
                return
            else:
                self.write("Type 'Begin' to begin.")
                self.write()
                return
        
        if self.state == "beginning_p1":
            if command.upper() == "RUN":
                self.beginning_p1()
                return
            else:
                self.write("Type 'RUN' to continue.")
                self.write()
                return

        if self.state == "beginning_p2":
            if command.upper() == "RUN":
                self.beginning_p2()
                return
            else:
                self.write("Type 'RUN' to continue.")
                self.write()
                return

        if self.state == "beginning_p3":
            if command.upper() == "RUN":
                self.beginning_p3()
                return
            else:
                self.write("Type 'RUN' to continue.")
                self.write()
                return

        if command == "help" or command == "Help":
            self.write("Commands:")
            self.write("North, South, East, West")
            self.write("Inspect/Interact, Take, Look, Quit")
            self.write()
            self.write("Certain locations have location-specific commands.")
            self.write()

        if command == "quit" or command == "Quit":
            self.write("Thanks for playing!")
            self.game_over = True

        if self.state == "DuPont_Library_room1":
            if command == "":
                self.DuPont_Library_room1()
                return
            if command == "north" or command == "North":
                self.DuPont_Library_room2()
                return
            if command == "help" or command == "Help":
                return
            if command == "skip":
                self.write()
                self.write()
                self.write()
                self.write()
                self.write()
                self.write()
                self.write()
                self.write()
                self.write()
                self.Bishops_Commons()
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "DuPont_Library_room2":
            if command == "south" or command == "South":
                self.DuPont_Library_room1()
                return
            elif command == "east" or command == "East":
                self.DuPont_Library_Elevator_Enterance()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "DuPont_Library_Elevator_Enterance":
            if command == "south" or command == "South":
                self.DuPont_Library_Elevator()
                return
            elif command == "east" or command == "East":
                self.DuPont_Library_room3()
                return
            elif command == "west" or command == "West":
                self.DuPont_Library_room2()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "DuPont_Library_Elevator":
            if command == "south" or command == "South":
                self.DuPont_Library_Stairs()
                return
            elif command == "north" or command == "North":
                self.DuPont_Library_Elevator_Enterance()
                return
            elif command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect": 
                self.Elevator_Inspect()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "DuPont_Library_Stairs":
            if command == "north" or command == "North":
                self.DuPont_Library_Elevator()
                return
            elif command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect": 
                self.DuPont_Library_Stairs_Int()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "DuPont_Library_Stairs_Int":
            if command == "north" or command == "North":
                self.DuPont_Library_Elevator()
                return
            elif command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.write("We already know what happens...")
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "DuPont_Library_room3":
            if command == "north" or command == "North":
                self.DuPont_Enterance_Right()
                return
            elif command == "west" or command == "West":
                self.DuPont_Library_Elevator_Enterance()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "DuPont_Library_room1":
            if command == "south" or command == "South":
                self.DuPont_Library_room2()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "DuPont_Enterance_Right":
            if command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.write("The door is locked. You can't go through it.")
                self.write("There is another door to the East. You can go back North.")
                self.write()
                return
            elif command == "help" or command == "Help":
                return
            elif command == "east" or command == "East":
                self.DuPont_Enterance_Left()
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "DuPont_Enterance_Left":
            if command == "south" or command == "South":
                self.Table_Room()
                return
            elif command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.DUL_int()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "DUL_int":
            if command == "south" or command == "South":
                self.Table_Room()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "room_to_staircase2":
            if command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.staircase2()
                return
            elif command == "help" or command == "Help":
                return
            elif command == "south" or command == "South":
                self.Table_Room2()
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "staircase2":
            if command == "south" or command == "South":
                self.Table_Room()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Table_Room2":
            if command == "north" or command == "North":
                self.Coffee_Shop_Bait()
                return
            elif command == "east" or command == "East":
                self.Grand_Room()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Coffee_Shop_Bait":
            if command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.Golden_Paper()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return
        
        if self.state == "Table_Room":
            if command == "west" or command == "West":
                self.writing_center()
                return
            elif command == "help" or command == "Help":
                return
            elif command == "north" or command == "North":
                self.room_to_staircase2()
                return
            elif command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.Bookcase_1()
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Bookcase_1":
            if command == "gaze" or command == "Gaze":
                self.purple_paper()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("Gaze. No other option.")
                return

        if self.state == "purple_paper":
            if command == "north" or command == "North":
                self.room_to_staircase2()
                return
            elif command == "help" or command == "Help":
                    return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "writing_center":
            if command == "west" or command == "West":
                self.outside_Cup_And_Gown_Cafe()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "outside_Cup_And_Gown_Cafe":
            if command == "south" or command == "South":
                self.Cup_And_Gown_Cafe()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Cup_And_Gown_Cafe":
            if command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.Golden_Paper()
                return 
            elif command == "help" or command == "Help":
                return 
            if command == "east" or command == "East":
                self.outside_Cup_And_Gown_Cafe()
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Cup_And_Gown_Till":
            if command == "go around" or command == "Go around" or command == "Go Around":
                self.Golden_Paper()
                return
            if command == "help" or command == "Help":
                self.write("Try the command 'go around'.")
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Golden_Paper":
            if command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.Facti()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Facti":
            if command == "north" or command == "North":
                self.Facti_Leave()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Facti_Leave":
            if command == "help" or command == "Help":
                self.write("Try the command 'look'.")
                self.write()
                return
            if command == "look" or command == "Look":
                self.Gold_Exit()
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Gold_Exit":
            if command == "help" or command == "Help":
                self.write("Try the command 'enter'.")
                self.write()
                return
            if command == "enter" or command == "Enter":
                self.BC_Gold()
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "BC_Gold":
            if command == "west" or command == "West":
                self.Bishops_Commons_West()
                return
            elif command == "east" or command == "East":
                self.Bishops_Commons_East()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "door_to_Bishops_Commons":
            if command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.door_to_Bishops_Commons_inspect()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "door_to_Bishops_Commons_inspect":
            if command == "enter" or command == "Enter":
                self.Bishops_Commons()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Bishops_Commons":
            if command == "west" or command == "West":
                self.Bishops_Commons_West()
                return
            if command == "east" or command == "East":
                self.Bishops_Commons_East()
                return
            elif command == "help" or command == "Help":
                return
            if command == "skip":
                self.write()
                self.write()
                self.write()
                self.write()
                self.write()
                self.write()
                self.write()
                self.Cemetery_Purple()
                return
            if command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.write("Nothing to do here.")
                return
            else:
                self.write("You hit a wall. Can't you see anything?")
                return

        if self.state == "Bishops_Commons_West":
            if command == "east" or command == "East":
                self.Bishops_Commons()
                return
            elif command == "help" or command == "Help":
                return
            if command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.Bishops_Commons_West_Door()
                return
            else:
                self.write("You hit a wall. Can't you see anything?")
                return

        if self.state == "Bishops_Commons_East":
            if command == "west" or command == "West":
                self.Bishops_Commons()
                return
            if command == "north" or command == "North":
                self.Staircase_Door()
                return
            if command == "south" or command == "South":
                self.Foosball_Table()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You hit a wall. Can't you see anything?")
                return

        if self.state == "Staircase_Door":
            if command == "south" or command == "South":
                self.Bishops_Commons_East()
                return
            if command == "north" or command == "North":
                self.Staircase3()
                return
            if command == "east" or command == "East":
                self.Glowey_Door()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You hit a wall. Can't you see anything?")
                return

        if self.state == "Staircase3":
            if command == "north" or command == "North":
                self.Staircase_Death_Ending()
                return
            if command == "south" or command == "South":
                self.Staircase_Door()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Foosball_Table":
            if command == "play" or command == "Play":
                self.Foosball_Table_Play()
                return
            if command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.Foosball_Table_Interact()
                return
            if command == "south" or command == "south":
                self.Gold_Wall_1()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Foosball_Table_Play":
            if command == "back" or command == "Back":
                self.Foosball_Table()
                return
            if command == "help" or command == "Help":
                self.write("Try the command 'back'.")
                self.write()
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Foosball_Table_Interact":
            if command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.Foosball_Table_Interact_2()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Foosball_Table_Interact_2":
            if command == "collect" or command == "Collect":
                self.take_figureine()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "take_figureine":
            if command == "north" or command == "North":
                self.figureine_door()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "figureine_door":
            if command == "north" or command == "North":
                self.Figureine_Staircase()
                return
            if command == "east" or command == "East":
                self.Glowey_Door_Unlocked()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Glowey_Door_Unlocked":
            if command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                True
            if command == "west" or command == "West":
                self.GDK_West()
                return
            if command == "east" or command == "East":
                self.GDK_East()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "GDK_West":
            if command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.write("Would you like to interact with the headset or the paper?")
                self.write()
                if command == "headset" or command == "Headset":
                    self.Headset()
                    return
                if command == "paper" or command == "Paper":
                    self.Purple_Paper()
                    return
                elif command == "help" or command == "Help":
                    return
                else:
                    self.write("You can't do that here.")
                    return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "GDK_East":
            if command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.GDK_East_Interact()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Gold_Wall_1":
            if command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.Gold_Wall_2()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Gold_Wall_2":
            if command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.Gold_Wall_3()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Gold_Wall_3":
            if command == "interact" or command == "Interact" or command == "inspect" or command == "Inspect":
                self.Gold_Wall_4()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Gold_Wall_4":
            if command == "run" or command == "Run" or command == "RUN":
                self.Gold_Wall_Stairs()
                return
            elif command == "help" or command == "Help":
                return
            else:
                self.write("You can't do that here.")
                return

        if self.state == "Gold_Wall_Stairs":
            if command == "down" or command == "Down":
                self.Cemetery_Gold()
                return
            elif command == "help" or command == "Help":
                self.write("Try the command 'down'.")
                return
            else:
                self.write("You can't do that here.")            
                
    def beginning_p1(self):
        self.write("You're late for class! Why, oh, why have you selected to live in") 
        self.write("Benedict Hall. You are the farthest away from Gailor and you have")
        self.write("5 minutes to get to class. You don't own a bike because your")
        self.write("parents said it wouldn't fit in the car. You don't have a car")
        self.write("because you are terrified to crash. So RUN!")
        self.write()
        self.write("Type 'RUN' to continue.")
        self.write()
        self.state = "beginning_p2"

    def beginning_p2(self):
        self.write("You hear the door slam shut behind you as you leave Benedict, but") 
        self.write("who cares. The fastest route to Gailor is through Georgia Avenue,")
        self.write("so without hesitation you hit the crosswalk. The faint sound of")
        self.write("distant cars are heard. For some reason the sound is getting") 
        self.write("louder...You must keep running or else you'll be late.")
        self.write()
        self.write("Type 'RUN' again.")
        self.write()
        #self.stop_music(self.background_music1)
        self.state = "beginning_p3"

    def beginning_p3(self):
        #self.play_music(self.car_woosh)
        self.write("A group of slow-walking freshman are blocking the crosswalk. Nice.")
        self.write("No time to wait, so you must cross the road. Rushing across the")
        self.write("pathway, there's nobody to hold you back. Freedom is fun, but scary.")
        self.write()
        self.write("nobody is there to protect you.")
        self.write()
        self.write("Press ENTER to continue.")
        self.write()
        self.state = "DuPont_Library_room1"

    def DuPont_Library_room1(self):
        #self.play_music(self.buzz)
        self.write("DuPont_Library")
        self.write()
        self.write("You're in a library. Rows and rows of shelves, containing books lined ahead of you. The")
        self.write("whir of limelight whistles above you, faint screeches of chairs being pulled out, and faint")
        self.write("footsteps surrounding. It's a cozy space, cold yet comforting. This is your start, where")
        self.write("everything about you will start.")
        self.write("(Type 'help' for possible commands)")
        self.write()
        self.state = "DuPont_Library_room1"

    def DuPont_Library_room2(self):
        self.write("You walk North, farther into the depths of the library. The walls close you into a corner.")
        self.write("You can move East or back South.")
        self.write()
        self.state = "DuPont_Library_room2"

    def DuPont_Library_Elevator_Enterance(self):
        self.write("As you walk East, you see an opening to your South. Through the")
        self.write("opening, you can see a small elevator and a staircase. There is")
        self.write("more room to continue East.")
        self.write()
        self.state = "DuPont_Library_Elevator_Enterance"

    def DuPont_Library_Elevator(self):
        self.write("In this room, there is an elevator. South, there are some stairs.")
        self.write()
        self.state = "DuPont_Library_Elevator"

    def Elevator_Inspect(self):
        self.write("The elevator doesn't jostle or whir. You didn't notice the yellow")
        self.write("'DO NOT USE' tape. Or at least the 'ESU TON OD' tape. You always")
        self.write("look over the little things.")
        self.write()
        self.state = "DuPont_Library_Elevator"

    def DuPont_Library_Stairs(self):
        self.write("You approach the stairs. It looks very old and rickety. The light")
        self.write("is quite dim, so you can't really see what is in front of you.")
        self.write()
        self.state = "DuPont_Library_Stairs"

    def DuPont_Library_Stairs_Int(self):
        self.write("You go up the stairs… You hit a wall. The steps seem to just")
        self.write("disappear into the roof. There is nowhere to go but DOWN.")
        self.write()
        self.state = "DuPont_Library_Stairs_Int"

    def DuPont_Library_room3(self):
        self.write("You continue past the elevator room, and a wall halts your progress")
        self.write("to the East. You can go North or back West.")
        self.write()
        self.state = "DuPont_Library_room3"
        
    def DuPont_Enterance_Right(self):
        self.write("Library Foyer")
        self.write()
        self.write("A door lies ahead. You can continue East or interact with the door.")
        self.write()
        self.state = "DuPont_Enterance_Right"

    def DuPont_Enterance_Left(self):
        self.write("Once again, a door lies ahead.")
        self.write()
        self.state = "DuPont_Enterance_Left"

    def DUL_int(self):
        self.write("Locked again. There is an opposite entrance, heading back inside the library to the South.")
        self.write()
        self.state = "DUL_int"
        
    def room_to_staircase2(self):
        self.write("The room is empty, on the left end of the wall is a staircase. South leads to a large open room.")
        self.write()
        self.state = "room_to_staircase2"

    def staircase2(self):
        self.write("You get up the stairs...")
        self.write()
        self.write("You hit another wall. What's the use of being here if you don't learn from your mistakes?")
        self.write()
        self.state = "staircase2"

    def Table_Room(self):
        self.write("Table Room")
        self.write()
        self.write("Reentering the library. You're in a different room, couches look thrown around.")
        self.write("Desks strewn across the room. A stray bookcase along the wall. A door is North of you")
        self.write("and there is an opening to the West.")
        self.write()
        self.state = "Table_Room"

    def Table_Room2(self):
        self.write("It probably goes nowhere anyway. A lit up room is NORTH of you. It smells of expired coffee.")
        self.write("A break in the wall is East of you. People are talking inside.")
        self.write()
        self.state = "Table_Room2"

    def Grand_Room(self):
        self.write("This room is grand, bigger than the entrance. It seems to split in the middle with the length.")
        self.write("Desks are stacked in a huge pile, the stack seems to ascend further into the ceiling. Wheeled")
        self.write("whiteboards linger in corners of the room, headphones collapsed onto the floor. There is a tall")
        self.write("poster collapsed on the floor, the words are barely legible, but the only letters legible are a")
        self.write("W, an R, an I, and a T.")
        self.write()
        self.write("People are speaking in here, pulsing up and down in volume. Locked doors are along the walls,")
        self.write("windows are tinted. No one is inside.")
        self.write()
        self.state = "Grand_Room"

    def Coffee_Shop_Bait(self):
        self.write("You enter a room alike to a coffee shop. You have what you need already. There is no one behind the")
        self.write("till. Coffee is expired. Machines aren't functional. You should just keep going.")
        self.write()
        self.state = "Coffee_Shop_Bait"

    def Bookcase_1(self):
        self.write("You thumb through the books on the shelf. Titles of each")
        self.write("book are blurred or flipped in text. It's like you're inside") 
        self.write("a photograph, each item frozen in place, no book will open,")
        self.write("seemingly glued shut. Your hands grace a purple sheet of paper.") 
        self.write()
        self.write("Gaze upon it?")
        self.write()
        self.state = "Bookcase_1"

    def purple_paper(self):
        #self.play_music(self.item)
        self.write("The paper reads, 'campus.' This seems notable enough to keep in mind.")
        self.write()
        self.state = "purple_paper"

    def writing_center(self):
        self.write("This room is grand, bigger than the entrance. It seems to split in the")
        self.write("middle with the length. Desks are stacked in a huge pile, the stack")
        self.write("seems to ascend further into the ceiling. Wheeled whiteboards linger")
        self.write("in corners of the room, headphones collapsed onto the floor. There is")
        self.write("a tall poster collapsed on the floor, the words are barely legible, but")
        self.write("the only letters legible are a W, an R, an I, and a T. People are speaking in")
        self.write("here, pulsing up and down in volume. Locked doors are along the walls,")
        self.write("windows are tinted. No one is inside.")
        self.write()
        self.write("You may only exit from here. There is a smell of expired coffee, West of you.")
        self.write()
        self.state = "writing_center"

    def outside_Cup_And_Gown_Cafe(self):
        self.write("The smell of expired coffee intensifies. You can see the source of the smell is")
        self.write("South of you.")
        self.write()
        self.state = "outside_Cup_And_Gown_Cafe"

    def Cup_And_Gown_Cafe(self):
        self.write("You enter a room alike to a coffee shop. You have what you need already.")
        self.write("There is no one behind the till. Coffee is expired. Machines aren't functional.")
        self.write("You should just keep going.")
        self.write()
        self.state = "Cup_And_Gown_Cafe"

    def Cup_And_Gown_Till(self):
        self.write("There is a till, a countertop. You may go around, for no reason at all.")
        self.write()
        self.state = "Cup_And_Gown_Till"

    def Golden_Paper(self):
        self.write("There is a golden sheet of paper. Inspect it?")
        self.write()
        self.state = "Golden_Paper"

    def Facti(self):
        #self.play_music(self.item)
        self.write("The paper reads, 'facti.' This seems significant enough to write down somewhere.")
        self.write()
        self.state = "Facti"

    def Facti_Leave(self):
        self.write("You turn around. Reentering the library. You're in a different room, couches look thrown around.")
        self.write("Desks strewn across the room. A stray bookcase along the wall.")
        self.write()
        self.state = "Facti_Leave"

    def Gold_Exit(self):
        self.write("There is a staircase on your right. It casts into a shadow further down. You've learned. Why try?")
        self.write("There is nowhere to go. Why would you want to leave?")
        self.write()
        self.state = "Gold_Exit"

    def BC_Gold(self):
        self.write("This wasn't an exit. The second floor of Bishop? It smelled rotten. You can hear the buzzing of")
        self.write("mosquitoes and bees outside. The red carpet peels up at the edges. Posters and photos along the")
        self.write("walls, they look mildly familiar. To each other. The text is flipped, you don't know what they are")
        self.write("smiling about, or if they're smiling at all. Looking close, their faces are blurred to mosaics.")
        self.write()
        self.state = "BC_Gold"

    def door_to_Bishops_Commons(self):
        self.write("You examine the scene around you. Couches are assorted in placement. Desks in the")
        self.write("same way. The bookcase you searched along the side. The unlocked door is beside you.")
        self.write()
        self.state = "door_to_Bishops_Commons"

    def door_to_Bishops_Commons_inspect(self):
        self.write("There is a staircase. It casts into a shadow further down. It's time to see more. See through my eyes. Go.")
        self.write()
        self.state = "door_to_Bishops_Commons_inspect"

    def Bishops_Commons(self):
        #self.play_music(self.BC_Buzzing)
        self.write()
        self.write("You're home. Finally. Home. There's the familiar buzzing of") 
        self.write("mosquitoes and bees outside. There's that moldy smell. There's")
        self.write("the peeling red carpet. Photos of your familiar members on the")
        self.write("wall, backwards text on each flier. Looking closer, the faces") 
        self.write("are off center too. You live here. You will live here. What") 
        self.write("matters now? You're home.")
        self.write()
        self.state = "Bishops_Commons"

    def Bishops_Commons_East(self):
        self.write("The first thing you see are two barracaded doors. Are you going to try to")
        self.write("open this door? Or will you move on?")
        self.write()
        self.write("There are two opposing hallways, one towards the west, and the other towards the East")
        self.state = "Bishops_Commons_East"

    def Staircase_Door(self):
        self.write("You approach the staircase door. You stand staring at it, it's open. For once, a door has opened for you")
        self.write("to the North. Standing there, you may also enter the glowing door to the East.")
        self.write()
        self.state = "Staircase_Door"

    def Staircase3(self):
        self.write("You choose to go forward to the staircase. You start to go down until")
        self.write("you realize that there are no more steps. You look up and find yourself")
        self.write("about to pencil dive into a pit. This is probably not the way to go.")
        self.write()
        self.write("Be careful.")
        self.state = "Staircase3"

    def Staircase_Death_Ending(self):
        self.write("You've chosen to give up. You pencil dive into the pit. The pit was 8")
        self.write("stories, your feet crumble beneathe you, and your brain explodes, you")
        self.write("idiot.")
        self.write()
        self.game_over = True

    def Glowey_Door(self):
        self.write("You approach the door. You can see inside that there's a lot to search.")
        self.write("You try to turn the door but it doesn't budge. Maybe you're forgetting")
        self.write("something? Or someone? There's a staircase that you can do down, and there")
        self.write("are locations to the north and east you can explore.")
        self.write()
        self.state = "Glowey Door"
    
    def Bishops_Commons_West(self):
        self.write("The first thing you see are wide doors to a staircase. It gleams")
        self.write("with hope. A bright, almost blinding light beaming through the windows.")
        self.write()
        self.state = "Bishops_Commons_West"

    def Bishops_Commons_West_Door(self):
        self.write("This door does not budge. Maybe you should stop trying to open doors.")
        self.write()
        self.state = "Bishops_Commons_West_Door"

    def Bishops_Commons_West2(self):
        self.write("Stepping back, you see two hallways west and east of you. Along the walls are")
        self.write("spreads of some newspaper. 'PURPLE' in bold letters. It makes you uneasy. You")
        self.write("can't read the words on the newspaper but, it seems like a lot is going on. West")
        self.write("of you, the hallway ends. East of you, there is an open door. You may also inspect the walls.")
        self.write()
        self.state = "Bishops_Commons_West2"

    def Foosball_Table(self):
        self.write("As you approach, you hear was sounds like scattering little ants or a")
        self.write("dragging beaded necklace. The sound slows and you see instead the players")
        self.write("of foosball, stiffening as you look at them. A ball rolls into the goal.")
        self.write()
        self.state = "Foosball_Table"

    def Foosball_Table_Play(self):
        self.write("You play with the foosball. Who are you playing with? You are just")
        self.write("making it easier for yourself. Alone, you aren't winning or losing.")
        self.write("You're just beating yourself. Don't make stupid choices.")
        self.write()
        self.state = "Foosball_Table_Play"

    def Gold_Wall_1(self):
        self.write("You run into a wall. Of course you do.")
        self.write()
        self.write("There's nothing here. Why are you insistent on running into walls.")
        self.write()
        self.state = "Gold_Wall_1"

    def Gold_Wall_2(self):
        self.write("You feel the wall. That's great, look at you go. Touching everything.")
        self.write("You do remember the smell of mold, don't you? There's still newpaper.")
        self.write("It's all yellow and gross, the pages crumble as you touch. While you're")
        self.write("touching everything, there's a gold paper hiding under the newspaper.")
        self.write()
        self.state = "Gold_Wall_2"

    def Gold_Wall_3(self):
        #self.play_music(self.item)
        self.write("The paper reads, 'sunt.' This seems significant to write down somewhere. The")
        self.write("sound of a fire lighting sounds behind you. And then the sound of groaning")
        self.write("You look back and find what looks like a monstrous form of your roommate")
        self.write("back in Benedict, slowly wading towards you. A door behind them unlocks.")
        self.write()
        self.state = "Gold_Wall_3"

    def Gold_Wall_4(self):
        #self.play_music(self.Enemy)
        self.write("You dart past her, rushing right for the door. She cries and groans for you,")
        self.write("adjusting to follow you. You manage to get to the door. The one that refused")
        self.write("to open. Your hope is briefly heightened before shortening again. You were")
        self.write("fooled, weren't you. Would you give in to that again?")
        self.write()
        self.write("Would you give in to me?")
        self.state = "Gold_Wall_4"

    def Roommate_Death_Ending(self):
        self.write("You stop and stay. The monstrous form of your roommate charges for you and")
        self.write("pulls you back by the arm. She picks you up with a renewed strength, her")
        self.write("face is pulled apart, her jaw locked open.")
        self.write()
        self.write("She bites your head off.")
        self.write()
        self.game_over = True

    def Gold_Wall_Stairs(self):
        #self.stop_music(self.Enemy)
        self.write("You pull forcefully on the door, it opens easily so essentially, you toss")
        self.write("yourself back, your roomate's huge hands graze your spine, just before")
        self.write("you manage to slip through the door. And slam it shut. Manners much?")
        self.write("You turn around and find another set of stairs, one going up")
        self.write("(you find it clipped into the roof.)")
        self.write("and the rest going down.")
        self.write()
        self.state = "Gold_Wall_Stairs"

    def Cemetery_Gold(self):
        self.write("You find yourself facing a barricaded gate. You try to push at the doors, they don't budge. No matter how")
        self.write("hard you push, the doors stay shut. There's another way for certain. You turn around and find yourself in")
        self.write("the University Cemetary. This must be the end of this strange place. Rows and rows of stones lay ahead of you.")
        self.write("The cobble shuffling beneath you. You won't look back. Trees stand overhead, bare and looming. Do you remember")
        self.write(" what brought you here? Names whirl around you, people, family?")
        self.write()
        self.state = "Cemetery_Gold"
        self.game_over = True

    def Foosball_Table_Interact(self):
        self.write("You choose to analyze the foosball table. You look really classy,")
        self.write("hunched over on your knees, trying to find something. Each player is")
        self.write("dressed a dark purple and gold. It's cute, isn't it cute?")
        self.write()
        self.state = "Foosball_Table_Interact"

    def Foosball_Table_Interact_2(self):
        self.write("You reach in and start adjusting each of the players. You correct them")
        self.write("to their standing positions. You're just about to stop, when one of the")
        self.write("players... weigh differently. It falls as you try to turn it upright.")
        self.write()
        self.state = "Foosball_Table_Interact_2"

    def take_figureine(self):
        self.write("You take the figurine. You turn it around in your hand and find what")
        self.write("looks to be a key. You hear a doorknob twist NORTH of you.")
        self.write()
        self.state = "take_figureine"

    def figureine_door(self):
        self.write("You approach the staircase door. You stand staring at it,")
        self.write("it's open. For once, a door has opened for you. Standing")
        self.write("there, you may also enter the glowing door to the East.")
        self.write()
        self.state = "figureine_door"

    def Figureine_Staircase(self):
        self.write("You choose to go forward to the staircase. You start to go down until")
        self.write("you realize that there are no more steps. You look up and find")
        self.write("yourself about to pencil dive into a pit. This is probably not the way")
        self.write("to go. You should go south and try the only closed door that will")
        self.write("probably need a key...")
        self.write()
        self.state = "Staircase4"

    def Glowey_Door_Unlocked(self):
        self.write("You approach the glowing door. You test the knob. Yep. It's locked. Thankfully, you have a key.") 
        self.write("You insert the key into the keyhole and twist. The door pops open. Inside, you are met with a")
        self.write("dorm-sized room. You can distinctly hear music playing beside you. Ahead is a classy bookcase,")
        self.write("on it, sits a TV. It's running on static. On the sides of the room are two desks. This room's")
        self.write("walls are covered in windows to the outside.")
        self.write()
        self.state = "Glowey_Door_Unlocked"

    def GDK_Bookcase(self):
        self.write("You head to the bookcase. Again, none of the books seem attainable. You continue your search.")
        self.write("You try to tug each book apart, but nothing budges. Nothing is here.")
        self.write()
        self.state = "GDK_Bookcase"

    def GDK_Window(self):
        self.write("You look through the windows. It's the sky. Quite blue actually. You are in the sky.")
        self.write()
        self.state = "GDK_Window"

    def GDK_West(self):
        self.write("You head to the west desk. There's a headset sitting on the desk, underneath that a purple paper.")
        self.write("You can hear a beautiful orchestra playing from the headset. It's a sweet, nostalgic play. It")
        self.write("a sweet, nostalgic play. it reminds you of home. you are home.")
        self.write()
        self.state = "GDK_West"

    def Headset(self):
        #self.play_music(self.item)
        self.write("You pick up the headset.")
        self.write()
        self.state = "Headset"

    def Purple_Paper(self):
        #self.play_music(self.item)
        self.write("You pick up the purple paper. On it reads 'nostier.' You should remember this.")
        self.write()
        self.state = "Purple_Paper"

    def Dorm_Sized_Room(self):
        self.write("You turn around to find yourself in a inside the dorm-sized room. You can distinctly hear")
        self.write("music playing beside you. Ahead is a classy bookcase, on it, sits a TV. It's running on static.")
        self.write("On the sides of the room are two desks. This rooms walls are covered in windows to the outside.")
        self.write("You have what you need. You should leave.")
        self.write()
        self.state = "Dorm_Sized_Room"

    def Cemetery_Purple(self):
        self.write("You've reached your resolution. Your end. Rows and rows of stones")
        self.write("lay ahead of you. The cobble shuffling beneath you. You won't look")
        self.write("back. There's nothing more than this, than finality. The greenery of")
        self.write("the forest surrounds your new home. People will remember you by")
        self.write("when you died. And that is all. Names whirl around you, people,")
        self.write("family. Trees provide shade to some rocks. You have nothing more to")
        self.write("you. You like it in here.")
        self.write()
        self.write("Trees stand in varying colors, some green, some orange, some lively,")
        self.write("some bare. Gravestones are practically nameless, engravings grown")
        self.write("over with time cloaked by lichen and moss. The gravel path is littered")
        self.write("with crunchy dead leaves, undettered by the billowing winds.")
        self.write()
        self.state = "Cemetary_Purple"

    def GDK_East(self):
        self.write("You head to the east desk. on it sits a thick yearbook:")
        self.write("TIGERS 1879(mahala ward)/1907(willie six/1935(kennerly's)")
        self.write()
        self.state = "GDK_East"

    def GDK_East_Interact(self):
        self.write("Just like the books in the library bookcase. You flip the cover and flip the whole book.")
        self.write()
        self.state = "GDK_East_Interact"

    def Glowey_Door_Bookcase_Interact(self):
        self.write("You head to the bookcase. Again, none of the books seem attainable. You continue your search.")
        self.write("You try to tug each book apart, but nothing budges. Nothing is here.")
        self.write()
        self.state = "Glowey_Door_Bookcase_Interact"

    def ST_Marks_Cemetery(self):
        self.write("The entire cemetery was pretty divided, grouped up however. Each")
        self.write("grave had a friend. But looking ahead, the trail dips a few feet,")
        self.write("dwindling, before displaying the separate plot of land. There aren't")
        self.write("many graves here. Three TAYLOR graves sit along the trail, grouped")
        self.write("up and decorated. There are a few other graves scattered about,")
        self.write("small orange flags billowing across the field. Along the edge of the")
        self.write("isolated cemetery, a border of collapsed and misplaced rocks.")
        self.state = "ST_Marks_Cemetery"

    async def run(self):
        print("RUN STARTED")
        pygame.init()
        print("PYGAME INIT DONE")
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        print("SCREEN CREATED")
        pygame.display.set_caption("Trails We Want(And The Ones We Take)")
        background_color = (255, 255, 255)
        font = pygame.font.Font(str(self.FONT_FILE), 30)
        print("FONT CREATED")
        clock = pygame.time.Clock()
        command = ""
        running = True

        print("pygame initialized:", pygame.get_init())

        print(self.messages)

        #self.play_music(self.background_music1)

        self.write("Welcome to Sewanee! We are so excited to have you here.")
        self.write("Before we begin, we need to ask you a few questions.")
        self.write("Who are you?")
        self.write()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif not self.game_over:
                        if event.key == pygame.K_RETURN:
                            self.write("> " + command)
                            self.handle_command(command)
                            command = ""
                        elif event.key == pygame.K_DELETE:
                            command = ""
                        elif event.key == pygame.K_BACKSPACE:
                            command = command[:-1]
                        elif event.unicode.isprintable():
                            command = (command + event.unicode)[:60]

            screen.fill(background_color)

            lines = []
            for message in self.messages:
                lines.extend(textwrap.wrap(message, width=110) or [""])
            for index, line in enumerate(lines[-17:]):
                surface = font.render(line, True, (128, 0, 128))
                screen.blit(surface, (24, 20 + index * 30))

            if self.game_over:
                prompt = "Game ended. Refresh to restart; Esc closes the game."
            else:
                prompt = "> " + command + "_"
            surface = font.render(prompt, True, (0, 0, 0))
            screen.blit(surface, (24, HEIGHT - 50))
            pygame.display.flip()
            await asyncio.sleep(0)
            clock.tick(30)

        pygame.quit()

def wrap_text(text, font, max_width):

    if not text:
        return [""]
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = word if not current else current + " " + word
        if font.size(test)[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

def draw_game(screen, font, small_font, game):
    screen.fill((255, 255, 255))
    screen.blit(font.render("Trails We Want (And The Ones We Take)", True, (335, 335, 340)), (40, 30))
    
    lines = []

    y = 80
    for line in lines:
        screen.blit(small_font.render(line, True, (320, 320, 325)), (40, y))
        y += 23

    pygame.draw.line(screen, (150, 150, 160), (40, HEIGHT - 60), (WIDTH - 20, HEIGHT - 60), 2)
    screen.blit(small_font.render("> ", True, (355, 355, 355)), (50, HEIGHT - 50))

import asyncio

game = TextAdventure()

asyncio.run(game.run())