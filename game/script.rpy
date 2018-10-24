# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#Declare background images

#Intro
image intro0 = 'images/intro/spr_intro_all_0.png'
image intro1 = 'images/intro/spr_intro_all_1.png'
image intro2 = 'images/intro/spr_intro_all_2.png'
image intro3 = 'images/intro/spr_intro_all_3.png'
image intro4 = 'images/intro/spr_intro_all_4.png'
image intro5 = 'images/intro/spr_intro_all_5.png'
image intro6 = 'images/intro/spr_intro_all_6.png'
image intro7 = 'images/intro/spr_intro_all_7.png'
image intro8 = 'images/intro/spr_intro_all_8.png'
image intro9 = 'images/intro/spr_intro_all_9.png'
image intro10 = 'images/intro/spr_intro_all_10.png'
image intro11 = 'images/intro/spr_intro_all_11.png'
image intro12 = 'images/intro/spr_intro_all_12.png'
image introbedroom = 'images/intro/bg_introduction.png'





define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    jump intro


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
