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


class DatabaseTable(Model):
    """Table properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar has_rows: Indicates whether table is empty or not
    :vartype has_rows: bool
    :ivar name: Schema-qualified name of the table
    :vartype name: str
    """

    _validation = {
        'has_rows': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'has_rows': {'key': 'hasRows', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self):
        super(DatabaseTable, self).__init__()
        self.has_rows = None
        self.name = None