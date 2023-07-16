
class song:
    def __init__(self,track,artist,duration):
        self.track = track
        self.artist = artist
        self.duration = duration
        self.next = None
        self.previous = None

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Track Name: ",self.track)
        print("Artist Name: ", self.artist)
        print("Duration Name: ", self.duration)
        print("Current Song: ",self,"Next Song: ",self.next,"Previous Song: ",self.previous)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


class playlist():

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def append(self,song):
        self.size += 1

        if self.head is None:
            self.head = song
            self.tail = song

        else:

            self.tail.next = song
            song.previous = self.tail
            self.tail = song

            # CIRCULAR
            self.head.previous = self.tail
            self.tail.next = self.head

    def iterate(self, direction=0):

        if direction == 0:
            temp = self.head
            while True:
                temp.show()
                temp = temp.next

                if temp == self.head:
                    break
        else:
            temp = self.tail
            while True:
                temp.show()
                temp = temp.previous

                if temp == self.tail:
                    break


