import json
import sys

from app.main import app

json.dump(app.openapi(), sys.stdout, indent=2)
