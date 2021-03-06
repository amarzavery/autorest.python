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
from msrest.exceptions import HttpOperationError


class Error(Model):
    """Error.

    :param status:
    :type status: int
    :param message:
    :type message: str
    :param parent_error:
    :type parent_error: ~fixtures.acceptancetestsmodelflattening.models.Error
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'parent_error': {'key': 'parentError', 'type': 'Error'},
    }

    def __init__(self, status=None, message=None, parent_error=None):
        self.status = status
        self.message = message
        self.parent_error = parent_error


class ErrorException(HttpOperationError):
    """Server responsed with exception of type: 'Error'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorException, self).__init__(deserialize, response, 'Error', *args)
