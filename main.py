import turtle
import pandas

screen = turtle.Screen()
screen.screensize()
screen.title("English Counties Game")
image = "BEC_500.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("English_Counties.csv")
all_counties = data["County"].tolist()
guessed_counties = []


while len(guessed_counties) < 41:
    answer_county = turtle.textinput(title=f"{len(guessed_counties)} out of 48",
                                     prompt="Guess a County: ").title()
    if answer_county == "Exit":
        missing_counties = [county for county in all_counties if county not in guessed_counties]
        new_data = pandas.DataFrame(missing_counties)
        new_data.to_csv("counties_to_learn.csv")
        break

    if answer_county not in guessed_counties:
        if answer_county in all_counties:
            guessed_counties.append(answer_county)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            county_data = data[data.County == answer_county]  # fetches row info where county = answer_county
            t.goto(int(county_data.x), int(county_data.y))
            t.write(answer_county)  # county_data.County.item() - will use first piece of info from row
