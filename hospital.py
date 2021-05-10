import random

running_time = 3600 * 4
la = 0.33
mu_self = 0.0084
mu_inte = 0.0026
mu_surg = 0.0030
mu_eyes = 0.0023
mu_ENT = 0.0023
mu_orth = 0.0033
mu_ultr = 0.0056
mu_bloo = 0.0083
mu_endo = 0.0032
mu_phar = 0.0084
mu_repo = 0.0165
gener_ultr_time = 600
gener_bloo_time = 600
gener_endo_time = 600
rate_self_help = 0.05
rate_internal_medicine = 0.27
rate_surgery = 0.50
rate_eyes = 0.6667
rate_ENT = 0.8333
rate_orthopedics = 1.0
rate_ultrasonic_examination = 0.65
rate_blood_detection = 0.75
rate_endoscopy = 0.43
rate_pharmacy = 0.99


class patient(object):
    flag_regi = 0  # 0 for no registration, 1 for self-help machines
    flag_depa = 0  # 0 for internal medicine department, 1 for surgery department,
                    # 2 for ophthalmology (eyes) department, 3 for E.N.T department, 4 for orthopedics department
    flag_ultr = 0  # 0 if patient dose not need a ultrasonic examination, otherwise 1
    flag_bloo = 0  # 0 if patient dose not need a blood detection, otherwise 1
    flag_endo = 0  # 0 if patient dose not need a endoscopy, otherwise 1
    flag_repo = 0  # 0 if patient dose not print an examination report, otherwise 1
    flag_phar = 0  # 0 if patient dose not need any medication, otherwise 1
    t_arrive = 0.00  # arrival time
    t_lea_regi = 0.00  # time of leaving registration office
    t_lea_depa = 0.00  # time of leaving internal medicine or surgery department
    t_lea_ultr = 0.00  # time of finishing ultrasonic examination
    t_lea_bloo = 0.00  # time of finishing blood detection
    t_lea_endo = 0.00  # time of finishing endoscopy
    t_lea_repo = 0.00  # time of leaving report printer
    t_lea_phar = 0.00  # time of leaving pharmacy
    t_leave = 0.00  # leave time
    t_regi_ser = 0.00  # service time of registration
    t_depa_ser = 0.00  # service time of department
    t_ultr_ser = 0.00  # service time of ultrasonic examination
    t_bloo_ser = 0.00  # service time of blood detection
    t_endo_ser = 0.00  # service time of endoscopy
    t_repo_ser = 0.00  # service time of report printer
    t_phar_ser = 0.00  # service time of pharmacy


'''
def min_leave(server_desk_num):
    num = server_plat[0]
    index = 0
    for k in range(1, len(server_plat)):
        if num > server_plat[k]:
            index = k
            num = server_plat[k]
    return num, index
'''


def min_len(server_desk_num):
    num = len(server_desk_num[0])
    index = 0
    for k in range(1, len(server_desk_num)):
        if num > len(server_desk_num[k]):
            index = k
            num = len(server_desk_num[k])
    return index

def min_len_num(server_desk_num):
    num = len(server_desk_num[0])
    index = 0
    for k in range(1, len(server_desk_num)):
        if num > len(server_desk_num[k]):
            index = k
            num = len(server_desk_num[k])
    return num


def max_len(server_plat):
    num = len(server_plat[0])
    for k in range(1, len(server_plat)):
        if num < len(server_plat[k]):
            num = len(server_plat[k])
    return num


def Initpatients():
    # initialize and arrive time
    allpatient = []
    allpatient.append(patient())
    t = 0.0
    size = 1

    while (True):
        temp = patient()
        if (t < running_time):
            t = t + random.expovariate(la)
            temp.t_arrive = t
            size += 1
            # set flags and service times
            k1 = random.random()
            if k1 < rate_self_help:
                temp.flag_regi = 1
                temp.t_regi_ser = random.expovariate(mu_self)
            k2 = random.random()
            if k2 >=0 and k2 < rate_internal_medicine:
                temp.flag_depa = 0
                temp.t_depa_ser = random.expovariate(mu_inte)
            elif k2 >= rate_internal_medicine and k2 < rate_surgery:
                temp.flag_depa = 1
                temp.t_depa_ser = random.expovariate(mu_surg)
            elif k2 >= rate_surgery and k2 < rate_eyes:
                temp.flag_depa = 2
                temp.t_depa_ser = random.expovariate(mu_eyes)
            elif k2 >= rate_eyes and k2 <rate_ENT:
                temp.flag_depa = 3
                temp.t_depa_ser = random.expovariate(mu_ENT)
            else:
                temp.flag_depa = 4
                temp.t_depa_ser = random.expovariate(mu_orth)
            k3 = random.random()
            if k3 < rate_ultrasonic_examination and temp.flag_depa != 2 and temp.flag_depa != 3:
                temp.flag_ultr = 1
                temp.t_ultr_ser = 1/mu_ultr
            else:
                temp.flag_ultr = 0
            k4 = random.random()
            if k4 < rate_blood_detection and temp.flag_depa != 2 and temp.flag_depa != 3:
                temp.flag_bloo = 1
                temp.t_bloo_ser = random.expovariate(mu_bloo)
            else:
                temp.flag_bloo = 0
            k5 = random.random()
            if k5 < rate_endoscopy and temp.flag_depa != 2 and temp.flag_depa != 3 and temp.flag_depa != 4:
                temp.flag_endo = 1
                temp.t_endo_ser = random.expovariate(mu_endo)
            else:
                temp.flag_endo = 0
            if temp.flag_ultr == 1 or temp.flag_bloo == 1 or temp.flag_endo == 1:
                temp.flag_repo = 1
                temp.t_repo_ser = 1/mu_repo
            k6 = random.random()
            if k6 < rate_pharmacy:
                temp.flag_phar = 1
                temp.t_phar_ser = random.expovariate(mu_phar)
            else:
                temp.flag_phar = 0

            allpatient.append(temp)
        else:
            break

    return allpatient, size


def Hospitalsim(allpatient, self_desk_size, inte_desk_size, surg_desk_size, eyes_desk_size, ENT_desk_size, orth_desk_size,
                ultr_desk_size, bloo_desk_size, endo_desk_size, repo_desk_size, phar_desk_size):
    ###############################################################
    self_desk = []
    inte_desk = []
    surg_desk = []
    eyes_desk = []
    ENT_desk  = []
    orth_desk = []
    ultr_desk = []
    bloo_desk = []
    endo_desk = []
    repo_desk = []
    phar_desk = []

    for i in range(0, self_desk_size):
        self_desk.append([])
    ###############################################################
    # time of leaving registration desk
    for patient in allpatient:
        if patient.flag_regi == 0:
            patient.t_lea_regi = patient.t_arrive
        # self-help machines
        else:
            now_time = patient.t_arrive
            for queue in self_desk:
                if len(queue) != 0:
                    for obj in queue:
                        if obj.t_lea_regi <= now_time:
                            queue.remove(obj)

            index = min_len(self_desk)
            self_desk[index].append(patient)

            if len(self_desk[index]) == 1:
                patient.t_lea_regi = patient.t_arrive + patient.t_regi_ser
                patient.t_leave = patient.t_lea_regi
            else:
                patient.t_lea_regi = self_desk[index][len(self_desk[index]) - 2].t_lea_regi + patient.t_regi_ser
                patient.t_leave = patient.t_lea_regi

    ###############################################################
    # time of leaving department
    '''
    size = len(allpatient)
    for i in range(size):
        for j in range(size - 1 - i):
            if allpatient[j].t_lea_regi > allpatient[j + 1].t_lea_regi:
                temp = allpatient[j + 1]
                allpatient[j + 1] = allpatient[j]
                allpatient[j] = temp
    '''

    for i in range(0, inte_desk_size):
        inte_desk.append([])
    for i in range(0, surg_desk_size):
        surg_desk.append([])
    for i in range(0, eyes_desk_size):
        eyes_desk.append([])
    for i in range(0, ENT_desk_size):
        ENT_desk.append([])
    for i in range(0, orth_desk_size):
        orth_desk.append([])

    for patient in allpatient:
        # internal medicine department
        if patient.flag_depa == 0:
            process = Intedepa(patient, inte_desk, inte_desk_size)
            patient = process[0]
            inte_desk = process[1]
        # surgery department
        elif patient.flag_depa == 1:
            process = Surgdepa(patient, surg_desk, surg_desk_size)
            patient = process[0]
            surg_desk = process[1]
        # eyes department
        elif patient.flag_depa == 2:
            process = Eyesdepa(patient, eyes_desk, eyes_desk_size)
            patient = process[0]
            eyes_desk = process[1]
        # ENT department
        elif patient.flag_depa == 3:
            process = ENTdepa(patient, ENT_desk, ENT_desk_size)
            patient = process[0]
            ENT_desk = process[1]
        # orthopedics department
        else:
            process = Orthdepa(patient, orth_desk, orth_desk_size)
            patient = process[0]
            orth_desk = process[1]

    ###############################################################
    # time of finishing blood detection
    #'''
    size = len(allpatient)
    for i in range(size):
        for j in range(size - 1 - i):
            if allpatient[j].t_lea_depa > allpatient[j+1].t_lea_depa:
                temp = allpatient[j+1]
                allpatient[j + 1] = allpatient[j]
                allpatient[j] = temp
    #'''
    for i in range(0, bloo_desk_size):
        bloo_desk.append([])

    for patient in allpatient:
        if patient.flag_bloo == 0:
            patient.t_lea_bloo = patient.t_lea_depa
        else:
            process = Blood(patient, bloo_desk)
            patient = process[0]
            bloo_desk = process[1]

    ###############################################################
    # time of finishing ultrasonic examination
    # '''
    size = len(allpatient)
    for i in range(size):
        for j in range(size - 1 - i):
            if allpatient[j].t_lea_bloo > allpatient[j + 1].t_lea_bloo:
                temp = allpatient[j + 1]
                allpatient[j + 1] = allpatient[j]
                allpatient[j] = temp
    # '''
    for i in range(0, ultr_desk_size):
        ultr_desk.append([])

    for patient in allpatient:
        if patient.flag_ultr == 0:
            patient.t_lea_ultr = patient.t_lea_bloo
        else:
            process = Ultrasonic(patient, ultr_desk, ultr_desk_size)
            patient = process[0]
            ultr_desk = process[1]



    ###############################################################
    # time of finishing endoscopy
    #'''
    size = len(allpatient)
    for i in range(size):
        for j in range(size - 1 - i):
            if allpatient[j].t_lea_ultr > allpatient[j + 1].t_lea_ultr:
                temp = allpatient[j + 1]
                allpatient[j + 1] = allpatient[j]
                allpatient[j] = temp
    #'''

    for i in range(0, endo_desk_size):
        endo_desk.append([])

    for patient in allpatient:
        if patient.flag_endo == 0:
            patient.t_lea_endo = patient.t_lea_ultr
        else:
            now_time = patient.t_lea_ultr
            for queue in endo_desk:
                if len(queue) != 0:
                    for obj in queue:
                        if obj.t_lea_endo <= now_time:
                            queue.remove(obj)

            index = random.randint(0, endo_desk_size - 1)
            endo_desk[index].append(patient)

            if len(endo_desk[index]) == 1:
                patient.t_lea_endo = now_time + patient.t_endo_ser
                patient.t_leave = patient.t_lea_endo
            else:
                patient.t_lea_endo = endo_desk[index][len(endo_desk[index]) - 2].t_lea_endo + patient.t_endo_ser
                patient.t_leave = patient.t_lea_endo

    ###############################################################
    # time of print examination report
    #'''
    size = len(allpatient)
    for i in range(size):
        for j in range(size - 1 - i):
            if allpatient[j].t_lea_endo > allpatient[j + 1].t_lea_endo:
                temp = allpatient[j + 1]
                allpatient[j + 1] = allpatient[j]
                allpatient[j] = temp
    #'''

    for i in range(0, repo_desk_size):
        repo_desk.append([])

    for patient in allpatient:
        if patient.flag_repo == 0:
            patient.t_lea_repo = patient.t_lea_endo
        else:
            if patient.flag_endo == 1:
                now_time = patient.t_lea_endo + gener_endo_time
            elif patient.flag_ultr == 1:
                now_time = patient.t_lea_endo + gener_ultr_time
            else:
                now_time = patient.t_lea_endo + gener_bloo_time
            for queue in repo_desk:
                if len(queue) != 0:
                    for obj in queue:
                        if obj.t_lea_repo <= now_time:
                            queue.remove(obj)

            index = min_len(repo_desk)
            repo_desk[index].append(patient)

            if len(repo_desk[index]) == 1:
                patient.t_lea_repo = now_time + patient.t_repo_ser
                patient.t_leave = patient.t_lea_repo
            else:
                patient.t_lea_repo = repo_desk[index][len(repo_desk[index]) - 2].t_lea_repo + patient.t_repo_ser
                patient.t_leave = patient.t_lea_repo

    ###############################################################
    # time of leaving pharmacy
    size = len(allpatient)
    for i in range(size):
        for j in range(size - 1 - i):
            if allpatient[j].t_lea_repo > allpatient[j + 1].t_lea_repo:
                temp = allpatient[j + 1]
                allpatient[j + 1] = allpatient[j]
                allpatient[j] = temp

    for i in range(0, phar_desk_size):
        phar_desk.append([])

    for patient in allpatient:
        if patient.flag_phar == 0:
            patient.t_lea_phar = patient.t_lea_repo
        else:
            now_time = patient.t_lea_repo
            for queue in phar_desk:
                if len(queue) != 0:
                    for obj in queue:
                        if obj.t_lea_phar <= now_time:
                            queue.remove(obj)

            index = min_len(phar_desk)
            phar_desk[index].append(patient)

            if len(phar_desk[index]) == 1:
                patient.t_lea_phar = patient.t_lea_repo + patient.t_phar_ser
                patient.t_leave = patient.t_lea_phar
            else:
                patient.t_lea_phar = phar_desk[index][len(phar_desk[index]) - 2].t_lea_phar + patient.t_phar_ser
                patient.t_leave = patient.t_lea_phar
    return allpatient


def Intedepa(patient, inte_desk, inte_desk_size):
    now_time = patient.t_lea_regi
    for queue in inte_desk:
        if len(queue) != 0:
            for obj in queue:
                if obj.t_lea_depa <= now_time:
                    queue.remove(obj)

    index = random.randint(0, inte_desk_size - 1)
    inte_desk[index].append(patient)

    if len(inte_desk[index]) == 1:
        patient.t_lea_depa = patient.t_lea_regi + patient.t_depa_ser
        patient.t_leave = patient.t_lea_depa
    else:
        patient.t_lea_depa = inte_desk[index][len(inte_desk[index]) - 2].t_lea_depa + patient.t_depa_ser
        patient.t_leave = patient.t_lea_depa

    return patient, inte_desk

def Surgdepa(patient, surg_desk, surg_desk_size):
    now_time = patient.t_lea_regi
    for queue in surg_desk:
        if len(queue) != 0:
            for obj in queue:
                if obj.t_lea_depa <= now_time:
                    queue.remove(obj)

    index = random.randint(0, surg_desk_size - 1)
    surg_desk[index].append(patient)

    if len(surg_desk[index]) == 1:
        patient.t_lea_depa = patient.t_lea_regi + patient.t_depa_ser
        patient.t_leave = patient.t_lea_depa
    else:
        patient.t_lea_depa = surg_desk[index][len(surg_desk[index]) - 2].t_lea_depa + patient.t_depa_ser
        patient.t_leave = patient.t_lea_depa

    return patient, surg_desk

def Eyesdepa(patient, eyes_desk, eyes_desk_size):
    now_time = patient.t_lea_regi
    for queue in eyes_desk:
        if len(queue) != 0:
            for obj in queue:
                if obj.t_lea_depa <= now_time:
                    queue.remove(obj)

    index = random.randint(0, eyes_desk_size - 1)
    eyes_desk[index].append(patient)

    if len(eyes_desk[index]) == 1:
        patient.t_lea_depa = patient.t_lea_regi + patient.t_depa_ser
        patient.t_leave = patient.t_lea_depa
    else:
        patient.t_lea_depa = eyes_desk[index][len(eyes_desk[index]) - 2].t_lea_depa + patient.t_depa_ser
        patient.t_leave = patient.t_lea_depa

    return patient, eyes_desk

def ENTdepa(patient, ENT_desk, ENT_desk_size):
    now_time = patient.t_lea_regi
    for queue in ENT_desk:
        if len(queue) != 0:
            for obj in queue:
                if obj.t_lea_depa <= now_time:
                    queue.remove(obj)

    index = random.randint(0, ENT_desk_size - 1)
    ENT_desk[index].append(patient)

    if len(ENT_desk[index]) == 1:
        patient.t_lea_depa = patient.t_lea_regi + patient.t_depa_ser
        patient.t_leave = patient.t_lea_depa
    else:
        patient.t_lea_depa = ENT_desk[index][len(ENT_desk[index]) - 2].t_lea_depa + patient.t_depa_ser
        patient.t_leave = patient.t_lea_depa

    return patient, ENT_desk

def Orthdepa(patient, orth_desk, orth_desk_size):
    now_time = patient.t_lea_regi
    for queue in orth_desk:
        if len(queue) != 0:
            for obj in queue:
                if obj.t_lea_depa <= now_time:
                    queue.remove(obj)

    index = random.randint(0, orth_desk_size - 1)
    orth_desk[index].append(patient)

    if len(orth_desk[index]) == 1:
        patient.t_lea_depa = patient.t_lea_regi + patient.t_depa_ser
        patient.t_leave = patient.t_lea_depa
    else:
        patient.t_lea_depa = orth_desk[index][len(orth_desk[index]) - 2].t_lea_depa + patient.t_depa_ser
        patient.t_leave = patient.t_lea_depa

    return patient, orth_desk

def Ultrasonic(patient, ultr_desk, ultr_desk_size):
    now_time = patient.t_lea_bloo
    for queue in ultr_desk:
        if len(queue) != 0:
            for obj in queue:
                if obj.t_lea_ultr <= now_time:
                    queue.remove(obj)

    index = random.randint(0, ultr_desk_size - 1)
    ultr_desk[index].append(patient)

    if len(ultr_desk[index]) == 1:
        patient.t_lea_ultr = patient.t_lea_bloo + patient.t_ultr_ser
        patient.t_leave = patient.t_lea_ultr
    else:
        patient.t_lea_ultr = ultr_desk[index][len(ultr_desk[index]) - 2].t_lea_ultr + patient.t_ultr_ser
        patient.t_leave = patient.t_lea_ultr

    return patient, ultr_desk

def Blood(patient, bloo_desk):
    now_time = patient.t_lea_depa
    for queue in bloo_desk:
        if len(queue) != 0:
            for obj in queue:
                if obj.t_lea_bloo <= now_time:
                    queue.remove(obj)

    index = min_len(bloo_desk)
    bloo_desk[index].append(patient)

    if len(bloo_desk[index]) == 1:
        patient.t_lea_bloo = patient.t_lea_depa + patient.t_bloo_ser
        patient.t_leave = patient.t_lea_bloo
    else:
        patient.t_lea_bloo = bloo_desk[index][len(bloo_desk[index]) - 2].t_lea_bloo + patient.t_bloo_ser
        patient.t_leave = patient.t_lea_bloo

    return patient, bloo_desk
###############################################################
# test
'''
count = 0
for obj in allpeople:
    if obj.choice == 1:
        count = count + 1
print(count/size)
print(min_len(server_plat1))
for obj in allpeople:
    if obj.choice == 1:
        print(obj.t_arrive1,'-',obj.t_leave1,':',obj.t_leave1 - obj.t_arrive1 - obj.t_serve1,':',obj.t_serve1)
    #else:
       # print(obj.t_arrive2,'-',obj.t_leave2,':',obj.t_leave2 - obj.t_arrive2 - obj.t_serve2)
'''
