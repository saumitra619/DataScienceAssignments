
import math 

initial_position = [0,0] 

while True: 
  user_input = input("Enter trace :- ") 
  if not user_input: 
    break 
  movement = user_input.split(" ") 
  
  direction = movement[0] 
  steps = int(movement[1]) 
  
  if direction=="UP": 
    initial_position[0]+=steps 
  elif direction=="DOWN": 
    initial_position[0]-=steps 
  elif direction=="LEFT": 
    initial_position[1]-=steps 
  elif direction=="RIGHT": 
    initial_position[1]+=steps 
  else: 
    pass 
# calculating the distance using pythagorus hypotenuse length

distance = math.sqrt(initial_position[1]**2+initial_position[0]**2)
print(int(round(distance)))
