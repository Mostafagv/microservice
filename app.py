# The app.py is what will wire all our other bits together and host it on some url. It is what configures Connexion,
# RestyResolver, Injector and runs it all.
import os
import connexion
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver
from providers.CouchProvider import CouchProvider

from injector import Binder


def configure(binder: Binder) -> Binder:
    binder.bind(
        CouchProvider
    )


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')  # Provide the app and the directory of the docs
    app.add_api('couch-service-docs.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
    app.run(port=int(os.environ.get('PORT', 2020)), debug=True)  # os.environ is handy if you intend to launch on heroku


# http://localhost:2020/v1.0/products/getproduct