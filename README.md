# AutoBathroomPass
A script to automatically fill out my school's bathroom pass form.

### Why am I making this?
My school recently implemented a policy that requires all students to fill out a Google form which is 
obtainable via QR code before going to the bathroom. While this might be good for their
internal management, it's a pain for students to fill out for the following reasons:
- The Wi-Fi sucks and almost never works on mobile devices (the device type primarily used to scan the code)
- Cellular data has a poor connection at my school, and not every student has access to it
- Not every student has a phone
- The form requires you to sign into your district Google account, which is a pain when dealing with poor connection
- It takes longer to fill out the form than it would actually take to go to the bathroom

After a couple of days, I decided I had enough, so I made this script to automate the process.
All one needs to do is run the script, input the day, and the rest will be done for you.

### Instructions
1. Install the following
- Python 3 (This was tested using Python 3.9, but other v3 versions should work fine)
- Selenium (pip install selenium)
2. Download a chrome driver and add it to the root directory of this script
https://chromedriver.chromium.org/downloads
3. Rename "_config.py" to "config.py" and fill out the necessary information
4. Run the script

### Limitations
Because I don't intend to market this in any way, I hard coded some values such as the entry IDs.
The directory path is also hard coded at this time (except for the Windows profile name) so this may need to be adjusted
depending on your directory path/OS
These aren't necessarily the best way to do things for broad use, but considering I only intended this to be used for
myself and friends, it wouldn't be worth the extra time to make it more flexible.
Despite this, it should be extremely easy to modify the script to suit your needs as it doesn't have a lot of code