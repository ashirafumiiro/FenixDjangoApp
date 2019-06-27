# Accrual System for employees
This application is developed using django framework version 2.2.2

## How it works

* Run Script add_cron_job to enable monthly update in cron table (done for linux). This is enabled using codeigniter CLI
* Users browse to directory and controller welcom (default) implements the logic
* For monthly update, CLI_Update controller is used and users can't access URL and a check is made to ensure CLI is used to access the controller


### Note:
* A user is able to see the points info (used accrued and balance) when logged in.
* dbcommands.tx ensures the appropriate user privileges for data access

## Sample
![alt text](djangoview.png)