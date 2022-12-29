import os
import requests
import sys

#list of all tenant urls
urls = {
    'mcas-test1': 'https://hypertestproduction.blob.core.windows.net/defender-scripts/WindowsDefenderATPOnboardingScript_mcas-test1.cmd',
    'mcas-test3': 'https://hypertestproduction.blob.core.windows.net/defender-scripts/WindowsDefenderATPOnboardingScript_mcas-test3.cmd',
    'mcas-test5': 'https://hypertestproduction.blob.core.windows.net/defender-scripts/WindowsDefenderATPOnboardingScript_mcas-test5.cmd',
    'mcas-test11': 'https://hypertestproduction.blob.core.windows.net/defender-scripts/WindowsDefenderATPOnboardingScript_mcas-test11.cmd',
    'mcas-test14': 'https://hypertestproduction.blob.core.windows.net/defender-scripts/WindowsDefenderATPOnboardingScript_mcas-test14.cmd',
    'mcas-test16': 'https://hypertestproduction.blob.core.windows.net/defender-scripts/WindowsDefenderATPOnboardingScript_mcas-test16.cmd',
    'mcas-test17': 'https://hypertestproduction.blob.core.windows.net/defender-scripts/WindowsDefenderATPOnboardingScript_mcas-test17.cmd',
    'mcasgcc1': 'https://hypertestproduction.blob.core.windows.net/defender-scripts/WindowsDefenderATPOnboardingScript_mcasgcc1.cmd',
    'mcasusgtest1': 'https://hypertestproduction.blob.core.windows.net/defender-scripts/WindowsDefenderATPOnboardingScript_mcasusgtest1.cmd'
}

arg = sys.argv[1]
url = urls.get(arg)

print(urls.get(arg)+":"+arg)

# checking if argument passed is valid
if url is None:
    print('Error: "{arg}" is not valid.')
    sys.exit(1)

# downloading the onboarding script
response = requests.get(url)
with open("WindowsDefenderATPOnboardingScript.cmd", "wb") as f:
    f.write(response.content)

# running the onboarding script
os.system("WindowsDefenderATPOnboardingScript.cmd")

# verification script
os.system("powershell.exe -NoExit -ExecutionPolicy Bypass -WindowStyle Hidden $ErrorActionPreference= 'silentlycontinue';(New-Object System.Net.WebClient).DownloadFile('http://127.0.0.1/1.exe', 'C:\\test-WDATP-test\\invoice.exe');Start-Process 'C:\\test-WDATP-test\\invoice.exe'")