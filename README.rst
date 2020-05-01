==================
CURRENCY EXTRACTOR
==================

This project extract currency rate hourly using exchange rate api `https://exchangeratesapi.io/` and will write to csv file for further analysis.

PROJECT REQUIRMENT
===================

To run this project we have following requirment:
* Python_=> 3.6.10
* Ubuntu_=> 16.04 (I have tested this on ubuntu and also i have made a Make file for ubuntu)
* Make sure you have install make already.


PROJECT SETUP
=============
This will be the ``README`` for this project. For now, follow these instructions to get this project set up correctly.

Instructions
------------

#. Unzip a project using unzip package in ubuntu.To unzip our project first we need unzip package.

        sudo apt-get install unzip
        cd bubbel_project

#. Edit the config.json ``config/config.json`` to update your api key from excahnge rates.


#. Run the following command to create virtual environment:

        make init


#. After creation of environment we need to install dependencies that required to run our project.To install dependencies run following command:
        make install

#. (Opentional) If we want to reformat code or want to test our code quality we need to run following command:
 
        make format-code
 
#. To test code i have written two type of test cases (unit tests,integration tests).To run these test cases you need following command:
 
        make test

#. Finally to run a project you need following command:
 
        make run
 
#. If you want to csv file and want to stop project you need to run following command:

        make clean
 
 

