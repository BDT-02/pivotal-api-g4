# Created by verofesa at 1/7/2019
#Feature: Create new account
#  Given I create an account
#      | name | First Project|
#  Scenario: I verify account creation status is 200
#    And I verify account schema

Feature: Get new account
  Scenario: Get account
    Given I get accounts
    #Then I verify the get status is 200
    #And I verify account schema


   Scenario: Details of existent account
    Given I selected account_01 from the list
    When I requested its details
    Then verify the get status is 200
    And verify account schema



