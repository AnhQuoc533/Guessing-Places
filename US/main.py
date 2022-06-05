import turtle
import time
from data import all_states


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.setup(width=726, height=491)
    screen.title("Name the US States")
    screen.bgpic("gfx/map.gif")

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()

    # for state, props in all_states.items():
    #     t.goto(props[0:2])
    #     t.write(state, align='center', font=("Arial", props[2], 'bold'))
    # screen.mainloop()

    found_states = set()
    try:
        # First time
        guess = screen.textinput(title="Name a State", prompt="What's that state's name?").title().strip()
        while guess != 'Exit' and guess not in all_states:
            guess = screen.textinput(title="Name a State", prompt="Wrong name, try again!").title().strip()

        if guess == 'Exit':
            raise AttributeError

        props = all_states.pop(guess)
        t.goto(props[0:2])
        t.write(guess, align='center', font=("Arial", props[2], 'bold'))

        display_text = "What's another state's name?"
        found_states.add(guess)

        while len(all_states):
            guess = screen.textinput(title=f"{len(found_states)}/50 States Correct", prompt=display_text).title().strip()

            if guess == 'Exit':
                raise AttributeError
            elif guess in found_states:
                display_text = "Already found, try another!"
            elif guess not in all_states:
                display_text = "Wrong name, try again!"
            else:
                props = all_states.pop(guess)
                t.goto(props[0:2])
                t.write(guess, align='center', font=("Arial", props[2], 'bold'))
                display_text = "What's another state's name?"
                found_states.add(guess)

        turtle.addshape("gfx/completed.gif")
        t.home()
        t.shape("gfx/completed.gif")
        time.sleep(0.5)
        t.showturtle()
        screen.mainloop()

    except AttributeError:
        try:
            t.color('red')
            for state, props in all_states.items():
                t.goto(props[0:2])
                t.write(state, align='center', font=("Arial", props[2], 'bold'))
            screen.mainloop()

        except turtle.Terminator:
            pass

    except turtle.Terminator:
        pass
