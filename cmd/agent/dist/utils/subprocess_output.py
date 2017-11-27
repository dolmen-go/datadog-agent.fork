# Unless explicitly stated otherwise all files in this repository are licensed
# under the Apache License Version 2.0.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2017 Datadog, Inc.

# (C) Datadog, Inc. 2010-2017
# All rights reserved

from _util import get_subprocess_output as subprocess_output
from _util import SubprocessOutputEmptyError  # noqa

def get_subprocess_output(command, log, raise_on_empty_output=True):
    """
    Run the given subprocess command and return its output. Raise an Exception
    if an error occurs.
    """

    cmd_args = []
    if isinstance(command, basestring):
        for arg in command.split():
            _args.append(arg)
    elif hasattr(type(command), '__iter__'):
        for arg in command:
            cmd_args.append(arg)
    else:
        raise TypeError("command must be a sequence or string")

    return subprocess_output(cmd_args, raise_on_empty_output)
