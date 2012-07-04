Feature: Create a basic packing list

In order to help my child pack
as a parent
I want to create a basic packing list

@create_list
Scenario: Create list of a single item
Given I navigate to the front page
    And I click on the "Create List" link
Then I am on the "Create List" page
When I enter "Pants" in the empty item field
    And I click the "Add" button
Then I see the text "Your list has been saved"



















#
#
#Scenario: Create list of multiple of the same item
#Given I navigate to the front page
#    And I click on the "Create List" link
#Then I am on the "Create List" page
#When I enter "Pants" in the "New Item" field
#    And I tab to the next field
#    And I enter "2" in the "Quantity" field
#    And I click the "Save" button
#Then