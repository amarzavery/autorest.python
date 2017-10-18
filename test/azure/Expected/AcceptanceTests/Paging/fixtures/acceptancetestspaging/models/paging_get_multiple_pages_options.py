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


class PagingGetMultiplePagesOptions(Model):
    """Additional parameters for get_multiple_pages operation.

    :param maxresults: Sets the maximum number of items to return in the
     response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing
     the request, in seconds. The default is 30 seconds. Default value: 30 .
    :type timeout: int
    """

    def __init__(self, **kwargs):
        self.maxresults = kwargs.get('maxresults', None)
        self.timeout = kwargs.get('timeout', 30)
