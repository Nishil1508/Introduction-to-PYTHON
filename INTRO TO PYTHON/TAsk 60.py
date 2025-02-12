# Write python program that user to enter only odd numbers, else will raise an exception. 

def get_odd_number():
    while True:
        try:
            
            user_input = int(input("Please enter an odd number: "))
            
            
            if user_input % 2 != 0:
                print(f"Thank you! You entered the odd number: {user_input}")
                break
            else:
               
                raise ValueError("That's not an odd number!")
        
        except ValueError as e:
         
            print(f"Error: {e}. Please try again.")


get_odd_number()
