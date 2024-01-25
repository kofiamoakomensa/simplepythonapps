# No Exception handling if type in capital case 
# what if patient symptoms are in different lists 


def main():
    # Define a simple symptom to disease mapping
    medical_database = {
        "Common Cold": ["cough", "sneezing", "sore throat"],
        "Flu": ["cough", "fever", "headache", "muscle aches"],
        "Allergy": ["sneezing", "itchy eyes", "runny nose"]
    }

    print("Welcome to the Hospital Diagnosis App")
    symptoms = input("Enter your symptoms, separated by commas: ").split(',')

    # Normalize and trim user input
    symptoms = [symptom.strip().lower() for symptom in symptoms]

    possible_conditions = diagnose(symptoms, medical_database)
    print("Based on your symptoms, you might have:", possible_conditions)


def diagnose(symptoms, medical_database):
    possible_conditions = []
    for condition, condition_symptoms in medical_database.items():
        if all(symptom in condition_symptoms for symptom in symptoms):
            possible_conditions.append(condition)
    return possible_conditions if possible_conditions else ["No matching condition found"]


if __name__ == "__main__":
    main()
