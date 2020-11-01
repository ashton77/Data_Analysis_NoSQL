# Fixed Cards spell merger-------------------------------

# Class creation for Person, cards
#person -> player1 and player2
#cards -> num of cards given by the users
#cards > name, charcteristic(int) unique, cards must be unique
import random
import time

# def shuffle_it(listy):
#   random.shuffle(listy)
#   return listy

class player:
  outdated_deck = []
  def __init__(self, name, points, deck):
    self._name = name
    self._points = points
    self._deck = []
    #self._outdated_deck = []


# p1_name = input('Enter the name of player1\n')
# p2_name = input('Enter the name of player2\n')
# player1 = player(p1_name,0,0)
# player2 = player(p2_name,0,0)
#print(player1._name)

class cards:
  #card_deck = []
  def __init__(self, name, runs, wickets, skill):
    #cards.card_deck.append(self)
    self._name = name
    self._runs = runs
    self._wickets = wickets
    self._skill = skill

  def view(self):
    print(f'name is {self._name}')
    print(f'runs is {self._runs}')
    print(f'wickets is {self._wickets}')
    print(f'skill is {self._skill}')

  # def characteristics(value):
  #   for i in range(1,value+1):
  #     yield i
  
def dice():
  return random.randint(1,6)

def switch_func(argument):
  switcher = {
      1 : 'Runs',
      2 : 'Wickets',
      3 : 'Skill'
  }
  return switcher.get(argument,'default')


#---------------------code for Resurrect spell-------------------------
def resurrect_spell(flag):
  if flag == 1:
    print(f'Wait for your random card from the outdated deck\n')
    print(f'Card coming up...')
    time.sleep(1)
    card_from_outdated = random.choice(player.outdated_deck)
    print(f'***************Your card************************\n')
    print(f'{card_from_outdated._name}\nRuns: {card_from_outdated._runs}\nWickets: {card_from_outdated._wickets}\nSkill: {card_from_outdated._skill}')
    print(f'************************************************\n')
    player2._deck.insert(0,card_from_outdated)
    print(f'{p2_name} pick the characteristic you want to challenge {p1_name} with!\n Select :\n 1 -> Runs\n 2 -> Wickets\n 3 -> Skill')
    time.sleep(2)
    charac = int(input(f'Enter your Choice\n'))

  
  else:
    print(f'Wait for your random card from the outdated deck\n')
    print(f'Card coming up...')
    time.sleep(1)
    card_from_outdated = random.choice(player.outdated_deck)
    print(f'***************Your card************************\n')
    print(f'{card_from_outdated._name}\nRuns: {card_from_outdated._runs}\nWickets: {card_from_outdated._wickets}\nSkill: {card_from_outdated._skill}')
    print(f'************************************************\n')
    player1._deck.insert(0,card_from_outdated)
    #print(player1._deck[0]._name)
    print(f'{p1_name} pick the characteristic you want to challenge {p2_name} with!\n Select :\n 1 -> Runs\n 2 -> Wickets\n 3 -> Skill')
    time.sleep(2)
    charac = int(input(f'Enter your Choice\n'))


  if charac == 1:
    if flag == 1:
      if player1._deck[0]._runs > player2._deck[0]._runs:
        flag = 1
      else:
        flag = 2
    else:
      if player2._deck[0]._runs > player1._deck[0]._runs:
        flag = 2
      else:
        flag = 1
  
  elif charac == 2:
    if flag == 1:
      if player1._deck[0]._wickets > player2._deck[0]._wickets:
        flag = 1
      else:
        flag = 2
    else:
      if player2._deck[0]._wickets > player1._deck[0]._wickets:
        flag = 2
      else:
        flag = 1
  
  else:
    if flag == 1:
      if player1._deck[0]._skill > player2._deck[0]._skill:
        flag = 1
      else:
        flag = 2
    else:
      if player2._deck[0]._skill > player1._deck[0]._skill:
        flag = 2
      else:
        flag = 1
    
  if flag == 1:
    print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n')
    print(f'{p1_name} Wins the round')
    print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n')
    player1._points += 1

  else:
    print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n')
    print(f'{p2_name} Wins the round\n')
    print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    player2._points += 1
  
  print(f'{p1_name} has {player1._points} point(s)')
  print(f'*************************************\n')
  print(f'{p2_name} has {player2._points} points(s)')
  print(f'*************************************\n')


  # player1._outdated_deck.append(player1._deck.pop(0))
  # player2._outdated_deck.append(player2._deck.pop(0))

  player.outdated_deck.append(player1._deck.pop(0))
  player.outdated_deck.append(player2._deck.pop(0))
  random.shuffle(player.outdated_deck)

  return flag


#---------------------code for God spell-------------------------------
def God_spell(flag):
  if flag == 1:
    print(f'{p1_name}, pick a random card from {p2_name} deck\n')
    p1_num = int(input(f'Pick a number to select the card'))
    print(f'***************Your card************************\n')
    print(f'{player1._deck[0]._name}\nRuns: {player1._deck[0]._runs}\nWickets: {player1._deck[0]._wickets}\nSkill: {player1._deck[0]._skill}')
    print(f'************************************************\n')
    print(f'{p1_name} pick the characteristic you want to challenge {p2_name} with!\n Select :\n 1 -> Runs\n 2 -> Wickets\n 3 -> Skill')
    time.sleep(2)
    charac = int(input(f'Enter your Choice\n'))

  else:
    print(f'{p2_name}, pick a random card from {p1_name} deck\n For this, select a number')
    p2_num = int(input(f'Pick a number to select the card'))
    print(f'***************Your card************************\n')
    print(f'{player2._deck[0]._name}\nRuns: {player2._deck[0]._runs}\nWickets: {player2._deck[0]._wickets}\nSkill: {player2._deck[0]._skill}')
    print(f'************************************************\n')
    print(f'{p2_name} pick the characteristic you want to challenge {p1_name} with!\n Select :\n 1 -> Runs\n 2 -> Wickets\n 3 -> Skill')
    time.sleep(2)
    charac = int(input(f'Enter your Choice\n'))
  
  if charac == 1:
    if flag == 1:
      if player1._deck[0]._runs > player2._deck[p1_num-1]._runs:
        flag = 1
      else:
        flag = 2
    else:
      if player2._deck[0]._runs > player1._deck[p2_num-1]._runs:
        flag = 1
      else:
        flag = 2
  
  elif charac == 2:
    if flag == 1:
      if player1._deck[0]._wickets > player2._deck[p1_num-1]._wickets:
        flag = 1
      else:
        flag = 2
    else:
      if player2._deck[0]._wickets > player1._deck[p2_num-1]._wickets:
        flag = 1
      else:
        flag = 2
  
  else:
    if flag == 1:
      if player1._deck[0]._skill > player2._deck[p1_num-1]._skill:
        flag = 1
      else:
        flag = 2
    else:
      if player2._deck[0]._skill > player1._deck[p2_num-1]._skill:
        flag = 1
      else:
        flag = 2
    
  if flag == 1:
    print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n')
    print(f'{p1_name} Wins the round')
    print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n')
    player1._points += 1

  else:
    print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n')
    print(f'{p2_name} Wins the round\n')
    print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    player2._points += 1
  
  print(f'{p1_name} has {player1._points} point(s)')
  print(f'*************************************\n')
  print(f'{p2_name} has {player2._points} points(s)')
  print(f'*************************************\n')


  # player1._outdated_deck.append(player1._deck.pop(0))
  # player2._outdated_deck.append(player2._deck.pop(0))

  player.outdated_deck.append(player1._deck.pop(0))
  player.outdated_deck.append(player2._deck.pop(0))
  random.shuffle(player.outdated_deck)

  return flag

#------------------Code for Normal round-----------------------
def normal_round(flag, normal_round_resurrect_spell_player1_flag, normal_round_resurrect_spell_player2_flag):
  time.sleep(2)
  print('Card coming up...\n')
  # print(f'{player1._deck[0]._name}\nRuns: {player1._deck[0]._runs}\nWickets: {player1._deck[0]._wickets}\nSkill: {player1._deck[0]._skill}')
  # print(f'********************************************\n')
  # print(f'{player2._deck[0]._name}\nRuns: {player2._deck[0]._runs}\nWickets: {player2._deck[0]._wickets}\nSkill: {player2._deck[0]._skill}')
  # print(f'********************************************\n')
  if flag == 1:
    print(f'******************{p1_name} Card**************************\n')
    time.sleep(2)
    print(f'{player1._deck[0]._name}\nRuns: {player1._deck[0]._runs}\nWickets: {player1._deck[0]._wickets}\nSkill: {player1._deck[0]._skill}')
    print(f'********************************************\n')
    time.sleep(2)
    print(f'{p1_name} pick the characteristic you want to challenge {p2_name} with!\n Select :\n 1 -> Runs\n 2 -> Wickets\n 3 -> Skill')
    time.sleep(2)
    charac = int(input(f'Enter your Choice'))
    #print(switch_func(charac))
    print(f'{p2_name}, do want to play the Resurrect Spell or continue as usual\n')
    time.sleep(1)
    spell_choice = int(input(f'Enter your choice:\n1 -> Continue as usual\n2 -> Resurrect Spell\n'))
    if spell_choice == 1:
      flag, charac = normal_round_card_compare(flag,charac)
    else:
      if normal_round_resurrect_spell_player1_flag == 0:
        flag = resurrect_spell(flag)
        normal_round_resurrect_spell_player1_flag += 1
      else:
        print(f'You have already played your Resurrect Spell. Round continues as usual\n')
        flag, charac = normal_round_card_compare(flag,charac)
  
  else:
    print(f'******************{p2_name} Card**************************\n')
    time.sleep(2)
    print(f'{player2._deck[0]._name}\nRuns: {player2._deck[0]._runs}\nWickets: {player2._deck[0]._wickets}\nSkill: {player2._deck[0]._skill}')
    print(f'********************************************\n')
    time.sleep(2)
    print(f'{p2_name} pick the characteristic you want to challenge {p1_name} with!\n Select :\n 1 -> Runs\n 2 -> Wickets\n 3 -> Skill')
    time.sleep(2)
    charac = int(input(f'Enter your Choice\n'))
    #print(switch_func(charac))
    print(f'{p1_name}, do want to play the Resurrect Spell or continue as usual\n')
    time.sleep(1)
    spell_choice = int(input(f'Enter your choice:\n1 -> Continue as usual\n2 -> Resurrect Spell\n'))
    if spell_choice == 1:
      flag, charac = normal_round_card_compare(flag,charac)
    else:
      if normal_round_resurrect_spell_player2_flag == 0:
        flag = resurrect_spell(flag)
        normal_round_resurrect_spell_player2_flag += 1
      else:
        print(f'You have already played your Resurrect Spell. Round Continues as usual\n')
        flag, charac = normal_round_card_compare(flag,charac)
  
  return flag, normal_round_resurrect_spell_player1_flag, normal_round_resurrect_spell_player2_flag

  
def normal_round_card_compare(flag,charac): #added this extra line--- test it or delete later
  time.sleep(2)
  print(f'**********Both players'' cards displayed**********************\n')
  print(f'\n******************{p1_name} Card**************************\n')
  print(f'{player1._deck[0]._name}\nRuns: {player1._deck[0]._runs}\nWickets: {player1._deck[0]._wickets}\nSkill: {player1._deck[0]._skill}')
  print(f'********************************************\n\n')
  time.sleep(2)
  print(f'******************{p2_name} Card**************************\n')
  print(f'{player2._deck[0]._name}\nRuns: {player2._deck[0]._runs}\nWickets: {player2._deck[0]._wickets}\nSkill: {player2._deck[0]._skill}')
  print(f'********************************************\n\n')


  if charac == 1:
    if player1._deck[0]._runs > player2._deck[0]._runs:
      flag = 1
    else:
      flag = 2

  elif charac == 2:
    if player1._deck[0]._wickets > player2._deck[0]._wickets:
      flag = 1
    else:
      flag = 2

  else:
    if player1._deck[0]._skill > player2._deck[0]._skill:
      flag = 1
    else:
      flag = 2

  if flag == 1:
    print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n')
    print(f'{p1_name} Wins the round')
    print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n')
    player1._points += 1

  else:
    print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n')
    print(f'{p2_name} Wins the round\n')
    print(f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    player2._points += 1
  
  print(f'{p1_name} has {player1._points} point(s)')
  print(f'*************************************\n')
  print(f'{p2_name} has {player2._points} points(s)')
  print(f'*************************************\n')


  # player1._outdated_deck.append(player1._deck.pop(0))
  # player2._outdated_deck.append(player2._deck.pop(0))

  player.outdated_deck.append(player1._deck.pop(0))
  player.outdated_deck.append(player2._deck.pop(0))
  random.shuffle(player.outdated_deck)

  return flag, charac

def display_points():
  print(f'{p1_name} has {len(player1._deck)} card(s) left\n')
  print(f'{p2_name} has {len(player2._deck)} card(s) left\n')


# x=0
# c_num = int(input('enter number of cards\n'))
# #print(card._name)
# res1 = random.sample(range(1,c_num+1),c_num)
# res2 = shuffle_it(res1)
# res3 = shuffle_it(res2)
#print(res2)

# while x < c_num:
#   card = cards('card '+str(x+1),res1[x],res2[x],res3[x])
#   print(card._name) #print statement to display all cards face down
#   b = [cards for cards in cards.card_deck]
#   # for i in b:
#   #   print(i)
#   x = x+1

p1_name = input('Enter the name of player1\n')
p2_name = input('Enter the name of player2\n')
player1 = player(p1_name,0,0)
player2 = player(p2_name,0,0)

#card creation----
ms_dhoni = cards('MS Dhoni', 10000, 5, 9)
virat_kohli = cards('Virat Kohli', 9000, 9, 8)
hardik_pandya = cards('Hardik Pandya', 6000, 40, 7)
shane_watson = cards('Shane Watson', 9300, 34, 6)
suresh_raina = cards('Suresh Raina', 8000, 25, 5)
irfan_pathan = cards('Irfan Pathan', 5000, 55, 4)
chris_gayle = cards('Chris Gayle', 12000, 30, 3)
dwayne_bravo = cards('Dwayne Bravo', 8500, 35, 2)

b = [ms_dhoni, virat_kohli, hardik_pandya, shane_watson, suresh_raina, irfan_pathan, chris_gayle, dwayne_bravo]
random.shuffle(b)
#print(b)
# equal distribution of cards
p1_cards = b[:len(b)//2]
p2_cards = b[len(b)//2:]
player1._deck = p1_cards
player2._deck = p2_cards
#print(player1._deck)
#print(player2._deck)

input(f'{p1_name} click Enter to roll the dice')
player1_dice = dice()
#print(player1_dice)
input(f'{p2_name} click Enter to roll the dice')
player2_dice = dice()
#print(player2_dice)

if player1_dice > player2_dice:
  print(f'{p1_name} wins the dice')
  flag = 1

else:
  print(f'{p2_name} wins the dice')
  flag = 2

God_spell_player1_flag = 0
God_spell_player2_flag = 0
Resurrect_spell_player1_flag = 0
Resurrect_spell_player2_flag = 0
normal_round_resurrect_spell_player1_flag = 0
normal_round_resurrect_spell_player2_flag = 0

while len(player1._deck) != 0 and len(player2._deck) != 0:
  if flag == 1:
    print(f'{p1_name}, your turn')
  else:
    print(f'{p2_name}, your turn')

  round_type = int(input(f'Select:\n 1 -> Normal Round\n 2 -> God Spell\n'))
  if round_type == 1:
    #print(f'current flag {flag}')
    flag, normal_round_resurrect_spell_player1_flag, normal_round_resurrect_spell_player2_flag = normal_round(flag, normal_round_resurrect_spell_player1_flag, normal_round_resurrect_spell_player2_flag) #flag must assigned to a variable to reset the flag in the next iteration
    display_points()
    #print(flag)

  elif round_type == 2:
    if flag == 1:
      if God_spell_player1_flag == 0:
        flag = God_spell(flag)
        God_spell_player1_flag += 1
        display_points()
      else:
        print(f'You have already played your God Spell')
    
    else:
      if God_spell_player2_flag == 0:
        flag = God_spell(flag)
        God_spell_player2_flag += 1
        display_points()
      else:
        print(f'You have already played your God Spell')
      
  # elif round_type == 3:
  #   if flag == 1:
  #     if Resurrect_spell_player1_flag == 0:
  #       flag = resurrect_spell(flag)
  #       Resurrect_spell_player1_flag += 1
  #       display_points()
  #     else:
  #       print(f'You have already played your God Spell')
  #   #why should the first turn have a choice to play the resurrect spell?#####**************************
  #   else:
  #     if Resurrect_spell_player2_flag == 0:
  #       flag = resurrect_spell(flag)
  #       Resurrect_spell_player2_flag += 1
  #       display_points()
  #     else:
  #       print(f'You have already played your Resurrect Spell')

  else:
    print(f'Please enter a valid choice from the list')



  #   elif God_spell_player2_flag == 0:
  #     flag = God_spell(flag)
  #     God_spell_player2_flag += 1
  #     display_points()

  #   else:
  #     print(f'You have already played your God Spell')
  # #print('in While')

print(f'Game Over')
time.sleep(1)
print(f'Final Points\n {p1_name} scored {player1._points} point(s)\n*********************************\n{p2_name} scored {player2._points} point(s)')
time.sleep(1)
if player1._points > player2._points:
  print(f'{p1_name} wins the game')
elif player2._points >  player1._points:
  print(f'{p2_name} wins the game')
else:
  print(f'Its a Tie!')
