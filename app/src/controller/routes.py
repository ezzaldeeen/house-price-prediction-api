from flask import Blueprint, jsonify, request
from jsonschema.validators import Draft7Validator
from src.models.predictor import single_predict
import json

controller_blueprint = Blueprint('controller_blueprint',
                                 __name__,
                                 url_prefix='/api/v1')

# load schema
SCHEMA_PATH = "src/schemas/schema.json"
with open(SCHEMA_PATH) as f:
    SCHEMA = json.load(f)

# load data-info file
DATA_INFO_PATH = "src/models/data/dataset_info.json"
with open(DATA_INFO_PATH) as f:
    DATA_INFO = json.load(f)


def get_input_errors(body: dict) -> list:
    """
        check out the input if it's valid or not
        ------
        param: [dict] request's body
        ------
        return: [list] list of error messages
    """

    validator = Draft7Validator(SCHEMA)
    errors = [error.message for error in validator.iter_errors(body)]

    return errors


@controller_blueprint.route('/welcome')
def index():
    return jsonify({
        'message': 'welcome'
    })


@controller_blueprint.route('/single_prediction', methods=['POST'])
def single_prediction():
    """
        single prediction endpoint for new sample,
        check the validation of the the requests' body,
        this endpoint expect a json request,
        and the response would be integer ( prediction value )
    """

    body = request.get_json()
    # check the response if it's validate or not
    errors = get_input_errors(body)
    # if the request's body is invalid then return the errors
    if errors:
        response = jsonify({'success': False,
                            'message': "invalid input",
                            'errors': errors})
        response.status_code = 406
        return response

    # estimate the value of the new sample
    predicted_value = single_predict(body)

    response = jsonify({'success': True,
                        'predict_value': predicted_value})
    response.status_code = 200

    return response
