import sys, logging, json

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def render(game,current):
    '''Display the current location'''
    
    print("You are at" + game['room'][current]['name'])
    print(game['room'][current]['desc'])
    return True

def update(game,current,response):
    '''update our location, if possible. etc.'''
    for e in game['game']['room']['exists']:
        if response = e['verb']:
            current = e['target']
    return current

def check_input():
    '''check input'''
    response = input("What would you like to do? ")
    response = response.strip()
    response = response.upper()
    return response


def main():
    game = {}
    with open('zork.json') as json_file:
        game = json.load(json_file)
    # Your game goes here!

    current = 'WHOUS'

    quit = False
    while not quit:
        #render
        render()
        #check player input
        check_input()
        #update
        update()


    return True



#if we are running this from the command line, run main
if __name__ == '__main__':
	main()