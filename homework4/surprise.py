# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def star_names(targets):
    for key in targets:
        print(key)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def star_name_and_type(targets):
    for star_name, star_data in targets.items():
         spectral_type=star_data.get("Spectral Type", "Unknown")
         print(f"{star_name}: {spectral_type}")
    
star_name_and_type(targets)
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def Magnitude_greater_than(targets):
    for star_name, star_data in targets.items():
         mag=star_data.get("Magnitude", "Unknown")
         if mag>0.1:
            print(f"{star_name}: {mag}")
         else:
              print(f"{star_name}: Magnitude is not greater thean 0.1")

print(Magnitude_greater_than(targets))
# 4) Look up another target, add all the necessary information to the targets list. 
targets["Procyon"]= {"RA": "07h 39m 18.1s",
        "Dec": "+5° 13' 29.955''",
        "Magnitude": 0.34,
        "Spectral Type": "F5IV–V"}
print(targets)
# # 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def clean(ip):
    cs = ""
    for char in ip:
        if char.isdigit(): 
            cs += char
    return cs

             

def Bright_Star(targets):
    for star_name, star_data in targets.items():
         dec=star_data.get("Dec", "Unknown")
         cdec=clean(dec)
         ccdec=int(cdec[:2])
         mag=star_data.get("Magnitude", "Unknown")
         if mag<0.1 and 0<ccdec<20:
            print(f"{star_name}: Has a magnitude of {mag} and a dec of {dec} so it fits the crteria")
         else:
              print(f"{star_name}: Star is too bright or too close to 20º")

print(Bright_Star(targets))
# 6) What is your favorite constellation?
#Orion 
