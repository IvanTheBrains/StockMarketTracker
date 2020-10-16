# Stock Market Tracker

Compatible with Mac **ONLY**.

## Installation 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install external package called pync:

```bash
pip install pync
```

Pync is a module which allows you to send User Notifications to the Notification Center on Mac OS X 10.10, or higher.

When you will install this package just run this code:

```python
import pync
pync.notify("Hello World!")
```

Then you will see a popup where your Mac asks you to permit access to the notifications. Just press __accept__ button.

## Review of my project
This script will help you to monitor the actual price for the chosen object and also will notify you with the sound, that the price has changed.  
This script works only with [BCS Express](https://bcs-express.ru) website and the main link used in the script should be taken from [here](https://bcs-express.ru/kotirovki-i-grafiki). Just choose the share or futures you want click the link and copy that.
> I chose Amazon share and the link (URL) will look like this - [https://bcs-express.ru/kotirovki-i-grafiki/amzn](https://bcs-express.ru/kotirovki-i-grafiki/amzn)
    
I decided to write this project in OOP style as I thought that I will be able to create a few objects and run them together. However, I found out that I needed *multithreading*, so my first objected couldn't be interrupted with the n-object. Nevertheless, you can run more than 1 script in a few terminal windows with different URLs.  



## What I didn't finished or implemented
* Multithreading process
* Exceptions *(try/except)* for connection, requests errors
* [DYR](https://ru.wikipedia.org/wiki/Don’t_repeat_yourself) style wasn't used
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or improve.


