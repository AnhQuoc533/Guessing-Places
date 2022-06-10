import turtle
import time
from data import trans_table, provinces, alt_provinces


def decode(text):
    text = text.title().strip().translate(trans_table)

    if text in alt_provinces:
        text = alt_provinces[text]

    return text


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.setup(width=480, height=767, startx=0, starty=0)
    screen.title("Name the VN Provinces")
    screen.bgpic("gfx/vn-map.gif")

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()

    # for province in provinces.values():
    #     t.goto(province[0])
    #     t.write(**province[1])
    # screen.mainloop()

    found_prov = set()
    try:
        # First time
        guess = decode(screen.textinput(title="Name a Province", prompt="What's that province's name?"))
        while guess != 'Exit' and guess not in provinces:
            guess = decode(screen.textinput(title="Name a Province", prompt="Wrong name, try again!"))

        if guess == 'Exit':
            raise AttributeError

        props = provinces.pop(guess)
        t.goto(props[0])
        t.write(**props[1])

        display_text = "What's another state's name?"
        found_prov.add(guess)

        while len(provinces):
            guess = decode(screen.textinput(title=f"{len(found_prov)}/63 Provinces Correct", prompt=display_text))

            if guess == 'Exit':
                raise AttributeError
            elif guess in found_prov:
                display_text = "Already found, try another!"
            elif guess not in provinces:
                display_text = "Wrong name, try again!"
            else:
                props = provinces.pop(guess)
                t.goto(props[0])
                t.write(**props[1])
                found_prov.add(guess)
                display_text = "What's another province's name?"

        turtle.addshape("gfx/completed.gif")
        t.home()
        t.shape("gfx/completed.gif")
        time.sleep(0.5)
        t.showturtle()
        screen.mainloop()

    except AttributeError:
        try:
            t.color('red')
            for province in provinces.values():
                t.goto(province[0])
                t.write(**province[1])
            screen.mainloop()

        except turtle.Terminator:
            pass

    except turtle.Terminator:
        pass
