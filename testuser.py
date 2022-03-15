import datetime

from flask_jwt_extended.config import config
from flask_restful import Resource
from flask import Flask
from flask import Response, request
from flask_jwt_extended import create_access_token
from init import api
from models import Records
from init import app




class RegisterApi(Resource):
    def get(self):
        records = Records.objects().to_json()
        return Response(records, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        _records = Records(**body).save()
        id = _records.id
        return {'id': str(id)}, 200


class RegistrationApi(Resource):
    def put(self, id):
        body = request.get_json()
        Records.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        remove_record = Records.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        get_record = Records.objects.get(id=id).to_json()
        return Response(get_record, mimetype="application/json", status=200)


class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        _records = Records(**body)
        _records.hashing()
        _records.save()
        id = _records.id
        return {'id': str(id)}, 200


class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        _details = Records.objects.get(email=body.get('email'))
        authorized = _details.check(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401
        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(id), expires_delta=expires)
        return {'token': access_token}, 200


api.add_resource(RegisterApi, '/get')
api.add_resource(RegistrationApi, '/get/<id>')
api.add_resource(SignupApi, '/sign')
api.add_resource(LoginApi, '/login')

if __name__ == "__main__":
    app.run()
