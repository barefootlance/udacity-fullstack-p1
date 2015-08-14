# udacity-fullstack-p1
Udacity fullstack project #1: Movie Trailer Website

This is an implementation of the specification for the Movie Trailer Website, the first project of the Udacity Full Stack Web Developer Nanodegree. Aside from the basic functionality, this implementation adds a plot summary, a list of the primary actors, and the Kevin Bacon Number (kbn) for each of the actors.

The plot summary and list of actors are retrieved by using the [requests library](http://www.python-requests.org/en/latest/) to access the REST API exposed by [OMDb API](omdbapi.com).

The kbn is determined by using the requests library to submit a form on the [Oracle of Bacon](https://oracleofbacon.org) website.

## Running the project

* Clone the repo: `git clone https://github.com/barefootlance/udacity-fullstack-p1.git`.
* Install Python 2.7 (it may work on 2.6, but has not been tested with it - and 3.x is right out!)
* Install the requests libarary: `pip install requests`.
* From the project directory run `python entertainment_center.py`

Running the project will create a webpage (fresh_tomatoes.html), and launch that page in your default browser.

## Modifying the list of movies

The list of movies is hardcoded in the titles list in the entertainment_center.py file. Each element in the list is a 2-tuple, where the first member is the name of the movie, and the second is a link to the movie trailer on youtube (yes, it must be on youtube).

## Known issues

* Cannot get the Kevin Bacon Number for actors with non-ascii characters in their names. It's not clear if this would be cleared up by moving to Python 3.x (which is native unicode) or if there are other round-tripping issues. An example of this is for Stellan Skarsgård in Ronin.
* Displaying 3 or 4 movies on a row results in empty spaces in the grid. Unsightly and annoying, but does not seem to be an issue when only two are shown.
* The name of the movie is not always sufficient to return the movie information you expect. Should take advantage of the year parameter in the OMDb API, at the very least.
