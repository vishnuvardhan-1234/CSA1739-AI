
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

while True:
    print("Location:", location)
    print("Room status:", rooms)

    if rooms[location] == "Dirty":
        rooms[location] = "Clean"
        print("Action: Suck")
    elif location == "A":
        location = "B"
        print("Action: Move Right")
    else:
        location = "A"
        print("Action: Move Left")

    if all(status == "Clean" for status in rooms.values()):
        print("All rooms are clean!")
        break
