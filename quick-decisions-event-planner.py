# question 2 task 1

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# question 2 task 2

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

if venue == "large hall":
    facilities = "speakers and projector"
else:
    facilities = "projector"

print("Recommended venue: " + venue)
print("Recommended facilities: " + facilities)

#question 2 task 3

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

if venue == "large hall":
    facilities = "speakers and projector"
else:
    facilities = "projector"

print("Recommended venue: " + venue)
print("Recommended facilities: " + facilities)

food = input("Would you like vegetarian food?")
if input == "yes":
    print("Recommended: Veggie Delight Caterers")
else:
    print("Recommended: Gourmet Meals Caterers")
