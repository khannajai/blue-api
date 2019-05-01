from flask_restplus import Namespace, Resource, fields
from db import customers, transactions, accounts

api = Namespace('transactions', description='Transactions related operations')

transaction = api.model('Transaction', {
    'transaction_id': fields.Integer(required=True, description='The transaction identifier'),
    'amount': fields.Integer(required=True, description='The transaction amount'),
})

@api.route('/')
class TransactionList(Resource):
    @api.doc('list_transactions')
    @api.marshal_list_with(transaction)
    def get(self):
        '''List all transactions'''
        return transactions


@api.route('/<id>')
@api.param('transaction_id', 'The transaction identifier')
@api.response(404, 'Transaction not found')
class Transaction(Resource):
    @api.doc('get_transaction')
    @api.marshal_with(transaction)
    def get(self, id):
        '''Fetch a transaction given its identifier'''
        for tra in transactions:
            if tra['transaction_id'] == int(id):
                return tra
        api.abort(404)