import datetime as dt

from marshmallow import Schema, fields


class Transaction:
    def __init__(self, description, amount, type_transaction):
        self.description = description
        self.amount = amount
        self.created_at = dt.datetime.now()
        self.type = type_transaction

    def __repr__(self):
        return '<Transaction(name={self.description!r})>'.format(self=self)


class TransactionSchema(Schema):
    description = fields.Str()
    amount = fields.Number()
    created_at = fields.Date()
    type = fields.Str()
