# Team : eYHC#70
<h1>Title of the Project: E-hospital</h1>
A website to narrow down the gap between service providers and people in need during the covid-19 pandemic.
<h2>Description:</h2>
 During the past few weeks India has witness the most diffcult times out of which we had noted few points and devoloped a possible solution to these issues.<br>
  - Shortage of Beds.<br>
  - Unavailability of oxygen. <br>
  - Delivery of plasma/Blood.<br> 
  - Treatment of non-covid patients. <br>

Basic idea is to connect patients in need to hospitals, oxygen suppliers, blood bank all at one place thereby bringing the smooth connectivity in chain. We came up with a solution consiting of three modules namely Hospital, Blood bank and Supplier, making all these data available at a single access point to the user.

<h3>Home Page:</h3>
The navigation bar enables one to register, login, look for the lastest news on covid-19 from WHO and ICMR, about button redirects to the breif infomation about our site ,which is then followed by a slidebar with qoutes from diffrent people to boost peoples' confidence and to provide lastest updates as well. The icon bar on the left redirects to respective soical media links of the government authority. The main section has three cards, one to show the registeration stats of our website, other to benificary stats, while the center card has a button for the patients,on clicking pops-up a card that takes basic infomation on requirments which then open up a search results page. Footer consits of daily cases reported in the world and India.

<h3>Search Results:</h3>
On the homepage the data of person's requiremnet list along with his address is collected, which is then matched with our database depending on the city our page show the results with all the credentials.<br>


Input         | Types                    | Results 
------------- | ------------------------ | -------------
Ambulance     | ICU,Oxgyen,General,Covid | Driver name,contact detials,loaction 
Patient type  | Covid ,Non-Covid         | hospital
Oxygen        | YES/NO                   | Supplier contact detials,loaction
Blood/Plasma  | YES/NO                   | Supplier contact detials,loaction ,availability list and type 
Address       | main,city                | Results based on loaction 

<h3>Hospital portal </h3>
The hospital module has all the necessary information regarding the availability of Doctors, Beds, Oxygen, Blood and Ambulance services. Each hospital has to initially register with all the details such as name, address, email and other contact details. After registration the hospital can enter the availability of all the supplies in the hospital and can update them regularly. The patient can know information of  beds, and ambulance services that are currently available in the hospital. The hospital dashboard has separate sections for all services. The Doctors section has information about the doctors currently available along with their details. The Rooms section gives details about the number of rooms available with their status. The Oxygen and Blood bank section shows current availability in hospital and also on request due shortage or emergency in hospital, a automated mail would be sent to all vendors. The patient section consists of the details regarding the patient, doctor incharge and status of patient. The last section of dashboard consists of Ambulance services that are currently available in hospital, based on which patients can use them. All the details, statuses are constantly updated based on which it is easy to approach a hospital for treatment.

<h3>Blood Bank</h3>
The Blood Bank module has information regarding the the blood that is available. The Blood Bank also should register similarly to the Hospital. After the registration the details regarding the blood type, quantity available in the Blood Bank are created. The dashboard consists of 2 sections Blood Create and Blood List. Blood create section is used to add a new item to blood list along with its details. The Blood List section displays all the information of blood such as blood group, quantity, status, along with a message. The Blood list can be updated regularly as they vary by using the edit option given at the end of the list. Based on all the information regarding blood available in the Blood Bank, people can contact the required Blood Bank easily with contact details available.

<h3> Oxygen Supplier</h3>
The Oxygen Supplier module has necessary information regarding the the oxygen that is available. The Oxygen Supplier should register with all their details such as name, address and contact details. After the registration the information related to the oxygen is created. The dashboard consists of Create and Invoice sections. The Create section is used to add a new entry of oxygen details to Invoice list. The Invoice section displays all the information related to oxygen like number of cylinders, message, requirement status. The list can be updated as they vary by using the edit option given at the end of the list. Based on information regarding the oxygen available with the Oxygen Supplier, people can contact the required Oxygen Supplier easily with contact details available.

## <h2>Software Requirements:<h2>
  - Python 
  - Django
  - HTML
  - CSS
  - Bootstrap
  - Java script 
  - Sqlite 
  
 ## Thrid party packages
 Install the required Libraries
```
$ pip install -r requirements.txt
```
## <h3>Process Flow Diagram</h3>
At first the homepage is common to all the users ,here it either one can register if not yet done else can login,both the case brings you to the dashborad wherein users will get access to all options mention in above section. If you are a person look for aid ,on click on user portal will lead to a search results page based on your requirments.


## <h3>Data Flow Diagram</h3>
 while the process of registration the data is been collected and store in database ,in the dashboard the data can be updated,edited and deleted. Here if any commodity is critcal in number an auto alert mails is sent to respective supplier. The user serach data is taken and matched with the database after filtering out based on loaction results are displayed. 

# To run the project

python manage.py runserver
