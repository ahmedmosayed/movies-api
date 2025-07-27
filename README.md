
Clone the Repository:

git clone https://github.com/ahmedmosayed/movies-api.git
cd movies-api
2-
Install the Dependencies:
pip install -r requirements.txt
3-Run the Application:
uvicorn main:app --reload
4-
Access the API Docs:
http://127.0.0.1:8000

5- API Reference
/api/movies
Get a list of all movies
/api/movies/search?title={title}
Search for movies by title

Example
/api/movies/search?title=matrix

http://localhost:8000/api/movies/search?title=matrix

http://localhost:8000/api/movies/search?title=inception

http://localhost:8000/api/movies/search?title=inception&genre=Action

http://localhost:8000/api/movies/search?title=inception&genre=Action&actor=DiCaprio


6-Summary of Design Decisions
The design of the API follows the principles of RESTful API design. The API has a single endpoint
/api/movies which returns a list of all movies. The search functionality is implemented using a query
parameter. This design decision was made to keep the API simple and easy to use.

7-Known Limitations & Possible Improvements
The current implementation of the API does not handle errors well. It would be beneficial to add error
handling to make the API more robust.
The API does not have any authentication or authorization. This could be improved by adding authentication
and authorization mechanisms.
The API does not have any caching. This could be improved by adding caching mechanisms to improve
performance.



