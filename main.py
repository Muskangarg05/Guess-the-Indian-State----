from turtle import Turtle, Screen
import pandas

s = Screen()
image = "Blank_Indian_map.gif.gif"
s.addshape(image)
tim = Turtle()
tim.shape(image) # Set the background map image--

t = Turtle()
t.penup()
t.hideturtle()

data = pandas.read_csv("States.csv")  
all_states = data.state.to_list()  # Create a list of all state names


guessed_state = []
while len(guessed_state) < 28:
    ans_state = s.textinput(title = f"{len(guessed_state)}/28 States correct", prompt = "What's another state's name?")
    ans_state = ans_state.title()

# Skip if input is empty or cancelled--    
    if not ans_state:
        continue 
    
    if ans_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        print(missing_states) 
        
        new_data = pandas.DataFrame(missing_states)  
        new_data.to_csv("Missing_States.csv") 
        break  
    
    if ans_state in all_states and ans_state not in guessed_state:
        guessed_state.append(ans_state)
        state_data = data[data.state == ans_state]  # Get row for that state
        t.goto(state_data.x.item(), state_data.y.item()) 
        t.write(ans_state) 
            
    if len(guessed_state) == 28:
        t.goto(0, 250)
        t.write("🎉 You guessed all states correctly! 🧨", font = ("Arial", 20, "bold"), align = "center")
      
s.bye()        