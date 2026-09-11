# E53.Drink Water Reminder in Python.
import os;
import time;
REPEAT_INTERVAL = 3600 # Repeat Frequency in Seconds.
while True:
    command = (
        'powershell -Command "'
        "Add-Type -AssemblyName System.Speech; "
        "$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
        "$speak.Speak('Hey, Himanshu! Drink Water')\""
    )
    os.system(command)
    os.system(
        'powershell -Command "'
        "[System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms'); "
        "[System.Windows.Forms.MessageBox]::Show('Hey, Himanshu! Drink Water', 'Water Reminder')\""
    )
    time.sleep(REPEAT_INTERVAL)