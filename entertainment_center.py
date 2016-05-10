import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story about a toy",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine in an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

civil_war = media.Movie("Marvel: Civil War",
                        "Fight between 2 groups of superheroes.",
                        "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                        "https://www.youtube.com/watch?v=43NWzay3W4s")

bvs = media.Movie("Batman vs Superman",
                  "Batman vs Superman",
                  "https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg",
                  "https://www.youtube.com/watch?v=x177jhcMSqg")

martian = media.Movie("Martian",
                      "Astronout stuck in Mars.",
                      "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                      "https://www.youtube.com/watch?v=ej3ioOneTy8")

deadpool = media.Movie("Deadpool",
                       "A former Special Forces operative turned mercenary "
                       " is subjected to a rogue experiment that leaves him "
                       "with accelerated healing powers, adopting the alter ego Deadpool.",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=8wrdUol28hM")

# movies is an array with the Movie objects.
movies = [toy_story, avatar, civil_war, bvs, martian, deadpool]

# Calls open_movies_page() function and passing movies list of Movie objects.
# This function will generate a HTML based on the list of Movie objects.
fresh_tomatoes.open_movies_page(movies)
