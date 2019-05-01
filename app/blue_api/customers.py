from flask_restplus import Namespace, Resource, fields
from db import customers, transactions, accounts

api = Namespace('customers', description='Customers related operations')

customer = api.model('Customer', {
    'customer_id': fields.Integer(required=True, description='The customer identifier'),
    'first_name': fields.String(required=True, description='The customer first name'),
    'last_name': fields.String(required=True, description='The customer last name'),
    'accounts': fields.List(fields.Integer, required=True, description='The customer account list'),
    'balance': fields.List(fields.Integer, required=True, description='The balance for each customer')
})

new_account = api.model('New Account', {
    'customer_id': fields.Integer(required=True, description='The customer identifier'),
    'initial_balance': fields.Integer(required=True, description='Initial balance of new account'),
})

parser = api.parser()
parser.add_argument('initial_balance', type=int, required=True, help='The initial balance of new acount', location='form')

@api.route('/')
class CustomerList(Resource):
    @api.doc('list_customers')
    @api.marshal_list_with(customer)
    def get(self):
        '''List all customers'''
        return customers


@api.route('/<id>')
@api.response(404, 'Customer not found')
class Customer(Resource):

    @api.doc('get_customer')
    def get(self, id):
        '''Fetch a customer given its identifier'''
        for cus in customers:
            if cus['customer_id'] == int(id):
                user_accounts = []
                user_transactions = []
                for account in accounts:
                    if(account['customer_id']==int(id)):
                        user_accounts.append(account)
                        for transaction in transactions:
                            if(transaction['account_id']==account['account_id']):
                                user_transactions.append(transaction)
                return [cus, {'accounts': user_accounts}, {'transactions': user_transactions}]
        api.abort(404)

    @api.doc(parser=parser)
    def put(self, id):
        '''Create a new account given the user id and initial balance'''
        args = parser.parse_args()
        new_account_id = (len(accounts) + 1)

        
        for cus in customers:
            # add new account to customer's account list
            if cus['customer_id'] == int(id):

                # Create a new account
                accounts.append({
                'account_id': new_account_id,
                'balance': int(args['initial_balance']),
                'customer_id': int(id)})

                # Create a new transaction
                if(int(args['initial_balance']) > 0):
                    new_transaction_id = (len(transactions) + 1)
                    transactions.append({
                    'transaction_id': new_account_id,
                     'account_id': new_account_id,
                    'amount': int(args['initial_balance'])})
                return self.get(id)
        api.abort(404)

