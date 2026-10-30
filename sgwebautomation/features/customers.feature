@Execute
Feature: Verify the Create Customer and Delete Customer functionality 
    Scenario: Verify Create Customer and Delete Customer
        When I Launch browser and navigate URL
        Then I find the login page
        When I enter username in username text field
        When I enter password in password text field
        When I click on signin button
        Then I find the Home page
        When I click on customers menu
        Then I find list customers page
        When I click on add customer button
        Then I find add customer form
        When I enter customername in customername text field
        When I enter emailid in emailid text field
        When I enter location in location text field
        When I enter description in description text field
        When I clcik on save button to create a customer
        Then I find newly created customer in list customers page
        When I click on delete button on newly created customer to delete customer
        Then I find that newly created customer is not available
        When I click on logout link
        Then I find the login page