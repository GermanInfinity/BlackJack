# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    global in_play
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

#    def draw(self, canvas, pos, in_play):
    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
#        if in_play:
#            canvas.draw_image(card_back, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
#    

class Hand:
    global in_play 
    def __init__(self):
        self.hand = []
        
    def __str__(self):
        con = "Hand contains " 
        for i in self.hand:
            con += str(i)
            con += ' '
        return con
    
    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        total = 0 
        for card in self.hand:
            total += VALUES[card.get_rank()]
            
        if total >= 12:
            return total 
        
        elif total < 12:
            for card in self.hand:
                if card.get_rank() == 'A':
#                if 'A' in card.get_rank(): 
                    total += 10
                    return total
#        if total == 0:
        return total
            
            
    def draw(self, canvas, pos):
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0] += 80
            pos[1] += 0

 


class Deck():
    def __init__(self): 
        self.deck = []
        for i in SUITS:
            for j in RANKS:
                self.deck.append(Card(i,j))
         
                
    def __str__(self):
        s = "Deck contains "
        a = ''
        for i in self.deck:
            a += str(i) 
            a += ' '

        return s + a
    
    def deal_card(self):
        return self.deck.pop()
        
    def shuffle(self):
        random.shuffle(self.deck)
        
        



#define event handlers for buttons
def deal():

    global outcome, in_play, c1, player, dealer, score
    if in_play:
        outcome = "Player bursted.."
        score -= 1
        in_play = True
        
    if not in_play:
        outcome = "New Deal"
        c1 = Deck()
        c1.shuffle()
        player = Hand()
        dealer = Hand()
   
        player.add_card(c1.deal_card())
        dealer.add_card(c1.deal_card())
        player.add_card(c1.deal_card())
    
    
        dealer.add_card(c1.deal_card())

    
        in_play = True

def hit():
    
    global player, c1, in_play, outcome, score
    
    if player.get_value() <= 21 and in_play == True:
        outcome = ""
        player.add_card(c1.deal_card())
        print player.get_value()   #
    
    elif player.get_value() > 21:
        outcome = "Player bursted."
        print outcome   #
        score -= 1
        in_play = False
       
    
   
def stand():
    global player, dealer, c1, in_play, outcome, score
    
    if player.get_value() > 21:
        outcome = "Player bursted."
        in_play = False
        score += 1
        print outcome
        return outcome
    
    while dealer.get_value() < 17 or in_play == True: 
        outcome = ""
        dealer.add_card(c1.deal_card())
        
        if dealer.get_value() > 21:
            print dealer.get_value()#
            outcome = "Dealer bursts."
            in_play = False
            score += 1
            print outcome#
            return outcome
        elif player.get_value() <= dealer.get_value():
            print dealer.get_value()#
            outcome = "Dealer wins."
            score -= 1
            in_play = False
            print outcome#
            return outcome
        else:
            print dealer.get_value()#
            outcome = "Player wins."
            score += 1
            in_play = False
            print outcome#
            return outcome
            
 
def draw(canvas):

    global outcome, player, dealer, in_play
    
    canvas.draw_text('BLACKJACK', (220,150), 35, 'BLACK')
    canvas.draw_text('Player', (100,390), 27, 'BLACK')
    canvas.draw_text('Dealer', (100,240), 27, 'BLACK')
   
    
#    player.draw(canvas, [100, 400], in_play)
#    dealer.draw(canvas, [100, 250], in_play)

    player.draw(canvas, [100, 400])
    dealer.draw(canvas, [100, 250])
    if in_play:
        canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE,
                          [100 + CARD_CENTER[0], 250 + CARD_CENTER[1]], CARD_SIZE)

    #dealer.hole_draw(canvas, [200, 250])
    
    #dealer.draw(canvas, [100, 250])
   
    canvas.draw_text(outcome, (255,250), 22, 'Orange')
    canvas.draw_text('Score:', (400,250), 22, 'Black')
    canvas.draw_text(str(score), (460,250), 22, 'Orange')

    
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
