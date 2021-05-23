from cowin_api import CoWinAPI
import winsound
import argparse
import datetime
import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='cowin')
    parser.add_argument('-p', '--pincode', type=str, help="pincode of the area")
    parser.add_argument('-a', '--age', type=int, help="age")
    parser.add_argument('-v', '--vaccine', type=str, help="covaxin or covishield")
    parser.add_argument('-d', '--dose', type=int, help="dose 1 or dose 2")
    parser.add_argument('-t', '--timeout', type=int, help="retry time in sec(60 second default)")
    args = parser.parse_args()

    if args.pincode is None:
        print("Enter with --pincode <>")
        exit(0)

    timeout = 60
    if args.timeout:
        timeout = args.timeout
    
    dose = 1
    if args.dose:
        dose = args.dose
    
    pin_code = args.pincode
    date = datetime.datetime.today().strftime('%d-%m-%Y')
    min_age_limit = 18
    if args.age is not None:
        min_age_limit = args.age
    frequency = 2500
    duration = 2000

    cowin = CoWinAPI()

    print("Running the vaccine script for the pincode {} age {} date {} dose {}".format(pin_code, min_age_limit, date, dose))
    while True:
        time.sleep(timeout)
        try:
            available_centers = cowin.get_availability_by_pincode(pin_code, date, min_age_limit)
            centers = available_centers['centers']
            i = 1
            for center in centers:
                sessions = center['sessions']
                for session in sessions:
                    if (args.vaccine is None or args.vaccine.lower() == session['vaccine'].lower()) and \
                        ((dose == 1 and session['available_capacity_dose1'] != 0) or (dose == 2 and session['available_capacity_dose2'] != 0)):
                      
                        print("{}.Available for the pincode {} age {} date {} vaccine {} dose {}".format(i, pin_code, min_age_limit, session['date'],
                            session['vaccine'].lower(), dose))
                        i += 1
                        winsound.Beep(frequency, duration)
        except Exception:
            print("Unable to get centers, it will be re run after 15 sec")
            time.sleep(15)
