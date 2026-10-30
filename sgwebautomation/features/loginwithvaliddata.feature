Feature: Verify the Login functionality with valid credentials
    Scenario: login with valid test data
        When I Launch browser and navigate URL
        Then I find the login page
        When I enter username in username text field
        When I enter password in password text field
        When I click on signin button
        Then I find the Home page