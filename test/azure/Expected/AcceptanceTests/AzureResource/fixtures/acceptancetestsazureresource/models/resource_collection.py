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


class ResourceCollection(Model):
    """ResourceCollection.

    :param productresource:
    :type productresource:
     ~fixtures.acceptancetestsazureresource.models.FlattenedProduct
    :param arrayofresources:
    :type arrayofresources:
     list[~fixtures.acceptancetestsazureresource.models.FlattenedProduct]
    :param dictionaryofresources:
    :type dictionaryofresources: dict[str,
     ~fixtures.acceptancetestsazureresource.models.FlattenedProduct]
    """

    _attribute_map = {
        'productresource': {'key': 'productresource', 'type': 'FlattenedProduct'},
        'arrayofresources': {'key': 'arrayofresources', 'type': '[FlattenedProduct]'},
        'dictionaryofresources': {'key': 'dictionaryofresources', 'type': '{FlattenedProduct}'},
    }

    def __init__(self, **kwargs):
        self.productresource = kwargs.get('productresource', None)
        self.arrayofresources = kwargs.get('arrayofresources', None)
        self.dictionaryofresources = kwargs.get('dictionaryofresources', None)
