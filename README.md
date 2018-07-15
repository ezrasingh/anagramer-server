# Anagramer Server

A GraphQL server that returns the anagrams of a queried word.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To easily run the application with all dependencies and services you will need [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/v17.09/compose/install/).

### Configuration

Build and run the docker container:

```
docker-compose up --build
```
 
For subsequent runs just use:

```
docker-compose up
```

## Developing

For development you will need [Python 3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) (if you run into issues with pip try *pip3*). I suggest also developing from within a virtualenv (checkout [Virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/)). For more info on setting up this environment reference [IamAdiSri's Gist](https://gist.github.com/IamAdiSri/a379c36b70044725a85a1216e7ee9a46). You will also need to install or deploy [Redis](https://redis.io/topics/quickstart).

## Testing

For local [GraphiQL](https://github.com/graphql/graphiql) testing goto: [http://localhost:5000/graphql](http://localhost:5000/graphql).

An example query:

```graphql

query getAnagrams{
    anagrams(word: "aamrl")
}

```

## Built With

* [Flask](http://flask.pocoo.org/) - Microframework for Python based on Werkzeug, Jinja 2 and good intentions.
* [Graphene](http://graphene-python.org/) - Library for building GraphQL APIs in Python easily.
* [Redis](https://redis.io/) - In-memory data structure store, used as a database, cache and message broke 

