from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
import time

def room_booking(first_name, last_name, email):
    driver = webdriver.Chrome()
    driver.get('https://seneca.libcal.com/reserve/markhamstudyrooms')

    try:
        # Wait for available room elements to load
        available_slot = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "s-lc-eq-period-available"))
        )

        # Scroll to the available slot
        driver.execute_script("arguments[0].scrollIntoView(true);", available_slot)

        # Ensure the slot is clickable
        available_slot = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "s-lc-eq-period-available"))
        )

        # Click the available slot
        available_slot.click()


        # Wait for the Continue button to appear and become clickable, then click it
        continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "submit_times"))
        )
        continue_button.click()

        # Wait for the "I Agree" button to appear, scroll, and click it
        agree_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "terms_accept"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", agree_button)
        agree_button.click()

        # Enter first name
        first_name_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "fname"))
        )
        first_name_field.send_keys(first_name)

        # Enter last name
        last_name_field = driver.find_element(By.ID, "lname")
        last_name_field.send_keys(last_name)

        # Enter email
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys(email)

        # Click on "Submit my Booking"
        submit_button = driver.find_element(By.ID, "btn-form-submit")
        submit_button.click()

        # Wait for the confirmation page and check if 'Booking Confirmed' appears
        confirmation = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.s-lc-eq-success-title"))
        )

        if "Booking Confirmed" in confirmation.text:
            print("Booking Confirmed")
            return True  # Booking was successful

    except (TimeoutException, ElementNotInteractableException):
        print("Room already booked or some other issue.")
        return False  # Booking failed

    finally:
        driver.quit()


# Test Cases

def test_case_1():
    # General case to book available room
    result = room_booking("Gurmehak", "Kaur", "gkuppal4@myseneca.ca")
    print("Test Case 1: ", "Pass" if result else "Fail")

def test_case_2():
    #using non-existent email
    result = room_booking("First", "Student", "notexistant@myseneca.ca")
    print("Test Case 2: ", "Pass" if not result else "Fail")

def test_case_3():
    # Trying to book more than 2 hours for one student (against rules)
    room_booking("Gurmehak", "Kaur", "gkuppal4@myseneca.ca")
    room_booking("Gurmehak", "Kaur", "gkuppal4@myseneca.ca")
    result = ("Gurmehak", "Kaur", "gkuppal4@myseneca.ca")
    print("Test Case 3: ", "Pass" if not result else "Fail")

def test_case_4():
    #trying to book with a non-seneca email
    result = room_booking("Second", "Student", "student04@gmail.com")
    print("Test Case 4: ", "Pass" if not result else "Fail")

def test_case_5():
    #trying to use special characters in first and last name
    result = room_booking("Inv@l!d", "n@m#", "student05@myseneca.ca")
    print("Test Case 5: ", "Pass" if not result else "Fail")



# Call test cases
print("\n ***********Test Case-1********** \n")
test_case_1()
print("\n ***********Test Case-2********** \n")
test_case_2()
print("\n ***********Test Case-3********** \n")
test_case_3()
print("\n ***********Test Case-4********** \n")
test_case_4()
print("\n ***********Test Case-5********** \n")
test_case_5()




