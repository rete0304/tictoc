# -*- coding: utf-8 -*-

import player
class game():
    def __init__(self):
        self.player1 = player.player("O")
        self.player2 = player.player("X")
        self.checkerboard = []
        self.put_times = 0 #當數字為九代表棋盤塞滿了
        self.side = 1 #0代表"O"方，1代表"X"方
        self.position_convert = {"ul":[0,0] , "um":[0,1] , "ur":[0,2],
                                 "ml":[1,0] , "mm":[1,1] , "mr":[1,2],
                                 "bl":[2,0] , "bm":[2,1] , "br":[2,2]}
        self.end = False
    def put(self):
        if self.side == 0:
            player_now = self.player1
            self.side = 1
        else:
            player_now = self.player2
            self.side = 0
        put_success = False
        while(put_success != True):
            print "You are player ",player_now.player_type," ,put you chess:"
            put_position = raw_input()
            if put_position not in self.position_convert: #檢查輸入是否正確
                continue

            if (self.isRepeat(self.position_convert[put_position]) == True): #檢查是否有重複下棋
                continue
            else:

                put_success = True
                self.put_times = self.put_times + 1


            player_now.putChessman(self.position_convert[put_position])




    def draw(self):
        print "X"
        print self.player1.position
        print "O"
        print self.player2.position

    def check(self):
        """
        1.如果下子次數超過9顆，代表遊戲和局
        2.如果某一排的O排成一列，則回傳0
        3.如果某一排的X排成一列，則回傳1
        4.檢查中沒有和局也沒有獲勝，則回傳-1
        """
        if self.put_times > 8:
            self.end = True
        if self.isWin(self.player1.position) == True:
            self.end = True
            return 0
        if self.isWin(self.player2.position) == True:
            self.end = True
            return 1

        return -1
    def isRepeat(self,pos):
        """
        print pos
        print self.player1.position
        print self.player2.position
        print ( pos in self.player1.position )
        print (pos in self.player2.position)
        print ""
        """
        return (( pos in self.player1.position ) or (pos in self.player2.position) )

    def isWin(self,position):
        wen_table = [[[0, 0], [0, 1], [0, 2]],
                     [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]],
                     [[0, 0], [1, 0], [2, 0]],
                     [[0, 1], [1, 1], [2, 1]],
                     [[0, 2], [1, 2], [2, 2]],
                     [[0, 0], [1, 1], [2, 2]],
                     [[2, 0], [1, 1], [0, 2]]]
        check_result = False

        """
        for t_list in wen_table:      
            if(cmp(position,t_list) == 2):
                check_result = True
                return check_result           
        return check_result
        """
        return check_result

    def __del__(self):
        print('__del__')