# Game-2-FiniteState
A finite state choose tour own adventure project


Game Documentation: Finite state lab
Game overview: In this thrilling story full of quizzes, chases, and even Elvis cults it is up to you to decide the outcome. This is a text choose your own adventure game where you get to decide between options 1 or 2 and alter the story. It is a much more comedic one that story wise doesn’t take itself seriously. 
Language: Python in Visual Studio Code. Because of this you just need python and should be fine unless I am forgetting something.

Technical side: This project will use a similar if not the same way you showed us in class for how to make a choose your own adventure. This means the game will be set up into functions to carry out the main tasks that will relay info to each other.

Functions:
loadGame: this will carry all the nodes and story branches. It’ll be set up as (node name, description, option a, node a, option b, node b). Each node will need two different paths they can go down to work properly. This’ll be sent around to tell everyone what to display and where to go.
playNode: This function is where the actual gameplay part will be stored. It will start by taking in and splitting up all the elements from loadGame as the earlier mentioned categories and will then start from whatever is set as the current node. Don’t worry that’ll be described more later. Next it’ll print out the description and the options you get to choose as well as an input box so you can actually tell the game what you want to do. From there you then have some if/elif statements that will make it so that if you chose 1 then you go forward on option A and if you pick 2 then option B. An element called newNode will then be set as this and later will be returned. Lastly, but before returning, there will be an else for error handling that if the user doesn’t do 1 or 2 you say “hey stop” and replay the current node till they play nice.
gameStart: This function will be important. It will feature the part that actually grabs the parts of loadGame to send to playNode as well as tell it what node to start on. In this case we will start with the first node start. From there we will use a while keepGoing loop to tell the game that whatever gets returned from playNode, remember newNode?, set as the new current node and play the game from there. This keeps the gameplay loop alive and well. Lastly I will add an if statement so that if the node returned is quit then keepGoing is set to false and the loop and game stops.
Main: main starts up gameStart.
Last if statement: starts main.

Learned: I think the part that’ll stick with me in this lab is the fact of how easy it was. Admittedly I had you for cs120 so I already knew it was already going to be easy but that isn’t exactly what I mean. It is such a simple game type but it is really fun. Not just to play but to code. It is one that because of its simplicity it lets you put more into the writing and such. That is what I mostly would say I learned. You don’t need big extravagant stuff to make a good and fun game.
Proud: I am proud of my story making. Again since that was the main focus to me I got to put some fun humor into it.
Additive: The main thing I want to add is a visual element. This’ll obviously take a sec to make so I don’t know if I will. I can’t draw the greatest so.

Nodes: (Translated to python by the tool you gave us on canvas)
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

