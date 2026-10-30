@Execute
Feature: Verify the Login and Logout functionality with valid credentials using parameters
    Scenario Outline: login and logout with valid test data using parameters
        When I Launch browser and navigate URL
        Then I find the login page
        When I enter <username> in username text field
        When I enter <password> in password text field
        When I click on signin button
        Then I find the Home page
        When I click on logout link
        Then I find the login page
    Examples:
        |username|password|
        |pgudi|pgudi|
        |geeta|geeta|