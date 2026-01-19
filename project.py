import random
from faker import Faker
import sys



class Deck:
    def __init__(self):
        self.original_deck = ["4 Diamonds", "4 Spades", "4 Hearts", "4 Clubs",
                      "5 Diamonds", "5 Spades", "5 Hearts", "5 Clubs",
                      "6 Diamonds", "6 Spades", "6 Hearts", "6 Clubs",
                      "7 Diamonds", "7 Spades", "7 Hearts", "7 Clubs",
                      "10 Diamonds", "10 Spades", "10 Hearts", "10 Clubs",
                      "Q Diamonds", "Q Spades", "Q Hearts", "Q Clubs",
                      "J Diamonds", "J Spades", "J Hearts", "J Clubs",
                      "K Diamonds", "K Spades", "K Hearts", "K Clubs",
                      "A Diamonds", "A Spades", "A Hearts", "A Clubs",
                      "2 Diamonds", "2 Spades", "2 Hearts", "2 Clubs",
                      "3 Diamonds", "3 Spades", "3 Hearts", "3 Clubs",
                      ]
        self._game_deck = self.original_deck.copy()
        self_actual_round = 0
        random.shuffle(self.game_deck)
    



    @property
    def game_deck(self):
        return self._game_deck


    def get_power(self, card):
        return self.original_deck.index(card)

    def get_card_name(self, id):
        return self.original_deck[id]

    



class Player():
    def __init__(self, name):
        self._name = name
        self._hand  = []

    @property
    def name(self):
        return self._name

    @property
    def hand(self):
        return self._hand

    def add_card(self, card):
        if len(self._hand) <= 2:
            #print(len(self._hand))
            self._hand.append(card)
        else:
            raise ValueError("Hand's player is full")
    ## A carta sera decidida pela funcao "best_option"
    # A ideia é jogar sempre a melhor carta da mão
    def throw_card(self, card):
        if card in self._hand:
            self._hand.remove(card)
            return card
        else:
            raise ValueError("The player don't have this card")




class Team():
    def __init__(self, title):
        self._title = title
        self._points = 0
        self._members = []

    def add_member(self, member_name):
        self._members.append(member_name)


    @property
    def members(self):
        return self._members

    @property
    def title(self):
        return self._title


    @property
    def points(self):
        return self._points


    def add_points(self, points):
        self._points += points

def Turn(player_one, player_two, game, round_i ):


    #print(f"Player {player_one.name}  \n {player_one.hand} \n ----------- \n\n")
    #print(f"Player {player_two.name}  \n {player_two.hand} \n ----------- \n\n")

    ## FAZER ESQUEMA PARA JOGAR SEMPRE A MAIS FORTE, o get_power fuciona para ordernar
    ## FAZER ESQUEMA PARA TRUCAR
    #### Se o power for grande, chamar truco para (50/50), e o proximo player (25-> aceitar, 50-Correr, 25-Trucar)
    ##### O truco n pode passar do 
    player_one_cast = player_one.throw_card(player_one.hand[random.randint(0, round_i - 1)])
    player_two_cast = player_two.throw_card(player_two.hand[random.randint(0, round_i - 1)])

    print("P1 "+player_one.name+ " CAST: " + player_one_cast )
    print("P2 "+player_two.name+ " CAST: " + player_two_cast)

    turn = {
        player_one.name: game.get_power(player_one_cast),
        player_two.name: game.get_power(player_two_cast),
    }

    sorted_list = sorted(turn.items(), key=lambda item: item[1])

    #print(sorted_list)
    winner, hand = sorted_list[1]
    #print(f"Winner is: {winner} with {game.get_card_name(hand)} H: {hand}")

    return winner

def game_round(round_deck, player_one, player_two):
    player_one.add_card(round_deck.game_deck.pop())
    player_one.add_card(round_deck.game_deck.pop())
    player_one.add_card(round_deck.game_deck.pop())
    
    player_two.add_card(round_deck.game_deck.pop())
    player_two.add_card(round_deck.game_deck.pop())
    player_two.add_card(round_deck.game_deck.pop())

    # print(f"Player {player_one.name}  \n {player_one.hand} \n ----------- \n\n")
    # print(f"Player {player_two.name}  \n {player_two.hand} \n ----------- \n\n")

    winners = []
    round_winner = ""
    for i in [3, 2, 1]:
        
        print(f"Turn [{i}] \n ----- ")
        turn_winner = Turn(player_one, player_two, round_deck, i)        
        print(f"WINNER: {turn_winner}  \n \n  \n \n " )
        winners.append(turn_winner)
        if turn_winner in winners:
            round_winner = turn_winner

    
    print(winners)
    return round_winner


def main():
    
 
    fake = Faker()
    alfa = Team("Alfa Team")
    beta = Team("Beta Team")

    ## MONTAR EQUIPE DE 4
    player_one = Player(fake.name())
    alfa.add_member(player_one.name)

    player_two = Player(fake.name())
    beta.add_member(player_two.name)



    ### FAZER MELHOR DE 3
    while (alfa.points <= 12) and (beta.points <= 12):
        if alfa.points == 12:
            sys.exit(f"The Team: {alfa.title}, clinched the match!!!")
            sys
        elif beta.points == 12:
            sys.exit(f"The Team: {beta.title}, clinched the match!!!")
        else: 

            match_deck = Deck()
            winner_player = game_round( match_deck, player_one, player_two)
            

            if winner_player in alfa.members:
                alfa.add_points(3)
            else:
                beta.add_points(3)
        
            print(f"------\n Team: {alfa.title} \n POINTS: [{alfa.points}] \n \n ")
            print(f"Team: {beta.title} \n POINTS: [{beta.points}] \n\n")

           

    

if __name__ == "__main__":
    main()
