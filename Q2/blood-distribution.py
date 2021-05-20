#blood-distribution
total = 0

blood = [int(blood) for blood in input("Enter the string of blood types available: ").split(" ")]
patients = [int(patient) for patient in input("Enter the string of patients: ").split(" ")]

# Helper function to manage patients helped and blood used for a given blood type and patient
def parser(i, n):
    # print(f"index {i}: {patients[i]}, blood: {blood[n]}")
    if blood[n] == 0: return
    global total
    o_patients = patients[i]
    if blood[n] > o_patients:
        blood[n] -= o_patients
        total += o_patients
        patients[i] = 0
        return
    patients[i] -= blood[n]
    total += blood[n]
    blood[n] = 0
    return


#Loop that iterates in from 7-0 (from most restricted donor to universal donor) of all units of blood available
for i in range(7, -1, -1):
    if i == 0:
        for j in range(8):
            parser(j, i)
    elif i == 1:
        for j in range(1,8,2):
            parser(j, i)
    elif i == 2:
        for j in [2,3,6,7]:
            parser(j, i)
    elif i == 3:
        for j in [3,7]:
            parser(j, i)
    elif i == 4:
        for j in range(4,8):
            parser(j,i)
    elif i == 5:
        for j in [5,7]:
            parser(j,i)
    elif i == 6:
        for j in range(6,8):
            parser(j,i)
    else:
        parser(7, i)

print(total)