from cowin_api import CoWinAPI
import winsound
import argparse
import datetime
import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='cowin')
    parser.add_argument('-p', '--pincode', type=str, help="pincode of the area")
    parser.add_argument('-a', '--age', type=int, help="age")
    args = parser.parse_args()

    if args.pincode is None:
        print("Enter with --pincode <>")
        exit(0)

    pin_code = args.pincode
    date = datetime.datetime.today().strftime('%d-%m-%Y')
    min_age_limit = 18
    if args.age is not None:
        min_age_limit = args.age
    frequency = 2500
    duration = 1000

    cowin = CoWinAPI()

    print("Running the vaccine script for the pincode {} age {} date {}".format(pin_code, min_age_limit, date))
    while True:
        time.sleep(5)
        try:
            available_centers = cowin.get_availability_by_pincode(pin_code, date, min_age_limit)
            centers = available_centers['centers']
            for center in centers:
                sessions = center['sessions']
                for session in sessions:
                    if session['available_capacity'] != 0:
                        print("Slots available for the pincode {} age {} date {}".format(pin_code, min_age_limit,date))
                        while True:
                            winsound.Beep(frequency, duration)
        except Exception:
            print("Unable to get centers, it will be re run after 2 min")
            time.sleep(120)
