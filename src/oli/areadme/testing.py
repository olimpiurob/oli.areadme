# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import oli.areadme


class OliAreadmeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=oli.areadme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'oli.areadme:default')


OLI_AREADME_FIXTURE = OliAreadmeLayer()


OLI_AREADME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(OLI_AREADME_FIXTURE,),
    name='OliAreadmeLayer:IntegrationTesting'
)


OLI_AREADME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(OLI_AREADME_FIXTURE,),
    name='OliAreadmeLayer:FunctionalTesting'
)


OLI_AREADME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        OLI_AREADME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='OliAreadmeLayer:AcceptanceTesting'
)
