# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DictionaryWrapper(Model):
    """DictionaryWrapper.

    :param default_program:
    :type default_program: dict[str, str]
    """

    _attribute_map = {
        'default_program': {'key': 'defaultProgram', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        self.default_program = kwargs.get('default_program', None)
