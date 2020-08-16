
from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
app = Flask(__name__)
api = Api(app)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysqlasp123@localhost:3306/platform_python'
db = SQLAlchemy(app)
app.config['JWT_SECRET_KEY'] = 'ceshiren'  # Change this!
jwt = JWTManager(app)





class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username


class CaseTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_title = db.Column(db.String(180), unique=False, nullable=False)
    case_content = db.Column(db.Text, unique=False, nullable=True)
    case_module = db.Column(db.String(120), unique=False, nullable=True)
    case_author = db.Column(db.String(120), unique=False, nullable=False)
    case_result = db.Column(db.Text, unique=False, nullable=True)
    case_project = db.Column(db.String(120), unique=False, nullable=True)
    case_executor = db.Column(db.String(120), unique=False, nullable=True)
    case_priority = db.Column(db.String(120), unique=False, nullable=True)
    case_remarks = db.Column(db.String(120), unique=False, nullable=True)
    case_create_time = db.Column(db.DateTime, unique=False, nullable=True)
    case_update_time = db.Column(db.DateTime, unique=False, nullable=True)
    case_other1 = db.Column(db.String(120), unique=False, nullable=True)
    case_other2 = db.Column(db.String(120), unique=False, nullable=True)
    case_other3 = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<CaseTable %r>' % self.case_title


class Login(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        user = User.query.filter_by(username=current_user).first()
        return {
            'data': {
                'username': user.username,
                'email': user.email
            },
            'errcode': 0
        }

    def post(self):
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).first()
        if user is None:
            return {
                'data': '',
                'errcode': 1
            }
        else:
            access_token = create_access_token(identity=user.username)
            return {
                'data': {
                    'username': user.username,
                    'password': user.password,
                    'token': access_token

                },
                'errcode': 0
            }

    def put(self):
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).update({'password': password})

        if not user:
            return {
                'data': user,
                'errcode': 1
            }
        else:
            db.session.commit()
            return {
                'data': user,
                'errcode': 0
            }


class Project(Resource):
    def get(self):
        pass


class TestCase(Resource):
    @jwt_required
    def get(self):
        case_title=request.form['case_title']
        case = CaseTable.query.filter_by(case_title=case_title).first()
        if case is None:
            return {
                'data': '',
                'errcode': 1
            }
        else:
            return {
                'data': {
                    'case_title': case.case_title,
                    'case_content': case.case_content
                },
                'errcode': 0
            }

    @jwt_required
    def post(self):
        form=request.form
        case = CaseTable(**form)
        db.session.add(case)
        if not case:

            return {
                'data': '',
                'errcode': 1
            }
        else:
            db.session.commit()
            return {
                'data': {
                    'case_title':case.case_title,
                    'case_author':case.case_author,
                    'case_content': case.case_content
                },
                'errcode': 0
            }

    @jwt_required
    def put(self):

        id = request.form['id']
        case_title = request.form['case_title']
        case_content = request.form['case_content']
        casetable = CaseTable.query.filter_by(id=id).update({'case_title': case_title,'case_content':case_content})
        if not casetable:
            return {
                'data': casetable,
                'errcode': 1
            }
        else:
            db.session.commit()
            return {
                'data': casetable,
                'errcode': 0
            }

    @jwt_required
    def delete(self):


        id = request.form['id']
        number = CaseTable.query.filter_by(id=id).delete()
        if not number:
            return {
                'data': number,
                'errcode': 1
            }
        else:
            db.session.commit()
            return {
                'data': number,
                'errcode': 0
            }


api.add_resource(Login, '/login')
api.add_resource(TestCase, '/testcase')

if __name__ == '__main__':
    app.run(debug=True)
