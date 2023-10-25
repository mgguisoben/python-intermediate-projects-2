from turtle import Turtle, Screen
import pandas

def get_states():
    data_file = pandas.read_csv("50_states.csv")

    states_dict = {}

    for _, state in data_file.iterrows():
        states_dict[state.state] = (state.x, state.y)

    return states_dict


states = get_states()

screen = Screen()
screen.setup(width=725, height=492)
screen.title("US States Game")
screen.bgpic("blank_states_img.gif")

t = Turtle()
t.penup()
t.hideturtle()

user_guesses = []

while len(user_guesses) < 50:

    user_input = screen.textinput(f"{len(user_guesses)}/50 correct guesses", "Name a US state:").title()

    if user_input in states.keys():
        user_guesses.append(user_input)
        t.goto(states[user_input])
        t.write(user_input, font=('Arial', 10, 'normal'))

    elif user_input == 'Exit':
        break

not_guessed = {"states": []}

for state in states.keys():
    not_guessed['states'].append(state)

pandas.DataFrame(not_guessed).to_csv("not_guessed.csv")


