# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:49:38 2020

@author: mnm
"""


'''Welcome to a mighty game of tic tac toe!'''
import random

def graph(game):
   #l = 3
    w = 3
    c = ' ---'
    m = '|'
    graph_g = []
    i0 = 0
    i1 = 1
    i2 = 2
    for e in game:
        for x in e:
            graph_g.append(x)
    
        for i in range(1):
            
            print(c*3)
            print(f'{m} {graph_g[i0]} {m} {graph_g[i1]} {m} {graph_g[i2]} {m}')
            i0 += 3
            i1 += 3
            i2 += 3
        
    
        
       
    print(c*w)
  
    
def put_xo(user,game,turn):
    
    
      
    swap = []
    if turn == 1:
        user1 = user
        r1,c1 = int(user1[0]),int(user1[2])
                
        swap = game[r1-1]
        
        while swap[c1-1] != 0:
            user1 = list(input('Not a valid choise! Try an empty space: '))
            r1,c1 = int(user1[0]),int(user1[2])                
            swap = game[r1-1]                        
        else:
            swap[c1-1] = 'X'
            print(swap[c1-1])
            game[r1-1] = swap
            
    if turn == 2:
        user2 = user
        r2,c2 = int(user2[0]),int(user2[2])
        swap = game[r2-1]
   
        while swap[c2-1] != 0:
            user2 = list(input('Not a valid choise! Try an empty space: '))
            r2,c2 = int(user2[0]),int(user2[2])                
            swap = game[r2-1]                        
        else:
            swap[c2-1] = 'O'
            
            game[r2-1] = swap
   
        
    
    graph(game)
    return game

def win_check(game):
    '''checks if game the elements in all winning combinations are the same'''
    l1 = game[0]
    l2 = game[1]
    l3 = game[2]
    c1 = [l1[0],l2[0],l3[0]]
    c2 = [l1[1],l2[1],l3[1]]
    c3 = [l1[2],l2[2],l3[2]]
    d1 = [l1[0],l2[1],l3[2]]
    d2 = [l1[2],l2[1],l3[0]]
    ttt = l1,l2,l3,c1,c2,c3,d1,d2
    
    for i in ttt:
        if set(i) == {'X'}:
            return 1
        elif set(i) == {'O'}:
            return 2

def cpu_check(game):
    '''ends the game if it is possible with one move'''
    l1 = game[0]
    l2 = game[1]
    l3 = game[2]
    c1 = [l1[0],l2[0],l3[0]]
    c2 = [l1[1],l2[1],l3[1]]
    c3 = [l1[2],l2[2],l3[2]]
    d1 = [l1[0],l2[1],l3[2]]
    d2 = [l1[2],l2[1],l3[0]]

    ttt = [l1,l2,l3,c1,c2,c3,d1,d2]
    for e in ttt:        
        if e.count('O') == 2 and e.count(0) == 1:
            return True

def cpu_end(game):
    '''ends the game it is possible by one move
    ttt is possible winning spaces
    q is the index of the possible winning combination in ttt
    w is the index of the 0 in that 3 space '''
    
    l1 = game[0]
    l2 = game[1]
    l3 = game[2]
    c1 = [l1[0],l2[0],l3[0]]
    c2 = [l1[1],l2[1],l3[1]]
    c3 = [l1[2],l2[2],l3[2]]
    d1 = [l1[0],l2[1],l3[2]]
    d2 = [l1[2],l2[1],l3[0]]

    ttt = [l1,l2,l3,c1,c2,c3,d1,d2]
    for e in ttt:        
        if e.count('O') == 2 and e.count(0) == 1:
            q = ttt.index(e)
            w = e.index(0)
    sc7 = {0:3,1:5,2:7}   
    sc6 = {0:1,1:5,2:9}
    sc5 = {0:3,1:6,2:9}
    sc4 = {0:2,1:5,2:8}
    sc3 = {0:1,1:4,2:7}    
    sc2 = {0:7,1:8,2:9}
    sc1 = {0:4,1:5,2:6}
    sc0 = {0:1,1:2,2:3}
    
    space_converter = {0:sc0,1:sc1,2:sc2,3:sc3,4:sc4,5:sc5,6:sc6,7:sc7}
    
    cpu = space_converter[q][w]#nested dict
    return cpu -1 

def cpu(game):
    
    p = []
    z = []
    for e in game:
        for x in e:
            z.append(x)
    for i,j in enumerate(z):
        if j == 0:
            p.append(i)    
    if cpu_check(game) == True:
        cpu = cpu_end(game)
        print(cpu)
        print(p)            
    else:
        cpu = random.choice(p)
    
        
    if cpu <= 2:
        r = 0
        c = cpu
    elif cpu <= 5:
        r = 1
        c = cpu - 3
    else:
        r = 2
        c = cpu - 6
    swap = [] 
    swap = game[r]


    swap[c] = 'O'
    game[r] = swap
    print('Hmmm let me think,')
    graph(game)
    return game    



def xo_game():

    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    player_choice = input('''Welcome to a mighty game of Tic Tac Toe by Krom abi!
Press any key to play with 2 Players                
Or you can type "cpu" to play against me!:''')
    graph(game)
    print('You can pick your space by row and order e.g. 2,3 for the 3rd space in the second line.')
    replay = ''
    while True:        
        user = list(input('Player 1,make your move:'))
        turn = 1
        game = put_xo(user, game, turn)
        
        if win_check(game) == 1:
          replay = input('Congrats Player 1! You won! type "re" to play again or any key to exit:')  
          if replay.lower() == "re": xo_game()
          else:break
        if player_choice.lower() =='cpu':
            game = cpu(game)
            if win_check(game) == 2:
                replay = input('LOL! you lost againts computer! type "re" to play again or any key to exit:')  
                if replay.lower == "re": xo_game()
                else:break
        else:
            user = list(input('Player 2, make your move:'))
            turn = 2
            game = put_xo(user, game, turn)
            if win_check(game) == 2:
                replay = input('Congrats Player 2! You won! type "yes" to play again or any key to exit:')  
                if replay.lower == "yes": xo_game()
                else:break
        
       
        
        
      
        
xo_game()        