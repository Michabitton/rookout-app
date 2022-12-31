
Python Containerized Flask Application Example

This application is an example application for the Rookout Python Agent tutorial.

Run it in a few simple steps:

    Build the container using Docker - docker build . -t rookout-python.
    Run the built container using docker run -it --name rookout -e ROOKOUT_TOKEN=<ROOKOUT_API_KEY> -p 8000:8000 -e ROOKOUT_COMMIT=<Branch> rookout-python
    Check out your brand new web app at http://localhost:8000.

