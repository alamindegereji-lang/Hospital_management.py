# HOSPITAL PATIENT AND APPOINTMENT MANAGEMENT SYSTEM

patients = []
appointments = []
bills = []

patient_counter = 1
appointment_counter = 1
total_revenue = 0

# Consultation charges
departments = {
    "General": 5000,
    "Dental": 10000,
    "Eye Clinic": 8000,
    "Cardiology": 15000
}


# Register a new patient
def register_patient():
    global patient_counter

    print("\n--- PATIENT REGISTRATION ---")

    name = input("Enter patient name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter patient name: ").strip()

    while True:
        try:
            age = int(input("Enter patient age: "))
            if age <= 0:
                print("Age must be greater than zero.")
            else:
                break
        except ValueError:
            print("Please enter a valid age.")

    phone = input("Enter phone number: ").strip()

    while not phone:
        print("Phone number cannot be empty.")
        phone = input("Enter phone number: ").strip()

    patient_id = f"P{patient_counter:03d}"

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "phone": phone
    }

    patients.append(patient)
    patient_counter += 1

    print("\nPatient registered successfully!")
    print("Patient ID:", patient_id)


# View all registered patients
def view_patients():
    print("\n--- REGISTERED PATIENTS ---")

    if not patients:
        print("No patients registered yet.")
        return

    for patient in patients:
        print("-------------------------")
        print("Patient ID:", patient["id"])
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Phone:", patient["phone"])


# Search for a patient
def search_patient():
    print("\n--- SEARCH PATIENT ---")

    patient_id = input("Enter patient ID: ").strip().upper()

    for patient in patients:
        if patient["id"] == patient_id:
            print("\nPatient found!")
            print("ID:", patient["id"])
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Phone:", patient["phone"])
            return

    print("Patient not found.")


# Book an appointment
def book_appointment():
    global appointment_counter

    print("\n--- BOOK APPOINTMENT ---")

    patient_id = input("Enter patient ID: ").strip().upper()

    patient = None

    for p in patients:
        if p["id"] == patient_id:
            patient = p
            break

    if patient is None:
        print("Patient ID does not exist.")
        return

    print("\nAvailable Departments:")

    for department, charge in departments.items():
        print(f"{department}: N{charge:,}")

    department = input("\nEnter department: ").strip().title()

    if department not in departments:
        print("Invalid department.")
        return

    day = input("Enter appointment day/date: ").strip()
    time = input("Enter appointment time: ").strip()

    if not day or not time:
        print("Day and time cannot be empty.")
        return

    # Prevent duplicate appointment slots
    for appointment in appointments:

        same_slot = (
            appointment["day"].lower() == day.lower()
            and appointment["time"].lower() == time.lower()
        )

        if same_slot:
            print("This appointment slot is already booked.")
            return

        # Prevent one patient from booking twice at the same time
        same_patient = (
            appointment["patient_id"] == patient_id
            and appointment["day"].lower() == day.lower()
            and appointment["time"].lower() == time.lower()
        )

        if same_patient:
            print("Patient already has an appointment at this time.")
            return

    appointment_id = f"A{appointment_counter:03d}"

    appointment = {
        "id": appointment_id,
        "patient_id": patient_id,
        "patient_name": patient["name"],
        "department": department,
        "day": day,
        "time": time
    }

    appointments.append(appointment)
    appointment_counter += 1

    print("\nAppointment booked successfully!")
    print("Appointment ID:", appointment_id)


# View all appointments
def view_appointments():
    print("\n--- APPOINTMENT RECORDS ---")

    if not appointments:
        print("No appointments available.")
        return

    for appointment in appointments:
        print("-------------------------")
        print("Appointment ID:", appointment["id"])
        print("Patient ID:", appointment["patient_id"])
        print("Patient Name:", appointment["patient_name"])
        print("Department:", appointment["department"])
        print("Day/Date:", appointment["day"])
        print("Time:", appointment["time"])


# Cancel an appointment
def cancel_appointment():
    print("\n--- CANCEL APPOINTMENT ---")

    appointment_id = input("Enter appointment ID: ").strip().upper()

    for appointment in appointments:
        if appointment["id"] == appointment_id:
            appointments.remove(appointment)
            print("Appointment cancelled successfully.")
            return

    print("Appointment not found.")


# Calculate patient bill
def calculate_bill():
    global total_revenue

    print("\n--- PATIENT BILLING ---")

    patient_id = input("Enter patient ID: ").strip().upper()

    patient = None

    for p in patients:
        if p["id"] == patient_id:
            patient = p
            break

    if patient is None:
        print("Patient not found.")
        return

    print("\nAvailable Departments:")

    for department, charge in departments.items():
        print(f"{department}: N{charge:,}")

    department = input("\nEnter consultation department: ").strip().title()

    if department not in departments:
        print("Invalid department.")
        return

    consultation_charge = departments[department]

    additional_charge = 0

    extra = input("Is there any additional service charge? (yes/no): ").strip().lower()

    if extra == "yes":
        while True:
            try:
                additional_charge = float(
                    input("Enter additional service charge: N")
                )

                if additional_charge < 0:
                    print("Charge cannot be negative.")
                else:
                    break

            except ValueError:
                print("Enter a valid amount.")

    total_bill = consultation_charge + additional_charge

    bill = {
        "patient_id": patient_id,
        "patient_name": patient["name"],
        "department": department,
        "consultation_charge": consultation_charge,
        "additional_charge": additional_charge,
        "total": total_bill
    }

    bills.append(bill)
    total_revenue += consultation_charge

    print("\n========== PATIENT BILL ==========")
    print("Patient Name:", patient["name"])
    print("Patient ID:", patient_id)
    print("Department:", department)
    print("Consultation Charge: N{:,.2f}".format(consultation_charge))
    print("Additional Charges: N{:,.2f}".format(additional_charge))
    print("----------------------------------")
    print("TOTAL BILL: N{:,.2f}".format(total_bill))
    print("==================================")


# Display system statistics
def display_statistics():
    print("\n--- HOSPITAL STATISTICS ---")
    print("Total Patients Registered:", len(patients))
    print("Total Appointments:", len(appointments))
    print("Total Bills Generated:", len(bills))
    print("Total Consultation Revenue: N{:,.2f}".format(total_revenue))


# Main menu
def main():

    while True:

        print("\n======================================")
        print(" HOSPITAL MANAGEMENT SYSTEM")
        print("======================================")

        print("1. Register a New Patient")
        print("2. View Registered Patients")
        print("3. Book an Appointment")
        print("4. View Appointments")
        print("5. Calculate Patient Bill")
        print("6. Search Patient by ID")
        print("7. Cancel an Appointment")
        print("8. Display Total Patients Registered")
        print("9. Display Total Consultation Revenue")
        print("10. Exit")

        choice = input("\nEnter your choice (1-10): ").strip()

        if choice == "1":
            register_patient()

        elif choice == "2":
            view_patients()

        elif choice == "3":
            book_appointment()

        elif choice == "4":
            view_appointments()

        elif choice == "5":
            calculate_bill()

        elif choice == "6":
            search_patient()

        elif choice == "7":
            cancel_appointment()

        elif choice == "8":
            print("\nTotal Registered Patients:", len(patients))

        elif choice == "9":
            print(
                "\nTotal Consultation Revenue: N{:,.2f}".format(
                    total_revenue
                )
            )

        elif choice == "10":
            print("\nThank you for using Hospital Management System.")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select between 1 and 10.")


# Run the program
if __name__ == "__main__":
    main()
