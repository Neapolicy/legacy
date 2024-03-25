# American Fruit Ninja
## It's like Fruit Ninja, but better

### American Fruit Ninja is a point and click shooter game that is meant to entertain players with a fun yet somewhat difficult game of Fruit Ninja!
#
This game is written in Python using Pycharm
# WHAT THIS PROJECT IS
**This game is somewhat similar to a game of fruit ninja only in the sense that you shoot fruits**
Otherwise, it is mostly unique, with its main appeal of being much more difficult to play than the actual thing, mainly due to its reloading mechanic. You are placed under a timer to shoot as much fruits as you can, but you can extend that timer by using your ultimate. You have six bullets, once you run out of ammo, you can no longer fire any more bullets unless you reload. 
It's that simple!
# WHAT IT CAN DO
This project mainly runs on timestamping and collision detecting, where it detects if your mouse collides with a sprite.
While the timestamping comes to play whenever you reload and use your ultimate
# HOW TO INSTALL / RUN THE APP
This program comes as a ZIP file, so you will have to install that first, and then you will want to extract its contents. Copy and paste all the files from the extracted ZIP file into a program capable of running Python and you're pretty much finished with installing the game
## LIBRARIES TO INSTALL
There is only one module that you need to install and that is Pygame. To do that, you have to run in the console
```
pip install Pygame
```
Or if you're using Pycharm to run the game, go to Python packages. Then type in the search bar Pygame, there should then be a result that says Pygame
Click that and then click on install package, and voila! You're done installing the libraries required to play this game.

# DIRECTIONS / HOW TO PLAY
Shoot as many fruits as you can before the timer ends
---
With the main mechanic being reloading and your ultimate, you might ask, how do I do any of these?
* Press R to reload, it takes .5 second to reload, and your gun can only hold up to six bullets
* Press E to use your ultimate, where you can earn youself some points, get a small increase on your timer, and reload all your bullets
* Although it takes 5 ability points to use your ultimate, which you can obtain by chooting the fruits, with there only being a chance of giving you a point, don't worry though, you start out with a 5/5 ability points
* Some fruits also give more points, specifically, watermelons give 1 point, apples give 2, and oranges give 3
# MECHANICS
The main mechanics of this game is a reload system and an ultimate system, but both mechanics share pretty similar code, so only the reloading system will be explained, as it is functionally similar to the ultimate system.

The reloading system works by pressing R, whcih stops all of your actions, by setting a variable called action to False, action is required to be true to do anything. It also prevents you from using your ultimate as it has a tendency to break your game. (When you use your ultimate, you are also p[revented from reloading and doing anything in general as well!)

It then sets a timestamp variable to true, and adds a certain amount of seconds to that timestamp, once the elapsed time meets that timestamp, you will get a bullet, and actions will be set back to true, and you are allowed to use your ultimate again.