#!/usr/bin/python3
from flask import Flask
from flask_graphql import GraphQLView
from anagramer import api

# Initialize Flask app
app = Flask(__name__)

# Add GraphQL endpoint
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=api.schema,
        graphiql=True
    )
)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
