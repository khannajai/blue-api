from flask_restplus import Namespace, Resource, fields
from db import customers, transactions, accounts

api = Namespace('accounts', description='Accounts related operations')

account = api.model('Account', {
    'account_id': fields.Integer(required=True, description='The account identifier'),
    'balance': fields.Integer(required=True, description='The account balance'),
})

@api.route('/')
class AccountList(Resource):
    @api.doc('list_accounts')
    @api.marshal_list_with(account)
    def get(self):
        '''List all accounts'''
        return accounts


@api.route('/<id>')
@api.param('account_id', 'The account identifier')
@api.response(404, 'Account not found')
class Account(Resource):
    @api.doc('get_account')
    @api.marshal_with(account)
    def get(self, id):
        '''Fetch an account given its identifier'''
        for acc in accounts:
            if acc['account_id'] == int(id):
                return acc
        api.abort(404)