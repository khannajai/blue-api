from flask_restplus import Api

from .customers import api as customers_api
from .accounts import api as accounts_api
from .transactions import api as transactions_api

api = Api(
    title='Blue Harvest Accounts API',
    version='1.0',
    description='A simple API for opening new accounts',
)

api.add_namespace(customers_api)
api.add_namespace(accounts_api)
api.add_namespace(transactions_api)