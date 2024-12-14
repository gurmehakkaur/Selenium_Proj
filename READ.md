# Overview
After learning Selenium, I wanted to get some hands on practice and then Seneca's Study room Booking Website caught my eye, as I am a frequent user. As the booking has certain rules, I wanted to test if all those rules are validated before completing a booking, and Selenium had already taught me how to automate the web testing. This selenium script replicates real user interaction, tries to book study room as per given details and then returns if the booking was successful or not, which in turn determines whether the test case passed or failed.

## A screenshot taken during Runtime
### Full runtime video is also available in this repository as ExecutionVideo.mp4
![image](https://github.com/user-attachments/assets/fcca9070-1bbf-401f-8d63-bc69c9eae1d6)

## Test Descriptions
![image](https://github.com/user-attachments/assets/f057aae8-5922-4505-b030-1f1dcff78222)

## Traceability Matrix
![image](https://github.com/user-attachments/assets/24f5790f-6637-438c-9318-4fed7cd2ea86)

## Impact
The two bugs which led to uncontrolled booking:
### 1.special characters in names and invalid college email addresses

## Steps to get started
**Clone the repository:
git clone https://github.com/gurmehakkaur/Selenium_Proj
cd study-room-booking

**Install Dependencies:
pip install selenium

**Run the Tests:
python lib.py
