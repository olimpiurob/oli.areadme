# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s oli.areadme -t test_areadme.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src oli.areadme.testing.OLI_AREADME_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_areadme.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a AReadme
  Given a logged-in site administrator
    and an add areadme form
   When I type 'My AReadme' into the title field
    and I submit the form
   Then a areadme with the title 'My AReadme' has been created

Scenario: As a site administrator I can view a AReadme
  Given a logged-in site administrator
    and a areadme 'My AReadme'
   When I go to the areadme view
   Then I can see the areadme title 'My AReadme'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add areadme form
  Go To  ${PLONE_URL}/++add++AReadme

a areadme 'My AReadme'
  Create content  type=AReadme  id=my-areadme  title=My AReadme


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the areadme view
  Go To  ${PLONE_URL}/my-areadme
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a areadme with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the areadme title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
