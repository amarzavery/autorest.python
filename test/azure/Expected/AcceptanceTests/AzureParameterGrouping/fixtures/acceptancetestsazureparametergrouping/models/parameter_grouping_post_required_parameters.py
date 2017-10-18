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


class ParameterGroupingPostRequiredParameters(Model):
    """Additional parameters for post_required operation.

    :param body:
    :type body: int
    :param custom_header:
    :type custom_header: str
    :param query: Query parameter with default. Default value: 30 .
    :type query: int
    :param path: Path parameter
    :type path: str
    """

    _validation = {
        'body': {'required': True},
        'path': {'required': True},
    }

    def __init__(self, body, path, **kwargs):
        self.body = body
        self.custom_header = kwargs.get('custom_header', None)
        self.query = kwargs.get('query', 30)
        self.path = path
