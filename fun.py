import sys
import os
import time
from playsound import playsound

def scrollText(text, sec=0.02):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(sec)

if __name__=="__main__":
	playsound('music.mp3', False)
	os.system('clear')

	print("\nTurn your sound ON =)")
	time.sleep(1)

	os.system('clear')

	scrollText("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠖⠒⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⡀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⣸⣽⣿⣽⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣷⡀⠀⠀⠀⠀⠀⠀⣼⣇⠀⢸⣿⣿⣿⣿⡏⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣧⠀⠀⠀⠀⠀⢰⣿⣿⡀⢸⣿⣿⢻⣿⡇⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣛⣿⣻⠀⠀⠀⠀⠀⢸⣿⣿⠀⢸⣿⣿⣾⣿⡇⢀⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣧⡀⠀⠀⠀⠀⣿⣿⣿⣷⢸⣿⣿⣿⣿⣇⣀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⢿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⢠⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣼⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠀⣼⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⢠⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⢠⣿⣿⣿⠀⠀⢰⡄⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⢧⢤⢤⢤⢼⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣀⣀⣀⣾⡿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⠀⠻⣿⢿⡿⠇⠀⣼⣧⠀⠀⠀⠀⣀⣀⣀⣸⣿⣿⣿⣿⣿⣾⣾⣾⣾⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣷⣷⣿⣷⣿⠄⠀⠀⠀⠀⠀⠀⡷⠶⠆⠀⠀\n", 0.005)
	scrollText("⠀⢾⣿⣿⣿⡇⢰⣿⣿⡄⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⣠⣿⣿⢿⣿⡇⢸⣿⣿⡃⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n", 0.005)
	scrollText("⣛⣿⣿⣼⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣧⠀⠀⠀⠀\n", 0.005)
	scrollText("⠹⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣧⡀⠀⠀\n", 0.005)
	scrollText("⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⡿⣿⣿⡿⣿⣿⠿⣿⣿⠿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣏⣿⠃⠀⠀⠀⣰⣿⣿⣿⣿⣷⡀⠀\n", 0.005)
	scrollText("⠀⢸⣿⣿⣿⣿⣿⣿⣿⡟⠀⣿⣿⡇⣿⣿⠀⣿⣿⠀⣿⣿⠀⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⠃⠀\n", 0.005)
	scrollText("⠀⢸⣿⣿⣿⣿⣿⣿⣿⣧⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⢸⣿⣿⢻⣿⣿⣷⡄\n", 0.005)
	scrollText("⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢀⠀⣸⣿⣿⣾⣿⣿⣯⡇\n", 0.005)
	scrollText("⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃\n", 0.005)
	scrollText("⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀\n", 0.005)
	scrollText("⠀⠸⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠀\n", 0.005)
	print("\033[93m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m")
	print("\033[93m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⣤⣠⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⠀⠐⣾⢴⣄⣠⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m")
	print("\033[93m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⢸⣿⢀⣠⡴⠲⣦⠀⣾⡇⢸⣿⠀⢸⣿⠀⣤⠀⢻⡇⠙⠁⣿⡇⠀⣿⠘⠉⢸⣿⠀⢀⡠⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m")
	print("\033[93m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣀⣿⣿⣀⣼⣿⠉⢹⣇⠀⣿⡇⣿⡇⢀⣿⠀⢸⣿⠀⣿⠀⣿⡇⣾⡇⣿⡇⠀⣿⠀⠀⢸⣿⠀⠙⢷⣜⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m")
	print("\033[93m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⢸⣿⠀⠸⣿⠀⣿⠇⠛⠷⠋⣿⠀⠘⢿⡼⠻⣴⠋⠀⠸⠷⠿⠋⠀⠛⠀⠀⢸⣿⠀⢴⡆⢻⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m")
	print("\033[93m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠀⢸⣿⠀⠀⠈⠉⠁⠀⣀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠀⠀⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m")
	print("\033[93m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⠂⠀⠀⠀⠀⠀⢿⡦⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m\n")

	time.sleep(2)

	scrollText("\t\t\t\033[01mHorror!\n\n\033[0m")
	scrollText("Since its creation, the famous school of sorcerer, Hogwarts, had \nnever known such offense.\n")
	scrollText("The forces of evil have bewitched the magic Sorting Hat. The latter \nno longer responds, as if he was dazed, and is unable to fulfill \nhis role of distributing the students in the four famous houses.\n")
	scrollText("Start of the academic year is approaching.\n")
	scrollText("Professor McGonagall asserted the situation: impossible for Hogwarts \nnot to welcome new students...\n")
	scrollText("She decides to call you, a \"datascientist\" muggle, capable of working \nmiracles with this tool that all muggles use: a \"computer\".\n")
	scrollText("Despite the reluctance of many sorcerers, the principal of the school \nwelcomes you in her office to explain the situation. The reason \nyou’re here is because her contact revealed that you’re \ncapable of recreating a magical Sorting Hat using your muggly tools \nalone.\n")
	scrollText("You agree. You explain that for \"magic\" to work, you must retrieve \nstudent data. McGonagall then gives you a dusty grimoire. Fortunately \nfor you, a simple \"Digitalis!\" and the book changes into a flash \ndrive...\n")

	time.sleep(2)
	input("Press enter to continue ...\n")
	os.system("clear")

	scrollText("\n\t\t\t\033[01mData Analysis\n\n\033[0m")
	scrollText("First, you have to analyze your dataset.\n")
	scrollText("After opening the files and being a little terrified by it \nyou wish to output some statistical resume of your data.\n")
	scrollText("\nYou write the file \033[01mdescribe.py\033[0m. It takes a dataset as argument.\n")
	scrollText("\n\033[01mPlease enter the file path to the dataset you wish to analyze:\033[0m\n")
	scrollText("\033[03mAvailable: datasets/dataset_train.csv datasets/dataset_test.csv\n")
	scrollText("To pass, enter 'pass'\033[0m\n\n")

	inp = input("--> ")
	while inp != "pass":
		os.system('clear')
		print("Analysis result:\n")
		os.system("python3 describe.py " + inp)
		inp = input("\nPress enter to clear...")
		os.system('clear')
		print("Please enter the file path to the dataset you wish to analyze:")
		print("\033[03mAvailable: datasets/dataset_train.csv or datasets/dataset_test.csv")
		print("To pass, enter 'pass'\033[0m\n")
		inp = input("--> ")

	os.system('clear')

	scrollText("\n\t\t\t\033[01mData Vizualization\n\n\033[0m")
	scrollText("Secondly, you wish to vizualize your data with graphical representations.\n")
	scrollText("McGonagall seems curious to understand your own kind of magic and\nkeeps glancing in your direction.\n")
	scrollText("\nDo you wish to give her explanations or do you prefer to keep it a secret?\n")
	scrollText("\033[03mEnter 'yes' and informations will be displayed.\n")
	scrollText("Enter 'no' and only graphics will be showed.\033[0m\n\n")

	expl = input("--> ")
	while expl != "no" and expl != "yes":
		os.system('clear')
		inp = input("\nOption non recognized, press enter...")
		os.system('clear')
		print("Do you wish to give her explanations or do you prefer to keep it a secret?")
		print("\033[03mEnter 'yes' and informations will be displayed.")
		print("Enter 'no' and only graphics will be showed.\033[0m\n")
		expl = input("--> ")

	os.system('clear')

	if expl == "yes":
		scrollText("You write the file \033[03mhistogram.py\033[0m. It takes no argument.\n\n")
		os.system("python3 histogram.py -expl")
		scrollText("You write the file \033[03mscatter_plot.py\033[0m. It takes no argument.\n\n")
		os.system("python3 scatter_plot.py -expl")
		scrollText("You write the file \033[03mpair_plot.py\033[0m. It takes no argument.\n\n")
		os.system("python3 pair_plot.py -expl")
	else:
		scrollText("You choose to ignore McGonagall, thinking it'll be faster this way.\nYou're also a little dry to never have gotten a letter for Hogwarts.\nShe leaves after some time.\n\n")
		scrollText("You write the file \033[03mhistogram.py\033[0m. It takes no argument.\n\n")
		os.system("python3 histogram.py")
		scrollText("You write the file \033[03mscatter_plot.py\033[0m. It takes no argument.\n\n")
		os.system("python3 scatter_plot.py")
		scrollText("You write the file \033[03mpair_plot.py\033[0m. It takes no argument.\n\n")
		os.system("python3 pair_plot.py -expl")

	input("Press enter to continue ...\n")
	os.system('clear')

	scrollText("\n\t\t\t\033[01mLogistic Regression\n\n\033[0m")
	scrollText("Finally, you must construct and train your model.\n")
	scrollText("You'll be able to predict houses of students later.\n")
	scrollText("Here, you will use a One-vs-All logistic regression model.\n")

	if expl == 'yes':
		scrollText("Someone barge into the headmistress study: \nA student accidently transformed another kid into porridge.\n")
		scrollText("She needs to take care of it, and leave quickly.\n")
		scrollText("Do you wish to wait for her and continue the explanations ?\n")
		scrollText("\033[03mEnter 'yes' and informations will be displayed.\n")
		scrollText("Enter 'no' and only results will be showed.\033[0m\n\n")
	else:
		scrollText("McGonagall come back to her office. She asks you if everything is fine.\n")
		scrollText("Do you wish to explains to her what you are doing ?\n")
		scrollText("\033[03mEnter 'yes' and informations will be displayed.\n")
		scrollText("Enter 'no' and only results will be showed.\033[0m\n\n")

	new_expl = input("--> ")
	while new_expl != "no" and new_expl != "yes":
		os.system('clear')
		inp = input("\nOption non recognized, press enter...")
		os.system('clear')
		print("Do you wish to give her explanations for the model training part ?")
		print("\033[03mEnter 'yes' and informations will be displayed.")
		print("Enter 'no' and only results will be showed.\033[0m\n")
		new_expl = input("--> ")

	os.system('clear')

	if expl == 'yes' and new_expl == 'no':
		scrollText("Having a Sorting Hat is more urgent than waiting for the headmistress. \nYou don't wait for her.\n")
	elif expl == 'no' and new_expl == 'no':
		scrollText("Nah. Even though the headmistress been nothing but respectful to you, you \ndon't like how wizards call you 'muggle'.\n")

	scrollText("You write the file \033[03mlogreg_train.py\033[0m. It takes the dataset to train on as argument.\n\n")
	scrollText("\n\033[01mPlease enter the file path to the dataset you wish to train on:\033[0m\n")
	scrollText("\033[03mAvailable: datasets/dataset_train.csv\n")
	scrollText("To pass, enter 'pass'\033[0m\n\n")

	inp = input("--> ")
	while inp != "pass":
		os.system('clear')
		if new_expl == 'yes':
			os.system("python3 logreg_train.py " + inp + " -expl")
		else:
			os.system("python3 logreg_train.py " + inp)
		inp = input("\nPress enter to clear...")
		os.system('clear')
		print("You write the file \033[03mlogreg_train.py\033[0m. It takes the dataset to train on as argument.\n\n")
		print("Please enter the file path to the dataset you wish to train on:")
		print("\033[03mAvailable: datasets/dataset_train.csv")
		print("To pass, enter 'pass'\033[0m\n")
		inp = input("--> ")

	input("Press enter to continue ...\n")
	os.system("clear")

	scrollText("You saved the weights of your model in \033[03mthetas.npz\033[0m file.\n\n")
	scrollText("You write the file \033[03mlogreg_predict.py\033[0m. \nIt takes the dataset to predict and the weights' file as arguments.\n\n")
	scrollText("\n\033[01mPlease enter the file path to the dataset you wish to perform prediction on:\033[0m\n")
	scrollText("\033[03mAvailable: datasets/dataset_test.csv\n")
	scrollText("To pass, enter 'pass'\033[0m\n\n")
	dataset = input("--> ")
	weights = ""

	while dataset !='pass' and weights != 'pass':
		scrollText("\n\033[01mPlease enter the weights' file path:\033[0m\n")
		scrollText("\033[03mAvailable: thetas.npz\n")
		scrollText("To pass, enter 'pass'\033[0m\n\n")
		weights = input("--> ")
		if weights != 'pass':
			os.system('clear')
			if new_expl == 'yes':
				os.system("python3 logreg_predict.py " + dataset + " " + weights + " -expl")
			else:
				os.system("python3 logreg_predict.py " + dataset + " " + weights)
			scrollText("You write the file \033[03mlogreg_predict.py\033[0m. \nIt takes the dataset to predict and the weights' file as arguments.\n\n")
			scrollText("\n\033[01mPlease enter the file path to the dataset you wish to perform prediction on:\033[0m\n")
			scrollText("\033[03mAvailable: datasets/dataset_test.csv\n")
			scrollText("To pass, enter 'pass'\033[0m\n\n")
			dataset = input("--> ")

	os.system("clear")
	input("Press enter to continue ...\n")
	os.system("clear")

	scrollText("Congratulations !\nYou finished building a working Sorting Hat algorithm.\n\n")
	scrollText("\n\t\t\t\033[01mTHE END\n\n\033[0m")

	input("Press enter to continue ...\n")
	os.system("clear")
