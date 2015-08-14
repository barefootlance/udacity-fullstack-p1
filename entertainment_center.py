def main():
    from media import Movie
    from fresh_tomatoes import open_movies_page

    # titles is the list of movie titles and associated youtube trailer links
    # as a tuple.
    # NOTE: the trailer link may be an empty string, but cannot be None.
    # NOTE: the youtube v2 API supported searching for move trailers, however
    # that has been deprecated, so it looks like we have to hardcode
    # trailer links rather than getting them dynamically
    titles = [
        ('Casablanca', "https://www.youtube.com/watch?v=EJvlGh_FgcI&spfreload=10"),
        ('Citizen Kane', "https://www.youtube.com/watch?v=8dxh3lwdOFw"),
        ('Frozen', "https://www.youtube.com/watch?v=R-cdIvgBCWY"),
        ('Twister', "https://www.youtube.com/watch?v=HCIK_AN8Zn4"),
        ('Tremors', "https://www.youtube.com/watch?v=liJfZvXdiTE"),
        ('Wings', "https://www.youtube.com/watch?v=p3G5IXn0K7A"),
        ('Ronin', "https://www.youtube.com/watch?v=EkJq5RPu-EY"),
        ('Wonder Boys', "https://www.youtube.com/watch?v=PAOFeG9hKoA"),
        ('Eternal Sunshine of the Spotless Mind', "https://www.youtube.com/watch?v=quuMv7cGUn0")
        ]

    movies = { Movie(get_movie_info(title[0]), title[1]) for title in titles }
    open_movies_page(movies)

def get_movie_info(title):

    # use requests to process http
    # from: http://docs.python-requests.org/en/latest/
    import requests, json

    # get the movie information from omdbapi.com
    omdbapi_url = "http://www.omdbapi.com/"
    payload = {'t':title, 'plot':'short', 'r':'json', 'type':'movie'}
    r = requests.post(omdbapi_url, params=payload)
    return r.json()

if __name__ == '__main__':
   main()
