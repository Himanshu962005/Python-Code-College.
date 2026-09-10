# E44.Shoutouts to Everyone in Python.
from os import system;
names = [
    "AADIL FARAZ",
    "AAKASH",
    "ANISH KANNAUJE",
    "ANKIT SINGH CHOUHAN",
    "BHIKHRANSHU NETAM",
    "DIGESH KUMAR SAHU",
    "DIPIKA",
    "DIVYA PANDEY",
    "HIMANSHU KARWA",
    "JAISHREE TANDI",
    "KARISHMA SAHU",
    "KHUSHI SEN",
    "KHAYATI DHRUW",
    "LAXMI SAHU",
    "NISHA SAHU",
    "P RAHUL",
    "PRAGYANSHU MISHRA",
    "PRASHANT VERMA",
    "RAJKUMAR MANDLE",
    "RISHABH BORKAR",
    "RUKESH SIDAR",
    "RUKHMANI NISHAD",
    "SAYED NAWAJISH ALI",
    "SHAYRA BANO",
    "SUSHMA SAHU",
    "YUGAL KISHOR CHANDRAKAR",
]
for name in names:
    system(
        f'powershell -Command "Add-Type -AssemblyName System.Speech; '
        f"$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
        f"$speak.Speak('Shoutout to {name}')\""
    )