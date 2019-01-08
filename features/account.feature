# Created by verofesa at 1/7/2019
Feature: Create new account
  Given I create an account
      | name | First Project|
  Scenario: I verify account creation status is 200
    And I verify account schema