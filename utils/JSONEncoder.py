#!/usr/bin/python3

import numpy as np
import simplejson as json
from bson import ObjectId
from decimal import Decimal
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class JSONEncoder(json.JSONEncoder):
    """Custom JSON encoder to handle special data types."""

    def default(self, o):
        """Override default method to handle custom types."""
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, Decimal):
            return float(o)
        if isinstance(o, (np.float32, np.float64)):
            return float(o)  # Convert all numpy floats to Python float
        if isinstance(o, np.int64):
            return int(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, set):
            return list(o)  # Convert sets to lists
        if isinstance(o, bytes):
            return o.decode('utf-8')  # Decode bytes to string

        logger.warning(f'Unhandled type: {type(o)} - {o}')
        return super().default(o)  # Call the superclass method for other types
