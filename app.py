import init
import api.v1.routes.init
import api.v1_1.routes.init
from api.init import api


if __name__ == '__main__':
    api.run(
        host=api.config['HOST'],
        port=api.config['PORT'],
    )
