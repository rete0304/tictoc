# -*- coding: utf-8 -*-

import player
class game():
    def __init__(self):
        self.player1 = player.player("O")
        self.player2 = player.player("X")
        self.checkerboard = []
        self.put_times = 0 #當數字為九代表棋盤塞滿了
        self.isRest = False
        self.isQuit = False
        self.side = 1 #0代表"O"方，1代表"X"方
        self.position_convert = {"ul":[0,0] , "um":[0,1] , "ur":[0,2],
                                 "ml":[1,0] , "mm":[1,1] , "mr":[1,2],
                                 "bl":[2,0] , "bm":[2,1] , "br":[2,2]}
        self.show_position = [['ul', 'um', 'ur'], ['ml', 'mm', 'mr'], ['bl', 'bm', 'br']]
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

            if put_position == "r":
                self.isRest = True
                break

            if put_position == "q":
                self.isQuit = True
                break

            if put_position not in self.position_convert: #檢查輸入是否正確
                continue

            if (self.isRepeat(self.position_convert[put_position]) == True): #檢查是否有重複下棋
                continue
            else:

                put_success = True
                self.put_times = self.put_times + 1


            player_now.putChessman(self.position_convert[put_position])




    def draw(self):
        for x in range(3):
            for y in range(3):
                if( [x,y] in self.player1.position):
                    print " "+self.player1.player_type+" ",
                elif ([x, y] in self.player2.position):
                    print " " + self.player2.player_type + " ",
                else:
                    print " " + self.show_position[x][y],
                if y<2:
                    print "|",
            print ""
            if(x<2):
                print "----*-----*-----"


    def check(self):
        """
        1.如果下子次數超過9顆，代表遊戲和局
        2.如果某一排的O排成一列，則回傳0
        3.如果某一排的X排成一列，則回傳1
        4.檢查中沒有和局也沒有獲勝，則回傳-1
        5.如果重新旗標(isRest)為真，則遊戲直接重新，不論和局
        6.如果放棄旗標(isQuit)為真，則遊戲直接跳出
        """
        if self.put_times > 8:
            print "No Body WIN This Game"
            self.end = True
        if self.isWin(self.player1.position) == True:
            print self.player1.player_type+" WIN This Game"
            self.end = True
            return 0
        if self.isWin(self.player2.position) == True:
            print self.player2.player_type + " WIN This Game"
            self.end = True
            return 1
        if self.isRest == True:
            print "Someone Reset The Game!!"
            self.end = False
        if self.isQuit == True:
            print "Bye!"
            self.end = True
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
        win_table = [[[0, 0], [0, 1], [0, 2]],
                     [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]],
                     [[0, 0], [1, 0], [2, 0]],
                     [[0, 1], [1, 1], [2, 1]],
                     [[0, 2], [1, 2], [2, 2]],
                     [[0, 0], [1, 1], [2, 2]],
                     [[2, 0], [1, 1], [0, 2]]]
        check_result = False


        for t_list in win_table:
            #直接檢查贏的3個座標是否同時在win table的某一個list面
            if (t_list[0] in position ) and \
               (t_list[1] in position ) and \
               (t_list[2] in position ):
                check_result = True
                return check_result
        return check_result

    def __del__(self):
        pass
