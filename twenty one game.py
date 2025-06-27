import os,random
from time import sleep
def clear():
    os.system("cls" if os.name=='nt' else "clear")
def deal_card():
    card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(card)
def calculate_score(list):
    if sum(list)==21 and len(list)==2:
        return 0
    elif 11 in list:
        if sum(list)>21:
            list.remove(11)
            list.append(1)
    return sum(list)
def compare(computer_score,user_score):
    Result={
        'user_black_jack':"You won with a blackjack 😎👌🔥\n\n\n",
        'computer_black_jack':"sorry, computer had blackjack 😱\n\n\n",
        'user_win':'You win 🥰\n\n\n',
        'user_lose':'You lose 😥\n\n\n',
        'user_over21':'You went over 21, sorry 😧\n\n\n',
        'computer_over21':'Computer went over 21, you win 🌟\n\n\n',
        'draw':'Draw 😊\n\n\n',
    }
    if user_score==0:
        return Result['user_black_jack']
    elif user_score>21:
        return Result['user_over21']
    elif computer_score>21:
        return Result['computer_over21']
    elif computer_score==0:
        return Result['computer_black_jack']
    elif user_score>computer_score:
        return Result['user_win']
    elif computer_score>user_score:
        return Result['user_lose']
    return Result['draw']
def game():
    computer_card=[deal_card() for _ in range(2)]
    user_card=[deal_card() for _ in range(2)]
    game_on=True
    while game_on:
        computer_score=calculate_score(computer_card)
        user_score=calculate_score(user_card)
        if computer_score==0 or user_score==0 or computer_score==21 or user_score==21:
            game_on=False
        else:
            print(f"Your cards are {user_card}, your score is {user_score}")
            print(f"The first computer's cards is {computer_card[0]}")
            if input('Do you want to draw another card (Y/N)\v').lower()=='y':
                user_card.append(deal_card())
            else:
                game_on=False
    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)
    print(f"Your final hand:{user_card} with score {user_score}")
    print(f"Computer's final hand:{computer_card} with score {computer_score}")
    print(compare(computer_score=computer_score,user_score=user_score))
    
while input("Choose a game to start...\n\n\n1-Froggy\n2-Twenty one \n3-Snack\n").lower()=="twenty one":
    clear()
    print("starting game...")
    sleep(3)
    clear()
    game()