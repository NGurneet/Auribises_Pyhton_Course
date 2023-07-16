
class romantic_mix:



    def __init__(self,name="Name",album="Album",duration="0:00",artist="Artist"):
        self.name = name
        self.album = album
        self.duration = duration
        self.artist = artist

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Track Name: ",self.name)
        print("Album :",self.album)
        print("Duration: ",self.duration)
        print("Artist: ",self.duration)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

track1 = romantic_mix("Tu Hai to Mujhe","Tu Hai to Mujhe","4:17","Arijit")
track2 = romantic_mix()
track3 = romantic_mix("Udaariaan","Seasons of Sartaj","5:42","Satinder Sartaj")
track1.show()
track2.show()
track3.show()






