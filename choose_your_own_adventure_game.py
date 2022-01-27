name = input(" What is your name: ")
print("welcome to this adventure, ",name)

answer=input("You wake up in the center of a moss-covered clearing. Look around. Pine trees and ferns in every direction. A mesmerising smell moves in the moist and cool air. Birds can be heard in the distance. No signs of civilisation. <Climb> up a tree or make your way through the <thicket> (c/t): ").lower()

if answer == "t":
    answer=input("You start walking, finding it hard to push through the thicket of ferns. Luckily, you find a knife in your shoulder bag, aiding your trek. You focus on covering as much distance as possible. Hours must have passed. You stumble, realising too late that the fading sun barely offers enough light to see where you are stepping. You panic, searching your surroundings for anything offering shelter. You spot a small opening between the roots of a gigantic tree. It may be just enough to fit in and hide from whatever creatures are starting to emerge in the dark. Do you use the <shelter> or keep <walking>? (s/w):  ")
    if answer == "s":
        print("You squeeze yourself into the small opening, realising in relief that it offers just enough space for you to hide. Exhausted, you are about to doze off when you notice the slimy surface of your surroundings. You must have crushed something on your way in. The foul smell of its remnants gets stronger too fast, making you sick. You spot the subtle silhouettes of mushrooms around you, just before your vision starts to blur. You lose consciousness. Game over.")
    elif answer == "w":
        print("You keep walking, stumbling more and more often and getting caught in bushes and ferns. Trying hard to see what's in front of you, you miss the sound of soft steps approaching from somewhere too close. Too late, you hear it jump in your direction, whatever carnivore it may be. All you feel is sharp teeth in your flesh and blood starting to flow down your skin. Game over.")
    else:
        print("invalid answer, please restart the adventure.")

elif answer == "c":
    answer=input("Sweat starts flowing down your back. The tree is harder to climb than it first looked, and you're finding it hard to hold on to the slick branches. You decide to take a rest on one of the larger forked branches, when you see it. Your leg. Iridescent tiny dots moving around. You take a closer look only to note with dismay that they are hundreds of insects you've not ever seen before. You grab your shoulder bag and frantically search for a tool. You find a <spray> can and a bottle of <water>. What do you grab? (s/w)")
    if answer == "s":
        answer=input("You spray the contents onto the alien looking creatures, realising in horror that they are inflating and starting to burst. The emerging gas is triggering a sharp pain in your head. Before you realise what is happening you watch yourself fall off the tree, unable to grab onto any of the branches you pass. You find yourself lying on the moss-covered ground, paralised. You lost.")
    elif answer == "w":
        answer=input("You empty the bottle's contents onto your leg and watch the horrifying creatures flow down the tree. Relieved, but aware that you have nothing left to drink from. You continue to climb as fast as you can, paying close attention to the tree's surface. To your delight, you reach the treetop and spot smoke emerging from a section of the vast forest not far from you. You take a closer look into your shoulder bag and see a <compass> and a <map>. What do you grab? (c/m)")
        if answer == "c":
            answer=input("You grab the compass and check the direction in which you see the smoke. North west. You must reach this place before dusk. Hurrying down the tree, you hold onto your compass and start to run. North West. You run as far as your feet take you, constantly checking if you're staying on track. You start to feel tired, watching the sun disappear behind the trees. Just before you think you can't walk any longer, you smell the food, cooking on a fire nearby. You enter a clearing. The house. You win. ")
        elif answer == "m":
            answer=input("You find a small house on the center of the map. It must be the place nearby emitting smoke. There is a small path leading to its entrance. All you have to do is to find it. You climb down the tree and start running. Once you find the path, you'll be able to tell where you are on the map. You walk. Ferns and pines. And more ferns. You start running. Every place looks just like where you've been before. There is no path. It is starting to rain. You quickly fold and pack your map back into the bag. You have to climb another tree, what if you're even further from the house than before? Grab the first large branch you can find. Slippery. You have to keep trying. The rain becomes so strong, you can barely see. You grab the next branch.. you miss it. The next thing you remember is falling flat on your back. Who knows from what height. The shooting pain in your leg indicates a fractured bone. No more climbing. Game Over.")
        else:
            print("invalid answer, please restart the adventure.")
    else:
        print("invalid answer, please restart the adventure.")


elif answer == "t":
    answer=input("You took the right turn while it's getting darker, you kept walking for an hour . Suddenly you a town with lights and restraunts and bars. What would you do ? Go back or go to the town? Write(back/town): ")

    if answer == "back":
        print("You are on your way back as quickly as possible then you drive back home safely. ")
    elif answer == "town":
        print("You are so happy that you found a town. You to a restraunt and you eat and happy. You wake up suddenly discovering that you are being chopped and turned into minced meat. Appearantly it is a canabalist town. ")
    else:
        print("invalid answer you lost")

else:
    print("invalid answer you lost")
