# -*- coding: utf-8 -*-
"""
dev1.0
"""
import game

def app():
    gameObj = game.game()
    while(gameObj.end == False):

        gameObj.draw()
        gameObj.put()
        gameObj.check()
        #3種狀況會結束遊戲:
        #1.O贏
        #2.X贏
        #3.格子填完但是沒有任何一人獲勝
        #(3也可以簡化成雙方下了9次但是沒有分出勝負)

if __name__ == "__main__":
    app()