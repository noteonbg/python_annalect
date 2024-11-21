from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Step 1: Define the base class
Base = declarative_base()

# Step 2: Define the Patient class (table)
class Patient(Base):
    __tablename__ = 'patients'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    dob = Column(DateTime)  # Date of birth
    email = Column(String, unique=True)

    # Relationship with appointments
    appointments = relationship('Appointment', back_populates='patient')

    def __repr__(self):
        return f"Patient(id={self.id}, name={self.first_name} {self.last_name})"

# Step 3: Define the Doctor class (table)
class Doctor(Base):
    __tablename__ = 'doctors'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    email = Column(String, unique=True)

    # Relationship with appointments
    appointments = relationship('Appointment', back_populates='doctor')

    def __repr__(self):
        return f"Doctor(id={self.id}, name={self.first_name} {self.last_name}, specialty={self.specialty})"

# Step 4: Define the Appointment class (table)
class Appointment(Base):
    __tablename__ = 'appointments'
    
    id = Column(Integer, primary_key=True)
    appointment_date = Column(DateTime, default=datetime.utcnow)
    doctor_id = Column(Integer, ForeignKey('doctors.id'), nullable=False)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)

    # Relationships
    doctor = relationship('Doctor', back_populates='appointments')
    patient = relationship('Patient', back_populates='appointments')

    def __repr__(self):
        return f"Appointment(id={self.id}, doctor={self.doctor.first_name} {self.doctor.last_name}, patient={self.patient.first_name} {self.patient.last_name}, date={self.appointment_date})"

# Step 5: Create a SQLite database in memory (or use a file)
engine = create_engine('sqlite:///hospital.db', echo=True)

# Step 6: Create the tables in the database
Base.metadata.create_all(engine)

# Step 7: Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Step 8: Adding data to the database

# Create doctor and patient instances
doctor1 = Doctor(first_name='John', last_name='Doe', specialty='Cardiology', email='johndoe@hospital.com')
doctor2 = Doctor(first_name='Jane', last_name='Smith', specialty='Neurology', email='janesmith@hospital.com')

patient1 = Patient(first_name='Alice', last_name='Johnson', dob=datetime(1980, 5, 15), email='alice@patient.com')
patient2 = Patient(first_name='Bob', last_name='Williams', dob=datetime(1990, 11, 25), email='bob@patient.com')

# Add the doctor and patient to the session
session.add(doctor1)
session.add(doctor2)
session.add(patient1)
session.add(patient2)

# Commit the session to save the data in the database
session.commit()

# Step 9: Creating appointments
appointment1 = Appointment(doctor_id=doctor1.id, patient_id=patient1.id, appointment_date=datetime(2024, 11, 22, 9, 0))
appointment2 = Appointment(doctor_id=doctor2.id, patient_id=patient2.id, appointment_date=datetime(2024, 11, 22, 10, 0))

# Add appointments to the session and commit
session.add(appointment1)
session.add(appointment2)
session.commit()

# Step 10: Querying the database

# Retrieve all patients and print them
patients = session.query(Patient).all()
for patient in patients:
    print(patient)

# Retrieve all appointments
appointments = session.query(Appointment).all()
for appointment in appointments:
    print(appointment)

# Retrieve appointments for a specific doctor
doctor_appointments = session.query(Appointment).filter(Appointment.doctor_id == doctor1.id).all()
for appointment in doctor_appointments:
    print(appointment)

# Close the session
session.close()
