



def main():
    # Define a simple symptom to disease mapping
    medical_database = {
        "Common Cold": ["cough", "sneezing", "sore throat"],
        "Flu": ["cough", "fever", "headache", "muscle aches"],
        "Allergy": ["sneezing", "itchy eyes", "runny nose"]
    }

    print("Welcome to the Hospital Diagnosis App")

    try:
        symptoms = input("Enter your symptoms, separated by commas: ").split(',')
        # Normalize and trim user input
        symptoms = [symptom.strip().lower() for symptom in symptoms]

        # Validate user input
        if not all_symptoms_valid(symptoms, medical_database):
            print("Some symptoms are not recognized. Please try again.")
            return

        possible_conditions = diagnose(symptoms, medical_database)
        print("Based on your symptoms, you might have:", possible_conditions)
    except Exception as e:
        print(f"An error occurred: {e}")


def all_symptoms_valid(symptoms, medical_database):
    all_symptoms = set(symptom for condition in medical_database.values() for symptom in condition)
    return all(symptom in all_symptoms for symptom in symptoms)


def diagnose(symptoms, medical_database):
    possible_conditions = []
    for condition, condition_symptoms in medical_database.items():
        if all(symptom in condition_symptoms for symptom in symptoms):
            possible_conditions.append(condition)
    return possible_conditions if possible_conditions else ["No matching condition found"]


if __name__ == "__main__":
    main()
