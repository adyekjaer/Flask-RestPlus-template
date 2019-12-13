from flask_restplus import Namespace, Resource, fields
from modules.data import data

api = Namespace('dogs', description='Dogs related operations')

dog = api.model('Dog', {
    'id': fields.String(required=True, description='The dog identifier'),
    'name': fields.String(required=True, description='The dog name'),
})

d = data.Data()


@api.route('/')
class DogList(Resource):
    @api.doc('list_dog')
    @api.marshal_list_with(dog)
    def get(self):
        '''List all dog'''
        return d.dogs


@api.route('/<id>')
@api.param('id', 'The dog identifier')
@api.response(404, 'Dog not found')
class Dog(Resource):
    @api.doc('get_dog')
    @api.marshal_with(dog)
    def get(self, id):
        '''Fetch a dog given its identifier'''
        for dog in d.dogs:
            if dog['id'] == id:
                return dog
        api.abort(404)
