from abc import ABC, abstractmethod
#Abstract Base Class:
# The Person class serves as an abstract base class, providing common attributes and methods 
# for all individuals in the hospital system, such as name, age, and id_number. It uses an abstract method 
#`get_info()` to enforce a custom implementation in subclasses.

class Person(ABC):
    def __init__(self, name, age, id_number):
        self.name = name            # Public attribute for the name of the person
        self.age = age              # Public attribute for the age of the person
        self.id_number = id_number  # Public attribute for the ID number of the person

    @abstractmethod
    def get_info(self):# Abstract method to be implemented by subclasses
      
        pass


#Patient Class (Inheritance ;subclass of Person):
#The Patient class inherits from Person and represents a hospital patient. It includes a private attribute,
#`__medical_history`, which is accessed and modified only through methods, supporting encapsulation.
class Patient(Person):
    def __init__(self, name, age, id_number, medical_history=None):
        super().__init__(name, age, id_number)  # Initializes inherited attributes
        self.__medical_history = medical_history if medical_history else []  # Private list for medical records

    def add_medical_record(self, record):
        # Method to add a medical record to the patient's history
        self.__medical_history.append(record)

    def get_medical_history(self):
        # Method to retrieve the patient's medical history
        return self.__medical_history

    def get_info(self):
        # Returns a summary of the patient's details
        return f"Patient {self.name}, Age: {self.age}, ID: {self.id_number}"


#Doctor Class(Inheritance ;subclass of Person)     
# The Doctor class also inherits from Person and represents a hospital doctor. Each doctor has a specialty and can be assigned multiple patients. 
# This class implements methods to assign patients and retrieve a list of assigned patients.
class Doctor(Person):
    def __init__(self, name, age, id_number, specialty):
        super().__init__(name, age, id_number)  # Initialize inherited attributes
        self.specialty = specialty              # Public attribute for the doctor's specialty
        self.patients = []                      # List to store assigned patients

    def assign_patient(self, patient): #method to assign a patient to the doctor, adds a patient to the doctor's patient list if the patient is an instance of Patient
        if isinstance(patient, Patient):
            self.patients.append(patient)
            print(f"{patient.name} assigned to Dr. {self.name} (Specialty: {self.specialty})")

    def get_patients(self): #method to retrieve a list of assigned patients
        return [patient.get_info() for patient in self.patients]

    def get_info(self): #method to return a summary of the doctor's details
        return f"Doctor {self.name}, Specialty: {self.specialty}, ID: {self.id_number}"


# Appointment Class 
# The Appointment class handles the scheduling of appointments between a doctor and a patient at a specific date and time it links instances of Doctor and Patient classes.
class Appointment:
    def __init__(self, doctor, patient, date, time):
        self.doctor = doctor  # Doctor object for the appointment
        self.patient = patient  # Patient object for the appointment
        self.date = date       # Appointment date
        self.time = time       # Appointment time

    def get_details(self): #method to return a formatted string with appointment details
        return f"Appointment with Dr. {self.doctor.name} for {self.patient.name} on {self.date} at {self.time}"


# Hospital Management System Class
# The HospitalManagementSystem class serves as a high-level interface for managing the hospital's  patients, doctors, and appointments.
# It includes methods to add doctors and patients, schedule appointments, and view scheduled appointments.
class HospitalManagementSystem:
    def __init__(self):
        self.patients = []     # List to store all patients
        self.doctors = []      # List to store all doctors
        self.appointments = [] # List to store all appointments

    def add_patient(self, name, age, id_number): #method to add a new Patient object to the system
        new_patient = Patient(name, age, id_number)
        self.patients.append(new_patient)
        print(f"Patient {name} added successfully.")
        return new_patient

    def add_doctor(self, name, age, id_number, specialty): #method to add a new Doctor object to the system
        new_doctor = Doctor(name, age, id_number, specialty)
        self.doctors.append(new_doctor)
        print(f"Doctor {name} added successfully.")
        return new_doctor

    def schedule_appointment(self, doctor, patient, date, time): #method to schedule an appointment between a doctor and a patient
        appointment = Appointment(doctor, patient, date, time)
        self.appointments.append(appointment)
        doctor.assign_patient(patient)  # Assigns the patient to the doctor
        print("Appointment scheduled successfully.")
        return appointment

    def get_appointments(self): #method to retrieve a list of all scheduled appointments
        return [appointment.get_details() for appointment in self.appointments]


# Main Execution  (Creating an instance of the HospitalManagementSystem class and demonstrating the functionality) 
if __name__ == "__main__":
    # Initialize the hospital management system
    hms = HospitalManagementSystem()

    # Adding doctors
    doctor_kim = hms.add_doctor("Dr.Kim", 22, "D001", "Cardiology")
    doctor_josh = hms.add_doctor("Dr.Josh ",33, "D002", "Neurology")

    # Adding patients
    patient_catherine = hms.add_patient("Catherine", 30, "P001")
    patient_johns = hms.add_patient("Johns Bonnes", 27, "P002")

    # Scheduling appointments
    hms.schedule_appointment(doctor_kim, patient_catherine, "2024-11-15", "10:00 AM")
    hms.schedule_appointment(doctor_josh, patient_johns, "2024-11-16", "11:00 AM")

    # Viewing all scheduled appointments
    for appointment_detail in hms.get_appointments():
        print(appointment_detail)
