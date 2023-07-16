"""
    Circular Doubly Linked List
"""

class song():

    def __init__(self,track,artist,duration):
        self.track = track
        self.artist = artist
        self.duration = duration
        self.next = None
        self.previous = None

    def show(self):
        print("Track Name: ",self.track)
        print("Artist Name: ", self.artist)
        print("Duration Name: ", self.duration)
        print("Current Song: ",self,"Next Song: ",self.next,"Previous Song: ",self.previous)

def main():
    song1 = song("Tu Hai to Mujhe","Arijit","4:17")
    song2 = song("Chorni", "DIVINE, Sidhu Moose Wala", "4:17")
    song3 = song("Tu Hai to Mujhe", "Arijit", "4:17")
    song4 = song("Tu Hai to Mujhe", "Arijit", "4:17")
    song5 = song("Tu Hai to Mujhe", "Arijit", "4:17")

    song1.next = song2
    song2.next = song3
    song3.next = song4
    song4.next = song5
    song5.next = song1

    song1.previous = song5
    song2.previous = song1
    song3.previous = song2
    song4.previous = song3
    song5.previous = song4

    temp = song1
    print("Printing the Linked Song Objects :)")
    print("Iterating in Forward Direction...")
    while True:
        temp.show()
        temp = temp.next

        if temp == song1:
            break
    print("Iterating in Backward Direction...")
    temp = song5
    while True:
        temp.show()
        temp = temp.previous

        if temp == song5:
            break

if __name__ =="__main__":
    main()