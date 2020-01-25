# the function which calls the swagger spec
from flask_injector import inject
from providers.CouchProvider import CouchProvider


@inject(data_provider=CouchProvider)
def read_product(data_provider) -> str:
    return data_provider.read_product()
# @inject
# def read_product(CouchProvider) -> str:
#     return data_provider.read_product()