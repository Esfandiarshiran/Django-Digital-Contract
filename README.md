# Django-Digital-Contract <br />
## DocuSign for Django(JWT Authentication method) <br />

This package was developed to utilize "e-contract/signatures" directly within a Django web application. To be exact, I am demonstrating DocuSign <br /> integration with Django for embedded signing.<br />
 
## Project status

Django-DocuSign is under development. The project is not mature yet, but users can already use it as well as Django developers are able to develop this web application. It means that APIs and implementations may change (improve!), but the app works well right now. <br />
I invite smart programmers to add more features to the app. So, help is welcome! Feel free to report issues, request features, or refactor them.<br />
 
## Next version<br />
I suggest software developers add features like adding PDF and DOC as documents to sign. It would be so easy, and there are samples in the Docusign documentation. (There are no differences in the process).<br />
 
## Features<br />
-As you see, the app has been designed in modular with MVT architecture, which means it’s capable of usage in other Django web applications. For example, you can use just the contract or account app in your Django web applications. You can also take advantage of its scalability and quickly develop it. It is worth noticing that Forget password, Change password, Log in with users' email, and also simple Django Recaptcha were embedded in the account app.<br />
Users can make a new contract, write their contract, and hit the confirm button. At this stage, the user will be authenticated by the JWT method and will just need to grant consent. There is no need to register on Docusign or have an account. In other words, the user must give consent to the developer for authentication. However, users have to log in to your website.<br />
The second step is about the second signer's data. The user fills out the other signatory party's data, like name, email, and date for sending the contract.<br />

Now it is time for the user signature. The user, after signing, comes back to your app and sees a success page, and their contract will immediately be sent to another signatory email.<br />
Eventually, both of them will have a PDF digital contract with two signatures in their email inboxes.<br />

 
## Django wrapper app for DocuSign embedded functionality (deep dive into the app)<br />

To use the system, you must add your private data as a software developer. The app benefits from JWT authentication using the DocuSign API, so developers should have their own personal data, including private key, public key, access token, etc.<br />
Achieving all the above data just requires having a look at DocuSign documents, but I will just mention what you need to look for.<br /><br />
1-private.key               (A py file including a private key and a public key)<br />
2-ds_client_id              (the app's DocuSign Integration key)<br />
3-authorization_server      (account-d.docusign.com)<br />
4-ds_impersonated_user_id   (The User ID)<br />
5-account_id                (Account ID)<br />

Note: As I mentioned previously, detecting all the confidential data is so straightforward. Log in for free on Docusign.com, make a quick app based on your platform(Django in this case), and finally achieve your goals. In addition, there are multiple videos on the DocuSign website that teach you how you are able to find them.<br />

With the above secret data, we can get the below information.<br />

1-Consent URL<br />
2-api_account_id<br />
3-access_token<br />
4-base_path<br />
5-args<br />
6-signer client_id (ds_impersonated_user_id)<br />
It would be amazing. isn't it?<br />
 

## Installation<br />

Run  pip install docusign-esign <br/>   
Run pip install django-simple-captcha based on the below link.<br />
https://django-simple-captcha.readthedocs.io/en/latest/usage.html <br />
Run python manage.py makemigrations to create the migrations. <br />
Run python manage.py  collectstatic to transform static files from asset to static_root. <br />
Run python manage.py migrate to create the app models. <br />
Run python manage.py createsuperuser to create an admin username, email, and password to log in. (Note that you have to input the right email address because you will receive the contract in your email inbox. Don’t Forget It.). <br />
Start the development server and visit http://127.0.0.1:8000 <br />

 
Thanks <br />
Esfandiar Shiran <br />
