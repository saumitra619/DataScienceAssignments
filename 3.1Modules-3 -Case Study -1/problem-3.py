from datetime import datetime

def get_part_of_day(hour):
     if 5 <= hour <= 18 :
          return "light"
     else :
          return "dark"


h = datetime.now().hour

print(f"Its {get_part_of_day(h)} right now.")  