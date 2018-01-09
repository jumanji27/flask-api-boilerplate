import init
import api.v1.routes.init
import api.v1_1.routes.init
from api.init import api as app


if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
    )
