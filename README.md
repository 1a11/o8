# O8 
<a href="https://www.buymeacoffee.com/1a11" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

O8 is the OSINT a tool that combines many others. OSINT has never been so fast and convenient. In this project are used:

  - phoneinfoga
  - h8mail
  - ip-api
  - haveibeenpwned
  - intelx

O8 allows you to quickly gather the information you need about a person by a variety of parameters, including: first name, last name, patronymic, IP address, e-mail address and user names.

# Installation
Clone O8 repo:
```sh
$ git clone https://github.com/1a11/o8.git
$ cd o8
```
Install dependencies : 
```
$ cd ./tools 
$ pip3 install -r requirements.txt
```
Wait until pip finish it's work. We also need to download and install phoneinfoga. Navigate to it's [repo](https://github.com/sundowndev/PhoneInfoga) and follow the installation instructions. Phoneinfoga binary is located in *tools* folder.
Now just run ***core[dot]py***.

Now, I do not utilize name params, but I will add this ASAP.

This software is licensed under GPL-3.0 licens. 
