import movie
import fresh_tomatoes

baahubhali_begin = movie.Movie("Baahubali: The Beginning",
                               "It's a tale of two cousins in the Kingdom of Mahishmati, India",
                               "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",
                               "https://www.youtube.com/watch?v=sOEg_YZQsTI")

baahubhali_conclusion = movie.Movie("Baahubali: The Conclusion",
                                    "It's tale of how Baahubali finishes Ballaladeva",
                                    "http://fugoes.com/wp-content/uploads/2015/07/Baahubali_Conclusion.jpg",
                                    "https://www.youtube.com/watch?v=L70RUBpunys")

lotr = movie.Movie("Lord of the Rings",
                   "It's story around on one evil ring, which always to try to return to it's evil master",
                   "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
                   "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

man_from_the_earth = movie.Movie("The Man from the Earth",
                                 "College professors discuss many topics with a colleague who claims to be thousands of years old",
                                 "https://upload.wikimedia.org/wikipedia/en/3/3b/The_Man_from_Earth.png",
                                 "https://www.youtube.com/watch?v=9mOIxyRTY5I")

live_free_or_die_hard = movie.Movie("Live Free or Die Hard",
                                    "As the nation prepares to celebrate Independence Day, veteran cop John McClane (Bruce Willis) carries out another routine assignment: bringing in a computer hacker (Justin Long) for questioning. Meanwhile, a tech-savvy villain named Thomas Gabriel (Timothy Olyphant) launches an attack on America's computer infrastructure. As chaos descends around him, McClane must use old-fashioned methods to fight the high-tech threat.",
                                    "https://upload.wikimedia.org/wikipedia/en/4/46/Live_Free_or_Die_Hard.jpg",
                                    "https://www.youtube.com/watch?v=v0qAZq0Zmcc")

in_time = movie.Movie("In Time",
                      "Story in a future where time is money and the wealthy can live forever",
                      "https://upload.wikimedia.org/wikipedia/en/e/e0/Intimefairuse.jpg",
                      "https://www.youtube.com/watch?v=fdadZ_KrZVw")

list_of_movies = [man_from_the_earth, in_time, baahubhali_begin, baahubhali_conclusion, lotr, live_free_or_die_hard]
fresh_tomatoes.open_movies_page(list_of_movies)
print movie.Movie.__module__