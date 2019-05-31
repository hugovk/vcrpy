import logging
from .config import VCR

# Set default logging handler to avoid "No handler found" warnings.
from logging import NullHandler


logging.getLogger(__name__).addHandler(NullHandler())


default_vcr = VCR()
use_cassette = default_vcr.use_cassette
