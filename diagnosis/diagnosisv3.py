

def main():
    # Define a simple symptom to disease mapping
    medical_database = {
        "Common Cold": ["cough", "sneezing", "sore throat"],
        "Flu": ["cough", "fever", "headache", "muscle aches"],
        "Allergy": ["sneezing", "itchy eyes", "runny nose"]
    }

    print("Welcome to the Hospital Diagnosis App")

    try:
        # Collect multiple lists of symptoms
        num_lists = int(input("How many lists of symptoms do you have? "))
        all_symptoms = []
        for i in range(num_lists):
            symptoms_input = input(f"Enter symptoms from list {i+1}, separated by commas: ").split(',')
            symptoms = [symptom.strip().lower() for symptom in symptoms_input]
            all_symptoms.extend(symptoms)

        # Validate user input
        if not all_symptoms_valid(all_symptoms, medical_database):
            print("Some symptoms are not recognized. Please try again.")
            return

        possible_conditions = diagnose(all_symptoms, medical_database)
        print("Based on your symptoms, you might have:", possible_conditions)
        print("You will need to see a medical doctor")
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
