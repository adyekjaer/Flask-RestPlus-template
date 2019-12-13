from flask import Blueprint
from flask_restplus import Api
from apis.cats import api as cats
from apis.dogs import api as dogs

blueprint = Blueprint('apiv1', __name__, url_prefix='/v1')

api = Api(
    blueprint,
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(cats)
api.add_namespace(dogs)
