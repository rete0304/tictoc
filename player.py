# -*- coding: utf-8 -*-

class player():
    def __init__(self,player_type):
        self.player_type=player_type
        self.position = []
    def putChessman(self,pos):
        self.position.append(pos)
    def getPosition(self):
        return self.position

