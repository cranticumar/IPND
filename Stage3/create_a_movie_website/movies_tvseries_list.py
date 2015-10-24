from movies import Movie
from tv_series import Tvseries
import fresh_tomatoes

friends = Tvseries(
    "F.R.I.E.N.D.S",
    "https://upload.wikimedia.org/wikipedia/commons/b/bc/Friends_logo.svg",
    "22 min",
    "https://www.youtube.com/watch?v=67hDG_tzRvE",
    "Sep 22, 1994",
    "May 06, 2004",
    "10",
    "236",
    "In this 1994 sitcom, Rachel Green, Ross Geller, Monica Geller, Joey Tribbiani, Chandler Bing and Phoebe Buffay are all friends, living off of one another in the heart of NY.")

bb_begin = Movie(
    "Baahubali: The Beginning",
    "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",
    "158 min",
    "https://www.youtube.com/watch?v=3NQRhE772b0",
    "Jul 01, 2015",
    "It's a tale of two cousins in the Kingdom of Mahishmati, India")

lotr = Movie(
    "Lord of the Rings: The Return of the King",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
    "201 min",
    "https://www.youtube.com/watch?v=r5X-hFf6Bwo",
    "Dec 01, 2003",
    "It's story around one evil ring, which always to try to return to it's evil master")

mfte = Movie(
    "The Man from the Earth",
    "https://upload.wikimedia.org/wikipedia/en/3/3b/The_Man_from_Earth.png",
    "89 min",
    "https://www.youtube.com/watch?v=9mOIxyRTY5I",
    "Nov 13, 2007",
    "College professors discuss many topics with a colleague who claims to be thousands of years old")

lfodh = Movie(
    "Live Free or Die Hard",
    "https://upload.wikimedia.org/wikipedia/en/4/46/Live_Free_or_Die_Hard.jpg",
    "130 min",
    "https://www.youtube.com/watch?v=v0qAZq0Zmcc",
    "Jun 27, 2007",
    "As the nation prepares to celebrate Independence Day, veteran cop John McClane (Bruce Willis) carries out another routine assignment: bringing in a computer hacker (Justin Long) for questioning. Meanwhile, a tech-savvy villain named Thomas Gabriel (Timothy Olyphant) launches an attack on America's computer infrastructure. As chaos descends around him, McClane must use old-fashioned methods to fight the high-tech threat.")

it = Movie(
    "In Time",
    "https://upload.wikimedia.org/wikipedia/en/e/e0/Intimefairuse.jpg",
    "109 min",
    "https://www.youtube.com/watch?v=fdadZ_KrZVw",
    "Oct 28, 2011",
    "Story in a future where time is money and the wealthy can live forever")

list_of_videos = [friends, bb_begin, lotr, mfte, lfodh, it]
fresh_tomatoes.launch_website(list_of_videos)