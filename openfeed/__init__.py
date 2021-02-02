
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent)) 

# https://github.com/protocolbuffers/protobuf/issues/1491#issuecomment-547504972
# FIXME

from .openfeed_client import OpenfeedClient

VERSION = '1.1.5'
