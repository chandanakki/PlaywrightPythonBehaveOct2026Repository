Feature: Verify the Login functionality with invalid credentials
    Scenario: login with invalid test data
        When I Launch browser and navigate URL
        Then I find the login page
        When I enter invalid username in username text field
        When I enter invalid password in password text field
        When I click on signin button
        Then I find the error message Invalid username or password