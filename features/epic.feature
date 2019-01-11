Feature: behave to epic

 Scenario: Update the epic
    Given I create a new project
      | name          |
      | First Project |
    And I create a new epic
      | label      |
      | Test epics |
    When I update the epic
      | label             |
      | Test Update epics |
    Then I verify epic updated status is 200
    And I verify epic schema


#  Scenario: Delete the epic
#    Given I create a project
#      | name          |
#      | First Project |
#    And I create a epic
#      | label      |
#      | Test epics |
#    When I delete the epic
#    Then I verify epic updated status is 204