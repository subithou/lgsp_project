# lgsp_project (Python Django - Genesys Cloud CX)

Idea
----
Grouping emails based on PNR (Passenger Name Record) and Priority routing of valued customers like Airline, Travel Agency.
Requirements
------------
  1.	Genesys CX 2 digital License 
  2.	Webhost to host the web-application
  
Solution & Skills used
----------------------
We developed our solution on Genesys Cloud platform and custom web application.
•	Genesys Cloud Platform
  1. Architect 
    * To create inbound email flow and priority routing 
    * Fetching the customer details along with priority from the data table.
    * Based on priority the emails will be sent to LGSP agent.
    * Extracting the PNR from the subject or body of an email and store it in data table.

  2. Script 
    * The agent can be able to see the extracted PNR and customer email along with priority details.
    * Also, agents can go to the web application by clicking button on script for updating the PNR number if its required, change the customer priority and see the previous      emails regarding with PNR number.

  3. Genesys APIs
    * Data table API – To fetch, update and insert the values in data table.
    * Conversation API – To fetch all the emails.

Coding Languages
----------------
1. Python Django – Used as backend of the web application. Used Genesys Data table API and conversation API to insert and update the priority and sort the emails based on    the respective PNR.
2. HTML, CSS, JS and bootstrap – Used as a frontend to provide the UI to agent for update the PNR, priority and see all emails based on the PNR.

Solution flow
-------------
1. The inbound email is routed to an agent as per the flow configuration and priority.
2. Once the agent picks up the interaction the web-application link which is tagged in the script is displayed to the agent along with current conversation details. 
3. The agent can then view all the emails tagged with that PNR. 
4. Agents can update or modify the PNR if the extracted PNR is wrong, and priority of a customer using our web application.




