# if not any(website in line for website in website_list)

import sys
import time
from datetime import datetime as dt

# User can specify which hour manually, generally for testing
# If the argument is an invalid integer, then ignore it
manual_hour = None
if len(sys.argv) > 1:
    try:
        manual_hour = int(sys.argv[1])

        if manual_hour < 0 or manual_hour > 23:
            raise ValueError

    except ValueError:
        manual_hour = None

hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect_ip = "127.0.0.1"
website_list = [
    "www.facebook.com", "facebook.com",
    "www.google.com", "google.com"
]

redirected_sites = ["### Website redirect -- START\n"]
for website in website_list:
    redirected_sites.append(f"{redirect_ip} {website}\n")
redirected_sites.append("### Website redirect -- END\n") 

while True:
    start_time = dt(dt.now().year, dt.now().month, dt.now().day, 8)
    end_time = dt(dt.now().year, dt.now().month, dt.now().day, 16)
    current_time = dt.now()

    if manual_hour != None:
        current_time = dt(dt.now().year, dt.now().month, dt.now().day, manual_hour)

    # DURING WORK HOURS
    if (start_time < current_time < end_time):
        with open(hosts_temp, "r+") as file:
            lines = file.readlines()

            # Better to ask forgiveness
            # Check if entry is already added
            # if it is, do nothing
            try:
                redirected_index = lines.index(redirected_sites[0])
            except ValueError:
                # check if there is a new line
                try:
                    newline_index = lines.index("\n")
                # use the end of file in exception
                except ValueError:
                    newline_index = len(lines)

                # when at the end of the IPV4 entries, 
                # insert our redirected_sites list
                lines = lines[0:newline_index] + redirected_sites + lines[newline_index:]

                file.seek(0)  # readlines consumes the iterator, so we need to start over
                file.writelines(lines)

    # DURING FREE HOURSE
    else:
        with open(hosts_temp, "r+") as file:
            lines = file.readlines()

            try:
                redirected_start_index = lines.index(redirected_sites[0])
                redirected_end_index = lines.index(redirected_sites[len(redirected_sites) - 1])

                lines = lines[0:redirected_start_index] + lines[(redirected_end_index + 1):]

                file.seek(0)  # readlines consumes the iterator, so we need to start over
                file.writelines(lines)
                file.truncate()
            except ValueError:
                pass

    time.sleep(5)