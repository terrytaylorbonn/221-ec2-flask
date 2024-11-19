#import datetime
import uuid
from flask import Flask
#from flask_swagger_ui import get_swaggerui_blueprint
from flask_smorest import Api, Blueprint
from flask.views import MethodView
from datetime import datetime, timezone

app = Flask(__name__)

class APIConfig:
    API_TITLE = "TODO_API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/docs"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_URL = "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
app.config.from_object(APIConfig)
api = Api(app)
todo = Blueprint("todo", "todo", url_prefix="/todo", description="TODO API")
tasks = [
    {
        "id": uuid.UUID("79f77ea7-4a0b-419e-a96a-bcea465605d0"),
        "created_at": datetime.now(timezone.utc),
        "completed": False,
        "task": "Create Flask API tutorial",
    },
]
@todo.route("/tasks")
class TodoCollection(MethodView):
    #@todo.arguments()
    @todo.response(status_code=200)
    def get(self, parameters):
        pass

    @todo.response(status_code=201)
    def post(self):
        pass


api.register_blueprint(todo)

@app.route('/')
def hello_world2():
    return "Hello, Flask! tt 24.1119 1236pm #3"

if __name__ == '__main__':
    app.run(debug=True)


# SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
# #API_URL = 'https://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)
# API_URL = '/static/petstore_swagger.json'  # Our API url (can of course be a local resource)

# # Call factory function to create our blueprint
# swaggerui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
#     API_URL,
#     config={  # Swagger UI config overrides
#         'app_name': "Test application"
#     },
#     # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
#     #    'clientId': "your-client-id",
#     #    'clientSecret': "your-client-secret-if-required",
#     #    'realm': "your-realms",
#     #    'appName': "your-app-name",
#     #    'scopeSeparator': " ",
#     #    'additionalQueryStringParams': {'test': "hello"}
#     # }
# )
