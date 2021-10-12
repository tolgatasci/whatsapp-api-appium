# Whatsapp Api Appium

#### REQUEMENTS
    ROOT PHONE or EMULATOR
### Start appium 

    appium  --allow-insecure=adb_shell

### Device Setting

    # Edit helper/config.py CAPS
    CAPS = dict(
        platformName='Android',
        platformVersion='28',
        automationName='UiAutomator2',
        udid='emulator-5554')

It's just normal texting for now. However, I will add picture or file sending for code soon.

Thanks for the base of the project.

[@chaps/py_wa_adb](https://github.com/chaps/py_wa_adb)
