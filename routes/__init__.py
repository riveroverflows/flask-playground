from flask import Blueprint

from .file1 import *
from .file2 import *
from .file3 import *

blueprint = Blueprint("routes", __name__)
