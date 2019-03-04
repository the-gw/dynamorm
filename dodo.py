# -*- coding: utf-8 -*-
# pylint: disable=W0614
from gwio.devtools.doit.tasks import *  # noqa: F403,F401
from gwio.devtools.doit.helpers import publisher


task_publish = publisher('gwio-dynamorm')
