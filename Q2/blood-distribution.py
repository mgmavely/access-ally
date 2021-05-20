#blood-distribution
total = 0

blood = [int(blood) for blood in input("Enter the string of blood types available: ").split(" ")]
patients = [int(patient) for patient in input("Enter the string of patients: ").split(" ")]


def parser(i, n):
    print(f"index {i}: {patients[i]}, blood: {blood[n]}")
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


for i in range(7, -1, -1):
    print(total)
    if i == 0:
        parser(0, i)
        parser(1, i)
        parser(2, i)
        parser(3, i)
        parser(4, i)
        parser(5, i)
        parser(6, i)
        parser(7, i)
    elif i == 1:
        parser(1, i)
        parser(3, i)
        parser(5, i)
        parser(7, i)
    elif i == 2:
        parser(2, i)
        parser(3, i)
        parser(6, i)
        parser(7, i)
    elif i == 3:
        parser(3, i)
        parser(7, i)
    elif i == 4:
        parser(4, i)
        parser(5, i)
        parser(6, i)
        parser(7, i)
    elif i == 5:
        parser(5, i)
        parser(7, i)
    elif i == 6:
        parser(6, i)
        parser(7, i)
    else:
        parser(7, i)

print(total)
print(blood)