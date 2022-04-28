class Board:

   def __init__(self):
       self.reset()

   def reset(self):
       self.cells = [" " ," " ," " ," " , " ", " " ," " ," " ," " ]

   def display(self):
       print(self.cells)

   def position(self, userInput):
       return self.cells[userInput - 1]

   def update(self, position, playerToken):
       self.cells[position - 1] = playerToken
       return self.cells

   def taken(self, userInput):
       if(self.position(userInput) != " "):
           return False
       return True


   def valid_move(self, userInput):
       if userInput in range(1,9) and not self.taken(userInput):
           return True
       return False

   def full(self):
       for space in self.cells:
           if(space == " "):
               return False
       return True
   
   def turn_count(self):
       
       return len(filter(lambda cell: cell == "X" or cell == "Y", self.cells))

       
       
       
breakpoint()

