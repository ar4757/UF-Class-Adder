# UF-Class-Adder

This program is a bot designed to secure a spot in a full class on ONE.UF. Optimal times to run the program are during drop/add week, when chances are high that someone will drop the class.

I am not responsible for any problems that occur to your ONE.UF account in the event UF notices and/or does not approve of this program.

## Usage

Enter your UF username and password, and the course code of the desired class, and hit submit. Status of the application will be displayed on the right side of the window (e.g. "Class Full, retrying" or "Class Added!"). Program takes around 10-15 seconds to get started, then refreshes and attempts to add the class every 5 or so seconds. As long as computer is running, program will continuously run in the background, until cancelled.

UF username is your GatorLink, not your UFID number. Also make sure course code is correct - valid examples include "MAC2311", "PHY2048", and "CHM2045".

Upon receiving the "Class Added!" notification, you can end the program and check your schedule on ONE.UF. The class should be there.

Pro Tip: Keep this on the down-low, and don't use it 24/7. Instead only use it when there's a decent chance someone will drop the class, aka drop/add week.

## Bugs

Likely problems include:

- Error if desired class time overlaps a class you already have
- Program not tested on Windows or Linux

## Linux Users

This program relies on a combination of Google Chrome and the Chrome WebDriver, aka ChromeDriver 

Windows and MacOS versions of ChromeDriver are included in the driver folder

If on Linux, may have to download the correct version from https://sites.google.com/a/chromium.org/chromedriver/downloads

## Running/Building from Source

Selenium is the only external dependency. One way to install is using:
  > pip3 install selenium

Running the program:
  > python3 classadderchrome.py

Building the program:
  MacOS:
    > pyinstaller --onefile --noconsole --add-binary driver/chromedriver:driver classadderchrome.py
  Windows:
    > pyinstaller --onefile --noconsole --add-binary driver/chromedriver.exe:driver classadderchrome.py
