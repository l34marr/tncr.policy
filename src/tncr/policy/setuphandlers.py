# -*- coding: utf-8 -*-


def post_install(context):
    """Post Install Script"""
    if context.readDataFile('tncrpolicy_default.txt') is None:
        return
    # Do something during the installation of this package

