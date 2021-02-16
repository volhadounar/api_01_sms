SMS notifications 
=================================

The app 'SMS notifications' uses service Twilio and sends sms from number NUMBER_FROM (visit https://www.twilio.com/console/) to verified number NUMBER_TO (https://twilio.com/user/account/phone-numbers/verified) if the user from vk.com is online, otherwise app waits for 5 sec and then check the online status again to send the message.
You have to be registed on https://www.twilio.com and on https://vk.com to run the app.

There was used OAuth(Open Authorization) - an authorization scheme that provides limited access to another user or app to service resources without the need to transfer a username and password.

Getting Started
===============

1.  You can build it in steps:
    1.  ``cd ...wherever...``
    2.  ``git clone https://github.com/volhadounar/api_01_sms.git``
    3.  ``cd api_01_sms``
    4.  ``touch .env`` -- Creates file to keep secret data.
    
        File .env should contain: 
            1. account_sid=     -- copy value from field ACCOUNT SID on page https://www.twilio.com/console/
            2. auth_token=      -- copy value from AUTH TOKEN on page https://www.twilio.com/console/
            3. vk_access_token= -- copy the value from https://oauth.vk.com/authorize?client_id=XXXXXX&scope=friends&response_type=token&v=5.92
            4. NUMBER_FROM=     -- copy from PHONE NUMBER on page https://www.twilio.com/console/
            5. NUMBER_TO=       -- copy from https://twilio.com/user/account/phone-numbers/verified.

        Register on https://vk.com/. Open https://vk.com/dev and create your own Standalone-app.
        Get client_id. Input in your browser this url to fetch token:
        https://oauth.vk.com/authorize?client_id=XXXXXX&scope=friends&response_type=token&v=5.92.
        Put in the variable vk_access_token with the token value.
    5.  ``pip install -r requirements.txt``  -- Should install everything you need.
    6.  ``python3 homework`` -- Running localy then enter the vk.com user id to check if he\she is online.

