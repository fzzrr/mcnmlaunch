#!/usr/bin/env python
# -*- coding: utf-8 -*-

" Production settings must be here. "
import logging
from mcnmlaunch.config import ROOTDIR
from os import path as op, environ

SECRET_KEY = 'srU7190rKKiQa8+ZL5sVTEcNAPiSmpv3'

logging.info("Production settings loaded.")
