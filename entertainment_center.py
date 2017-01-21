import media
import fresh_tomatoes
import tmdbsimple as tmdb
import API

tmdb.API_KEY = API.my_key
search = tmdb.Search()
path = "http://image.tmdb.org/t/p/w185//" 

# search movie by title from tmdb database
response = search.movie(query='finding dory')
# store result from search
s = search.results[0]

#Creating instance of Movie class that takes 4 arguments - title, description,
# and web URL
finding_dory = media.Movie(s['title'], s['overview'], path+s['poster_path'],
                    "https://www.youtube.com/watch?v=3JNLwlcPBPI")

response = search.movie(query='dark knight')
s = search.results[0]
dark_knight = media.Movie(s['title'], s['overview'], path+s['poster_path'],
                    "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

response = search.movie(query='avengers')
s = search.results[0]
avengers = media.Movie(s['title'], s['overview'], path+s['poster_path'],
                        "https://www.youtube.com/watch?v=1hPpG4s3-O4")

response = search.movie(query='inception')
s = search.results[0]
inception = media.Movie(s['title'], s['overview'], path+s['poster_path'],
                    "https://www.youtube.com/watch?v=66TuSJo4dZM")

response = search.movie(query='avatar')
s = search.results[0]
avatar = media.Movie(s['title'], s['overview'], path+s['poster_path'],
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

response = search.movie(query='3 idiots')
s = search.results[0]
idiots = media.Movie(s['title'], s['overview'], path+s['poster_path'],
                    "https://www.youtube.com/watch?v=xvszmNXdM4w")

response = search.movie(query='conjuring')
s = search.results[0]
conjuring = media.Movie(s['title'], s['overview'], path+s['poster_path'],
                    "https://www.youtube.com/watch?v=k10ETZ41q5o")

response = search.movie(query='suicide squad')
s = search.results[0]
suicide_squad = media.Movie(s['title'], s['overview'], path+s['poster_path'],
                    "https://www.youtube.com/watch?v=CmRih_VtVAs")

response = search.movie(query='jungle book')
s = search.results[0]
jungle_book = media.Movie(s['title'], s['overview'], path+s['poster_path'],
                    "https://www.youtube.com/watch?v=HcgJRQWxKnw")

#list of all the instances of class Movie
movies = [dark_knight,inception,avengers,avatar,idiots,finding_dory,
          conjuring,suicide_squad,jungle_book]

# open_movies_page() method defined in fresh_tomatoes package takes list of
# instances as argument and render the content on website
fresh_tomatoes.open_movies_page(movies)
