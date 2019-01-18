# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from mcrouter.test.McrouterTestCase import McrouterTestCase

class TestEmptyPool(McrouterTestCase):
    config = './mcrouter/test/test_empty_pool.json'
    extra_args = []

    def get_mcrouter(self, extra_args=[]):
        return self.add_mcrouter(self.config, extra_args=self.extra_args)

    def test_empty_pool(self):
        # Start a mcrouter without route handles
        key = 'foo'
        mcrouter_w_rh = self.get_mcrouter()
        self.assertIsNone(mcrouter_w_rh.get(key))
