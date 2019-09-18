#import packages
try:
	import RandomWords
except:
    from pip._internal import main as pip
    pip(['install', '--user', 'RandomWords'])
    from random_words import RandomWords
try:
	from colorama import Fore, Back, Style
except:
	from pip._internal import main as pip
	pip(['install', '--user', 'colorama'])
	from colorama import Fore, Back, Style

rw = RandomWords()
import os
import time

#list of 7 possible states of the hangman
hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#define function to clear the screen
def clear_screen():
	return os.system('cls')

#game on/off switch
game_on = False

#opening statement
clear_screen()
print ('Welcome to the Hangman!\n')

#ask player to start the game
while game_on is False:	
	game_start = input ('Would you like to start a new game? [y/n]... ').upper()
	if game_start == 'Y':
		game_on = True
	elif game_start == 'N':
		game_on = False
		clear_screen()
	else:
		clear_screen()
		print ("Please input [y] or [n]")
clear_screen()

while game_on is True:
	#generate a random word to guess and transform to a list
	word_to_guess = rw.random_word()
	word_to_guess_list = list(word_to_guess)
	length_of_word_to_guess = len((word_to_guess_list))
	#generate a placeholder list for tried but wrong guesses
	tried_but_wrong = []
	#create a representation of word_to_guess_list with hidden spaces
	hidden_word = ('_')*length_of_word_to_guess
	hidden_word_list = list(hidden_word)

	#info about generated word to guess
	print ('I have just generated a random word for you to guess!')
	print (f'\nThe word has {length_of_word_to_guess} letters.')
	
	#initialize the number of attempts left
	attempts_left = 6
	hangman_state = 0
	print (f'\nYou have {attempts_left} attempts left.')

	#start the while loop for the game's logic
	while attempts_left>0 or hidden_word_list != word_to_guess_list:

		#initialize the guessed letter
		guess = ('')
		
		#print the current state of the hangman
		print (hangman_pics[hangman_state])
		
		#print the letter already used an not in the word to guess
		if tried_but_wrong == []:
			pass
		else:
			print(f'\nTip: you have alread tried these letters: {tried_but_wrong}\n')
		
		#while loop for guessing a letter 
		while len(guess) != 1 or type (guess) != str:
			print (f'This is the word you are trying to guess:'+'\n'*2+f'{hidden_word_list}')
			guess = input ('\nPlease select a letter you think is in the hidden word... ')
		clear_screen()
		
		#check if guessed letter is in the word to guess and not already guessed
		if guess in word_to_guess_list and guess not in hidden_word_list:
			print (f'''Great! You guessed correctly, "{guess}" is in the word you are trying to guess.''')
			
			#check the indices of guessed letter(s)
			print (f'You have {attempts_left} attempts left.')
			indices_of_guessed_letter = [i for i, x in enumerate(word_to_guess_list) if x == guess]
			
			#replace blank spots in hidden_word_list with guessed letter(s)
			for indices in indices_of_guessed_letter:
				hidden_word_list [indices] = guess
		
		#inform the player that they already guessed the selected letter
		elif guess in hidden_word_list:
			print ('Woops! Looks like you have already guessed this one! Please try again!')
		
		#inform the player that they already tried that letter and it's not in the word to guess
		elif guess in tried_but_wrong:
			print (f'There is no "{guess}" in the word you are trying to guess, but you have already tried that one.')
		
		#else: inform the player that they guessed wrong
		else:
			print (f'There is no "{guess}" in the word you are trying to guess.')
			
			#add the guessed and wrong letter to a list of already tried guesses
			tried_but_wrong.append(guess)

			#reduce the number of attempts left
			attempts_left -= 1

			#progress the hangman state
			hangman_state += 1

			#print the info about the number of attempts left
			print (f'You have {attempts_left} attempts left.')
		
		#check for win or loss

		#check for win
		if word_to_guess_list == hidden_word_list:
			time.sleep(2)
			clear_screen()
			print (f'You correctly guessed the word, which is ' + Fore.GREEN + f'"{word_to_guess}"'+ Style.RESET_ALL+'.')
			print (f'You had {attempts_left} attempts left.')
			break

		#check for loss
		if attempts_left == 0:
			time.sleep(2)
			clear_screen()
			print
			print (f"You lost. The word you were trying to guess was " + Fore.RED+ f'"{word_to_guess}"' + Style.RESET_ALL + '.')
			print ('\nUnfortunately, you are dead.')
			print (hangman_pics[hangman_state])
			break

	#ask if player wants to replay
	restart = False
	while restart is False:	
		game_restart = input ('\nWould you like to start a new game? [y/n]... ').upper()
		if game_restart == 'Y':
			restart = True
			clear_screen()
			game_on = True
		elif game_restart == 'N':
			restart = True
			clear_screen()
			print ("Thank you for playing!")
			time.sleep(3)
			game_on = False
			clear_screen()
		else:
			clear_screen()
			print ("Please input [y] or [n]")