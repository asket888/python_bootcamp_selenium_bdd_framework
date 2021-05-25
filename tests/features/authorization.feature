@authorization
Feature: Authorization
  As a user I should be able to authorize in application

  @authorization_1
  Scenario: Login with correct data
    When I click [Login] button on the header of the page
     And I login to application on Login page
    Then nickname is presented on the header of the page
    When I click [Logout] button on the header of the page
    Then nickname is not presented on the header of the page

  @authorization_2
  Scenario: Login with correct data 2
    When I click [Login] button on the header of the page
     And I login to application on Login page
    Then nickname is presented on the header of the page
    When I click [Logout] button on the header of the page
    Then nickname is not presented on the header of the page
