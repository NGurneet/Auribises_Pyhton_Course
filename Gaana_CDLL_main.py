from Gaana_CDLL_oops import song,playlist
def main():
    trending_songs = playlist()
    song1 = song("Tu Hai to Mujhe","Arijit","4:17")
    song2 = song("Chorni", "DIVINE, Sidhu Moose Wala", "4:17")
    song1.show()

    trending_songs.append(song=song1)
    trending_songs.append(song2)
    trending_songs.append(
        song=song(track="4. Chorni", artist="DIVINE, Sidhu Moose Wala", duration=4.12)
    )
    print("********************************")
    print("PRINTING PLAYLIST - FORWARD")
    trending_songs.iterate()

    print("PRINTING PLAYLIST - BACKWARD")
    trending_songs.iterate(1)

if __name__=="__main__":
    main()