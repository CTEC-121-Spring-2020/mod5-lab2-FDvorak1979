"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

#def vers(name):
'''
    def refrain:
    print("name, "finger,", name, "finger, where are you?")

def main():
    singgFingerFamilySong():
    verse("Daddy")
    refrain()

    singgFingerFamilySong():
    verse("Momnmy")
    refrain()

     singgFingerFamilySong():
    verse("Brother")
    refrain()

     singgFingerFamilySong():
    verse("Sister")
    refrain()

     singgFingerFamilySong():
    verse("Baby")
    refrain()

main()    

'''

def ageRange(age):
    if age > 120:
        return 'X: Ancient or Immortal'
    elif age > 18  <= 120:
        return  'A: Adult'
    elif age > 13 and age <= 18:
        return  'T: Teen'
    elif age > 1 and age <= 13:
        return  'C: Child'
    elif age > 0 and age <= 1:
        return  'I: Infant'
    

print("I am 1 years old", ageRange(1))
print("I am 8 years old", ageRange(8))
print("I am 15 years old", ageRange(15))
print("I am 41 years old", ageRange(41))
print("I am 9,768 years old", ageRange(9768))
