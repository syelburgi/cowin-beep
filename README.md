# cowin-beep
This will help in getting the slot availability for covid vaccine by alerting(BEEP sound) the user.

Requirements:
Windows laptop 

Installation:
1. Install python3
2. Download the script and requirement file
3. run 'pip install -r requirement.txt'. (open command prompt and run this)
4. test it by running 'python3 cowin-beep.py --pincode 583227 --age 45'. if you hear beep sound then script is working . if you don't hear the sound  mail to sandeepyelburgi@gmail.com. stop the script by doing ctrl-c


Run:
python3 cowin-beep.py --pincode <your pincode> (by default it is run against 18 age). if you want to specific age group then run
python3 cowin-beep.py --pincode <your pincode> --age 45
 
if you are looking for specific vaccine like covaxin/covishield then it can be run like below
 python3 cowin-beep.py --pincode <your pincode> --age 45 --vaccine covaxin 
 python3 cowin-beep.py --pincode <your pincode> --age 45 --vaccine covishield
