import webbrowser
import speech_recognition as s
from speech_recognition import UnknownValueError

sr = s.Recognizer()

def Vocalib():
    try:
        with s.Microphone() as m:
            sr.adjust_for_ambient_noise(m)
            print("Listening...\n")
            audio = sr.listen(m, timeout=15, phrase_time_limit=15)
            query = sr.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
    except UnknownValueError:
        print("Sorry, I did not understand. Please try again.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

def Quess(question):
    print(question)
    while True:
        response = Vocalib()
        if "yes" in response:
            return True
        elif "no" in response:
            return False
        else:
            print("Please say 'yes' or 'no'.")

# List of valid fever types
valid_fever_types = [
    "typhoid fever", "dengue fever", "yellow fever", "scarlet fever",
    "rheumatoid fever", "ebola virus disease", "marburg hemorrhagic fever", "drug fever"
]

print("Welcome to FeverFind!!\n")

if Quess("Are you looking for certain fever codes in ICD-10 or SNOMED? Say yes or no."):
    print("We will give you fever names which we have in this module.")
    print("Say the name of the fever, then we will give you options for ICD-10 or SNOMED.\n")

    if Quess("Do you understand the instructions? Say 'Yes' or 'No'."):
        # Loop until a valid fever type is provided
        while True:
            print("Select from the list below by saying the fever type which you want:\nTyphoid Fever\nDengue Fever\nYellow Fever\nScarlet Fever\nRheumatoid Fever\nEbola Virus Disease\nMarburg Hemorrhagic Fever\nDrug Fever\n")
            fever_type = Vocalib()
            print(f"You selected: {fever_type}")

            # Check if the input is a valid fever type
            if fever_type in valid_fever_types:
                break  # Exit the loop if a valid fever is selected
            else:
                print(f"'{fever_type}' is not a valid fever type. Please select a valid fever type from the list.\n")

        # Loop for user preference until a valid response is provided
        while True:
            print("Do you want the fever code in ICD-10 or SNOMED? Please say (run) for 'ICD-10' or (luck) for 'SNOMED'.")
            preference = Vocalib()

            if "run" in preference:
                if fever_type == "typhoid fever":
                    print("Opening Typhoid fever ICD-10 link...")
                    webbrowser.open("https://icd.who.int/browse10/2019/en#/A01.0")
                elif fever_type == "dengue fever":
                    print("Opening Dengue fever ICD-10 link...")
                    webbrowser.open("https://icd.who.int/browse10/2019/en#/A97")
                elif fever_type == "yellow fever":
                    print("Opening Yellow fever ICD-10 link...")
                    webbrowser.open("https://icd.who.int/browse10/2019/en#/A95")
                elif fever_type == "scarlet fever":
                    print("Opening Scarlet fever ICD-10 link...")
                    webbrowser.open("https://icd.who.int/browse10/2019/en#/A38")
                elif fever_type == "rheumatoid fever":
                    print("Opening Rheumatoid fever ICD-10 link...")
                    webbrowser.open("https://icd.who.int/browse10/2019/en#/I00-I02")
                elif fever_type == "ebola virus disease":
                    print("Opening Ebola Virus Disease ICD-10 link...")
                    webbrowser.open("https://icd.who.int/browse10/2019/en#/A98.4")
                elif fever_type == "marburg hemorrhagic fever":
                    print("Opening Marburg Hemorrhagic Fever ICD-10 link...")
                    webbrowser.open("https://icd.who.int/browse10/2019/en#/A98.3")
                elif fever_type == "drug fever":
                    print("Opening Drug fever ICD-10 link...")
                    webbrowser.open("https://icd.who.int/browse10/2019/en#/R50.2")
                break  # Exit the loop after opening the ICD-10 link

            elif "luck" in preference:
                if fever_type == "typhoid fever":
                    print("Opening Typhoid fever SNOMED link...")
                    webbrowser.open("https://browser.ihtsdotools.org/?perspective=full&conceptId1=4834000&edition=MAIN/2024-10-01&release=&languages=en")
                elif fever_type == "dengue fever":
                    print("Opening Dengue fever SNOMED link...")
                    webbrowser.open("https://browser.ihtsdotools.org/?perspective=full&conceptId1=38362002&edition=MAIN/2024-10-01&release=&languages=en")
                elif fever_type == "yellow fever":
                    print("Opening Yellow fever SNOMED link...")
                    webbrowser.open("https://browser.ihtsdotools.org/?perspective=full&conceptId1=16541001&edition=MAIN/2024-10-01&release=&languages=en")
                elif fever_type == "scarlet fever":
                    print("Opening Scarlet fever SNOMED link...")
                    webbrowser.open("https://ips-browser.ihtsdotools.org/?perspective=full&conceptId1=30242009&edition=MAIN/2023-07-31&release=&languages=en")
                elif fever_type == "rheumatoid fever":
                    print("Opening Rheumatoid fever SNOMED link...")
                    webbrowser.open("https://browser.ihtsdotools.org/?perspective=full&conceptId1=58718002&edition=MAIN/2024-10-01&release=&languages=en")
                elif fever_type == "ebola virus disease":
                    print("Opening Ebola Virus Disease SNOMED link...")
                    webbrowser.open("https://ips-browser.ihtsdotools.org/?perspective=full&conceptId1=424206003&edition=MAIN/2023-07-31&release=&languages=en")
                elif fever_type == "marburg hemorrhagic fever":
                    print("Opening Marburg Hemorrhagic Fever SNOMED link...")
                    webbrowser.open("https://ips-browser.ihtsdotools.org/?perspective=full&conceptId1=424421007&edition=MAIN/2023-07-31&release=&languages=en")
                elif fever_type == "drug fever":
                    print("Opening Drug fever SNOMED link...")
                    webbrowser.open("https://ips-browser.ihtsdotools.org/?perspective=full&conceptId1=405543000&edition=MAIN/2023-07-31&release=&languages=en")
                break  # Exit the loop after opening the SNOMED link

            else:
                print("Sorry, I didn't catch that. Please say 'run' or 'luck'.")