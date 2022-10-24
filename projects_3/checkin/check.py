from typing import Dict


students = {}

def input_students() -> Dict[str, bool]:
    print("Please provide the students names and then q to quit")
    while True:
      inp = input("> ") 
      if inp == "q":
        break # breaking will automatically go to the action input since the main has a while loop
      else:
        students[inp] = False 
    return students
        
def input_action() -> str:
    action = input("[check] sign ins, [sign] in, or [q]uit: \n > ")
    return action
      
def print_check_ins(students: Dict[str, bool]) -> None:
    for names in students: 
      if students[names] == True:
        print(f"{names}: Y")
      else:
         print(f"{names}: N")

def sign_in(students: Dict[str, bool]) -> None:
    name = input("> ")
    for student in students: 
      if student == name:
        students[student] = True
        
def main() -> None:
    input_students()
    if students == {}:
      print("No students were provided")
    else:
      while True:
          action = input_action()
          if action == "check":
              print_check_ins(students)
          elif action == "sign":
              sign_in(students)
          elif action == "q":
              break
          else:
              print("Please choose a valid action.")


if __name__ == "__main__":
    main()
