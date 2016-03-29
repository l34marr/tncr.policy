# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import tncr.policy


class TncrPolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=tncr.policy)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'tncr.policy:default')


TNCR_POLICY_FIXTURE = TncrPolicyLayer()


TNCR_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TNCR_POLICY_FIXTURE,),
    name='TncrPolicyLayer:IntegrationTesting'
)


TNCR_POLICY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TNCR_POLICY_FIXTURE,),
    name='TncrPolicyLayer:FunctionalTesting'
)


TNCR_POLICY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TNCR_POLICY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='TncrPolicyLayer:AcceptanceTesting'
)
