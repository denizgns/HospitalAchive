# Author: Deniz Güneş

import random
#### Helper Methods#######
# Your code starts here #
def get_patient_info(command):
    """
    To read patient information in list form
    :param command:
    :return: a list that holds the information about the patient
    """
    patient = command.split(",")
    name = patient[0]
    height = float(patient[1])
    weight = float(patient[2])
    age = int(patient[3])
    gender = patient[4]
    patient[5].upper()
    blood_type = patient[5]

    if not (height > 0.0 and height < 3.0) and weight > 0 and age > 0 and (gender == 'male' or gender == 'female')\
            and (blood_type == 'A' or blood_type == 'AB' or blood_type == 'B' or blood_type == 'O'):
        patient_info = input('Enter command: ')
        patient = patient_info.split(",")
        name = patient[0]
        height = float(patient[1])
        weight = float(patient[2])
        age = int(patient[3])
        gender = patient[4]
        blood_type = str(patient[5]).upper()

    return patient

def print_patient_info(patient):
    """
    print the information about patients in a nice format
    wrote this function to be used when a name is entered
    """
    print(patient[0] + ', height: ' + str(patient[1]) + ', weight: ' + str(patient[2]) +\
          ', age: ' + str(patient[3]) + ', gender: ' + patient[4] + ', blood type: ' + patient[5])

def command_read(command, patient_list):
    """
    To read the commands and handle them as necessary
    """
    while command != 'exit':
        if len(command.split(",")) > 3:
            patient_list.append(get_patient_info(command))
            print('Patient info added successfully')
        elif (command == 'A' or command == 'a' or command == 'B' or command == 'b' or \
              command == 'AB' or command == 'ab' or command == 'o' or command == 'O'):
            command.upper()
            blood_command(command, patient_list)
        elif len(command.split(" ")) == 2:
            name_command(command, patient_list)
        command = input('Enter command: ')
# Your code ends here #

def blood_command(blood_type, patient_list):
    """
    To search for patients of the given blood type when a blood type is entered
    :param blood_type: given blood type by the command
    :param patient_list: the list of patients to search from
    """
    blood_list = []
    for i in range(0, len(patient_list)):
        current_patient = patient_list[i]
        if current_patient[5] == blood_type:
            blood_list.append(current_patient)

    if blood_list == []:
        print('No patient with such blood type')
    else:
        ran = random.randint(0, len(blood_list))
        current_patient = blood_list[ran]
        print('Randomly selected patient: ' + current_patient[0])


def name_command(name, patient_list):
    for i in range(0, len(patient_list)):
        patient = patient_list[i]
        if patient[0] == name:
           ispresent = 'yes'

    if ispresent != 'yes':
        print('No patient with such name')
    elif ispresent == 'yes':
        found = 0
        i = 0
        while found == 0:
            test = patient_list[i]
            if test[0] == name:
                print_patient_info(test)
                found = 1
            else:
                i += 1


def main():
    """
    This program handles addition, search of patient information
    :return: None
    """
    # Your code starts here #
    patient_list = []
    command = input('Enter patient:')
    command_read(command, patient_list)
    # Your code ends here #

if __name__ == "__main__":
    main()
