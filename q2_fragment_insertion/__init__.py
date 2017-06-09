# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import pkg_resources

from ._insertion import sepp_16s_greengenes


__version__ = pkg_resources.get_distribution('q2-fragment-insertion').version
__all__ = ['sepp_16s_greengenes']