import Board as Board

class Piece(Board):
    def __init__(self):
        #Insert inits for each piece here
        #black start
        RR1=Chariot_black.__init__(self, 0, 0, "black")
        RH1=Horse_black.__init__(self, 0, 1, "black")
        RE1=Elephant_black.__init__(self, 0, 2, "black")
        RA1=Advisor_black.__init__(self, 0, 3, "black")
        RG=General_black.__init__(self, 0, 4, "black")
        RA2=Advisor_black.__init__(self, 0, 5, "black")
        RE2=Elephant_black.__init__(self, 0, 6, "black")
        RH2=Horse_black.__init__(self, 0, 7, "black")
        RR2=Chariot_black.__init__(self, 0, 8, "black")
        RC1=Cannon_black.__init__(self, 2, 1, "black")
        RC2=Cannon_black.__init__(self, 2, 7, "black")
        RS1=Soldier_black.__init__(self, 3, 0, "black")
        RS2=Soldier_black.__init__(self, 3, 2, "black")
        RS3=Soldier_black.__init__(self, 3, 4, "black")
        RS4=Soldier_black.__init__(self, 3, 6, "black")
        RS5=Soldier_black.__init__(self, 3, 8, "black")

        #red
        R1=Chariot_red.__init__(self, 9, 0, "red")
        RH1=Horse_red.__init__(self, 9, 1, "red")
        RE1=Elephant_red.__init__(self, 9, 2, "red")
        RA1=Advisor_red.__init__(self, 9, 3, "red")
        RG=General_red.__init__(self, 9, 4, "red")
        RA2=Advisor_red.__init__(self, 9, 5, "red")
        RE2=Elephant_red.__init__(self, 9, 6, "red")
        RH2=Horse_red.__init__(self, 9, 7, "red")
        RR2=Chariot_red.__init__(self, 9, 8, "red")
        RC1=Cannon_red.__init__(self, 7, 1, "red")
        RC2=Cannon_red.__init__(self, 7, 7, "red")
        RS1=Soldier_red.__init__(self, 6, 0, "red")
        RS2=Soldier_red.__init__(self, 6, 2, "red")
        RS3=Soldier_red.__init__(self, 6, 4, "red")
        RS4=Soldier_red.__init__(self, 6, 6, "red")
        RS5=Soldier_red.__init__(self, 6, 8, "red")