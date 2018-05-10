# -*- coding: utf-8 -*-
"""
V2.0
"""
import game

def app():
    gameObj = game.game()
    gameObj.draw()
    while(gameObj.end == False):


        gameObj.put()
        gameObj.check()
        gameObj.draw()
        #3種狀況會結束遊戲:
        #1.O贏
        #2.X贏
        #3.格子填完但是沒有任何一人獲勝
        #(3也可以簡化成雙方下了9次但是沒有分出勝負)
    del gameObj
if __name__ == "__main__":
    isPlay = True
    while(isPlay == True):
        app()
        isContinue = True
        while isContinue == True:
            print "Are you went to paly the game(y/n):"
            inp = raw_input()
            if inp == "n":
                print "Good Bye!!"
                isPlay = False
                isContinue = False
            elif inp == "y":
                print "Let's Rock!!"
                isPlay = True
                isContinue = False
            else:
                print "Enter Wrong Answer"
