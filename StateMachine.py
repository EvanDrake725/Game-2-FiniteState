def loadGame():
    game = {
      "start": ["You are at home relaxing when you hear a knock at the door.", "Check the door", "check", "Don't pay it any mind", "relax"], 
      "check": ["You decide to check the door and it is none other than THE Evlis Presley!!", "Open the door", "open", "This can't be real.", "dont"], 
      "open": ["You open the door but it turns out to be an impersonator. They get in and knock you out. When you awake you are tied to a chair in your basement.", "Try to untie yourself", "untie", "Stay still and wait for them to return", "stay"], 
      "untie": ["You try to untie yourself and do! Now you need to try to get out!", "Run upstairs and escape.", "run", "Crawl through the convenient you sized air duct you have.", "duct"], 
      "run": ["You run upstairs but on your way to the door they catch you again.", "Struggle free", "struggle", "Don't struggle free", "let"], 
      "struggle": ["You struggle free and get outside. Once outside you call the cops and they arrest the Elvis. You are safe but can never trust musician look alikes ever again.", "Restart?", "start", "Quit?", "quit"], 
      "let": ["You stupidly let them take you again. The impersonator is no longer playing nice and thus sends his lion that all Elvis fans have to get you. It gets you.", "Restart?", "start", "Lions are dumb anyways.", "quit"], 
      "stay": ["You decide to stay still and see if you can reason with them and you can. Under the condition you listen to them sing.", "Listen", "listen", "Their music probably sucks.", "noListen"], 
      "listen": ["You listen and they werent half bad. Once they are done they leave and life goes back to normal", "Restart?", "start", "Quit?", "quit"], 
      "noListen": ["You say no and anger them. As punishment you are mind controlled into a fellow Elvis impersonator. You then find yourself pulling this scheme till everyone has fallen and become Elvis.", "Restart?", "start", "You quite like the Elvis life.", "quit"], 
      "duct": ["You crawl in the vents all stealthy like. You eventually make it to your garage and attempt to open the garage to escape. This alerts your kidnapper though.", "Run through the garage door", "garage", "Fight them", "fight"], 
      "garage": ["You try to run through the open garage door. This leads to them chasing after you but it seems that they forgot a major element. Eating peanut butter, banana, and bacon sandwiches everyday isnt healthy. You get away easily.", "Restart?", "start", "Quit?", "quit"], 
      "fight": ["You decide to fight. To take back your home. You kinda just push em and like a turtle they cant get back up. Very anti climactic but hey you get your house back I guess.", "Restart?", "start", "That sucked", "quit"], 
      "dont": ["You decide that this has to be some bit or something so you walk away from the door. He keeps being very noisy.", "Call the cops on him", "cops", "Relax and don't worry", "relax"], 
      "cops": ["You decide to call the cops on him since hes being such a nucence. Turns out he was part of some Elvis themed Illuminati or something it doesnt matter in this path. You are branded a hero.", "Elvis cult? What!?", "start", "Im fine", "quit"], 
      "relax": ["You decide to just relax and not worry. You then remember you have a project do!!", "Complete the project", "complete", "Eh you'll do it later", "later"], 
      "later": ["Welp you didnt do it later. Dont know what you expected. F-", "I really need to study", "start", "Skool iz stupd aniwys", "quit"], 
      "complete": ["You decide to really hunker down and complete the project. You get an A+ good job.", "Wonder what other paths there were?", "start", "Well that was a kinda short experience", "quit"], 
     }
    return game

def playNode(game,currentNode):
    (desc,menuA,nodeA,menuB,nodeB)=game[currentNode]
    print(f"""
    {desc}
    1.{menuA}
    2.{menuB}
    """)
    userChoice=input("Your choice:")
    if userChoice=="1":
        newNode=(nodeA)
    elif userChoice=="2":
        newNode=(nodeB)
    else:
        print("Please type 1 or 2")
        newNode=playNode(game, currentNode)
    return newNode

def gameStart():
    game=loadGame()
    currentNode="start"
    keepGoing=True
    while keepGoing:
        currentNode=playNode(game,currentNode)
        if currentNode=="quit":
            keepGoing=False

def main():
    gameStart()

if __name__=="__main__":
    main()