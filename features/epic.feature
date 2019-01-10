Feature: showing off behave

#Scenario:Create new project
#    Given I create a project
#        | name | First Project|
#    Then I verify project creation status is 200
#    And I verify project schema



  Scenario: Update the epic
    Given I create a project
      | name          |
      | First Project |
    And I create a epic
      | label      |
      | Test epics |
    When I update a epic
      | label             |
      | Test Update epics |
    Then I verify epic updated status is 200
    And I verify epic schema


  Scenario: Delete the epic
    Given I create a project
      | name          |
      | First Project |
    And I create a epic
      | label      |
      | Test epics |
    When I delete the epic
Then I verify epic updated status is 204