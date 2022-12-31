#!/usr/bin/env python
"""
Copyright 2022 Vadim Khitrin <me@vkhitrin.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import subprocess
from collections import namedtuple
from subprocess import Popen

from jiav import logger
from jiav.api.backends import BaseBackend
from jiav.api.schemas.command import schema

MOCK_STEP = {"cmd": "[true]", "rc": 0}

# Subscribe to logger
jiav_logger = logger.subscribe_to_logger()


class CommandBackend(BaseBackend):
    """
    Shell backend object

    Executes shell command

    Attributes:
        name - Backend name

        schema - json_schema to be used to verify that the supplied step
        is valid according to the backends's requirements

        step - Backend excution instructions
    """

    def __init__(self):
        self.name = "command"
        self.schema = schema
        self.step = MOCK_STEP
        super().__init__(self.name, self.schema, self.step)

    # Overrdie method of BaseBackend
    def execute_backend(self):
        """
        Execute shell command

        Returns a namedtuple describing the jiav manifest execution
        """
        # Parse required arugments
        cmd = [str(_cmd) for _cmd in self.step["cmd"]]
        rc = self.step["rc"]
        # Create a namedtuple to hold the execution result output and errors
        result = namedtuple("result", ["successful", "output", "errors"])
        jiav_logger.debug(f"Command: {cmd}")
        # Execute command
        shell_run = Popen(
            args=cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,
            universal_newlines=True,
        )
        output, errors = shell_run.communicate()
        shell_rc = shell_run.returncode
        jiav_logger.debug(f"Output: {output.strip()}")
        jiav_logger.debug(f"Return code: {shell_rc}")
        jiav_logger.debug(f"Expected return code: {rc}")
        # If executed return code equals desired return code
        if rc == shell_rc:
            successful = True
            jiav_logger.debug(
                "Command executed successfully with the expected return code"
            )
        else:
            successful = False
            jiav_logger.error("Command failed to execute with the expected return code")
            if errors:
                jiav_logger.error("Error: {}".format(errors))
        self.result = result(successful, output, errors)
