from hospital import *
import copy
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

simlist = []

self_desk_size = [9,10,11]
inte_desk_size = [19,21,23,25,27]
surg_desk_size = [19,21,23,25,27]
eyes_desk_size = [14,16,18,20,22]
ENT_desk_size = [16,18,20,20,22]
orth_desk_size = [14,16,18,20,22]
ultr_desk_size = [14,16,18,20,22]
bloo_desk_size = [12,14,16,18,20]
endo_desk_size = [10,12,14,16,18]
repo_desk_size = [6,7,8]
phar_desk_size = [20,22,24]
sim_num = 1
for i in range(sim_num):
    for j in range(len(inte_desk_size)):
        patientmodel = Initpatients()
        size = patientmodel[1]
        model = copy.deepcopy(patientmodel[0])
        result = Hospitalsim(copy.deepcopy(model), self_desk_size= self_desk_size[0],
                             inte_desk_size=inte_desk_size[0], surg_desk_size=surg_desk_size[0], eyes_desk_size=eyes_desk_size[0], ENT_desk_size=ENT_desk_size[0], orth_desk_size=orth_desk_size[0],
                             ultr_desk_size=ultr_desk_size[j], bloo_desk_size=bloo_desk_size[j], endo_desk_size=endo_desk_size[j],
                             repo_desk_size=repo_desk_size[1], phar_desk_size=phar_desk_size[1])
        simlist.append(result)


Ws0 = 0
Ws_regi = 0
Ws_inte = 0
Ws_surg = 0
Ws_eyes = 0
Ws_ENT = 0
Ws_orth = 0
Ws_ultr = 0
Ws_bloo = 0
Ws_endo = 0
Ws_repo = 0
Ws_phar = 0
Wq0 = 0
Wq_regi = 0
Wq_inte = 0
Wq_surg = 0
Wq_eyes = 0
Wq_ENT = 0
Wq_orth = 0
Wq_ultr = 0
Wq_bloo = 0
Wq_endo = 0
Wq_repo = 0
Wq_phar = 0
Ls0 = 0
Ls_regi = 0
Ls_inte = 0
Ls_surg = 0
Ls_eyes = 0
Ls_ENT = 0
Ls_orth = 0
Ls_ultr = 0
Ls_bloo = 0
Ls_endo = 0
Ls_repo = 0
Ls_phar = 0
Lq0 = 0
Lq_regi = 0
Lq_inte = 0
Lq_surg = 0
Lq_eyes = 0
Lq_ENT = 0
Lq_orth = 0
Lq_ultr = 0
Lq_bloo = 0
Lq_endo = 0
Lq_repo = 0
Lq_phar = 0

# for diagram
Ws0_d = []
Ws_regi_d = []
Ws_inte_d = []
Ws_surg_d = []
Ws_eyes_d = []
Ws_ENT_d = []
Ws_orth_d = []
Ws_ultr_d = []
Ws_bloo_d = []
Ws_endo_d = []
Ws_repo_d = []
Ws_phar_d = []
Wq0_d = []
Wq_regi_d = []
Wq_inte_d = []
Wq_surg_d = []
Wq_eyes_d = []
Wq_ENT_d = []
Wq_orth_d = []
Wq_ultr_d = []
Wq_bloo_d = []
Wq_endo_d = []
Wq_repo_d = []
Wq_phar_d = []
Ls0_d = []
Ls_regi_d = []
Ls_inte_d = []
Ls_surg_d = []
Ls_eyes_d = []
Ls_ENT_d = []
Ls_orth_d = []
Ls_ultr_d = []
Ls_bloo_d = []
Ls_endo_d = []
Ls_repo_d = []
Ls_phar_d = []
Lq0_d = []
Lq_regi_d = []
Lq_inte_d = []
Lq_surg_d = []
Lq_eyes_d = []
Lq_ENT_d = []
Lq_orth_d = []
Lq_ultr_d = []
Lq_bloo_d = []
Lq_endo_d = []
Lq_repo_d = []
Lq_phar_d = []


for obj in simlist:
    summ0 = 0
    t_regi = 0
    t_inte = 0
    t_surg = 0
    t_eyes = 0
    t_ENT = 0
    t_orth = 0
    t_ultr = 0
    t_bloo = 0
    t_endo = 0
    t_repo = 0
    t_phar = 0
    count0 = 0
    count_regi = 0
    count_inte = 0
    count_surg = 0
    count_eyes = 0
    count_ENT = 0
    count_orth = 0
    count_ultr = 0
    count_bloo = 0
    count_endo = 0
    count_repo = 0
    count_phar = 0


    for patient in obj:
        summ0 = summ0 + patient.t_leave - patient.t_arrive
        count0 += 1
        if patient.flag_regi == 1:
            t_regi = t_regi + patient.t_lea_regi - patient.t_arrive
            count_regi +=1
        if patient.flag_depa == 0:
            t_inte = t_inte + patient.t_lea_depa - patient.t_lea_regi
            count_inte = count_inte + 1
        elif patient.flag_depa == 1:
            t_surg = t_surg + patient.t_lea_depa - patient.t_lea_regi
            count_surg = count_surg + 1
        elif patient.flag_depa == 2:
            t_eyes = t_eyes + patient.t_lea_depa - patient.t_lea_regi
            count_eyes = count_eyes + 1
        elif patient.flag_depa == 3:
            t_ENT = t_ENT + patient.t_lea_depa - patient.t_lea_regi
            count_ENT = count_ENT + 1
        else:
            t_orth = t_orth + patient.t_lea_depa - patient.t_lea_regi
            count_orth = count_orth + 1
        if patient.flag_bloo == 1:
            t_bloo = t_bloo + patient.t_lea_bloo - patient.t_lea_depa
            count_bloo += 1
        if patient.flag_ultr == 1:
            t_ultr = t_ultr + patient.t_lea_ultr - patient.t_lea_bloo
            count_ultr += 1
        if patient.flag_endo == 1:
            t_endo = t_endo + patient.t_lea_endo - patient.t_lea_ultr
            count_endo += 1
        if patient.flag_repo == 1:
            t_repo = t_repo + patient.t_lea_repo - patient.t_lea_endo
            count_repo += 1
        if patient.flag_phar == 1:
            t_phar = t_phar + patient.t_lea_phar - patient.t_lea_repo
            count_phar += 1

    Ws0 = Ws0 + summ0/count0
    Ws_regi = Ws_regi + t_regi / count_regi
    Ws_inte = Ws_inte + t_inte / count_inte
    Ws_surg = Ws_surg + t_surg / count_surg
    Ws_eyes = Ws_eyes + t_eyes / count_eyes
    Ws_ENT = Ws_ENT + t_ENT / count_ENT
    Ws_orth = Ws_orth + t_orth / count_orth

    Ws_ultr = Ws_ultr + t_ultr / count_ultr
    Ws_bloo = Ws_bloo + t_bloo / count_bloo
    Ws_endo = Ws_endo + t_endo / count_endo

    Ws_ultr_d.append(t_ultr / count_ultr)
    Ws_bloo_d.append(t_bloo / count_bloo)
    Ws_endo_d.append(t_endo / count_endo)

    Ws_repo = Ws_repo + t_repo / count_repo
    Ws_phar = Ws_phar + t_phar / count_phar

    Ls0 = Ls0 + summ0 / count0
    Ls_regi = Ls_regi + t_regi / running_time
    Ls_inte = Ls_inte + t_inte / running_time
    Ls_surg = Ls_surg + t_surg / running_time
    Ls_eyes = Ls_eyes + t_eyes / running_time
    Ls_ENT = Ls_ENT + t_ENT / running_time
    Ls_orth = Ls_orth + t_orth / running_time

    Ls_ultr_d.append(t_ultr / running_time)
    Ls_bloo_d.append(t_bloo / running_time)
    Ls_endo_d.append(t_endo / running_time)

    Ls_ultr = Ls_ultr + t_ultr / running_time
    Ls_bloo = Ls_bloo + t_bloo / running_time
    Ls_endo = Ls_endo + t_endo / running_time
    Ls_repo = Ls_repo + t_repo / running_time
    Ls_phar = Ls_phar + t_phar / running_time

for obj in simlist:
    summ0 = 0
    t_regi = 0
    t_inte = 0
    t_surg = 0
    t_eyes = 0
    t_ENT = 0
    t_orth = 0
    t_ultr = 0
    t_bloo = 0
    t_endo = 0
    t_repo = 0
    t_phar = 0
    count0 = 0
    count_regi = 0
    count_inte = 0
    count_surg = 0
    count_eyes = 0
    count_ENT = 0
    count_orth = 0
    count_ultr = 0
    count_bloo = 0
    count_endo = 0
    count_repo = 0
    count_phar = 0
    for patient in obj:
        summ0 = summ0 + patient.t_leave - patient.t_arrive - patient.t_regi_ser - patient.t_depa_ser - patient.t_ultr_ser - patient.t_bloo_ser - patient.t_endo_ser - patient.t_repo_ser - patient.t_phar_ser
        count0 += 1
        if patient.flag_regi == 1:
            t_regi = t_regi + patient.t_lea_regi - patient.t_arrive - patient.t_regi_ser
            count_regi += 1
        if patient.flag_depa == 0:
            t_inte = t_inte + patient.t_lea_depa - patient.t_lea_regi - patient.t_regi_ser - patient.t_depa_ser
            count_inte = count_inte + 1
        elif patient.flag_depa == 1:
            t_surg = t_surg + patient.t_lea_depa - patient.t_lea_regi - patient.t_regi_ser - patient.t_depa_ser
            count_surg = count_surg + 1
        elif patient.flag_depa == 2:
            t_eyes = t_eyes + patient.t_lea_depa - patient.t_lea_regi - patient.t_regi_ser - patient.t_depa_ser
            count_eyes = count_eyes + 1
        elif patient.flag_depa == 3:
            t_ENT = t_ENT + patient.t_lea_depa - patient.t_lea_regi - patient.t_regi_ser - patient.t_depa_ser
            count_ENT = count_ENT + 1
        else:
            t_orth = t_orth + patient.t_lea_depa - patient.t_lea_regi - patient.t_regi_ser - patient.t_depa_ser
            count_orth = count_orth + 1
        if patient.flag_bloo == 1:
            t_bloo = t_bloo + patient.t_lea_bloo - patient.t_lea_depa - patient.t_bloo_ser
            count_bloo += 1
        if patient.flag_ultr == 1:
            t_ultr = t_ultr + patient.t_lea_ultr - patient.t_lea_bloo - patient.t_ultr_ser
            count_ultr += 1
        if patient.flag_endo == 1:
            t_endo = t_endo + patient.t_lea_endo - patient.t_lea_ultr - patient.t_endo_ser
            count_endo += 1
        if patient.flag_repo == 1:
            t_repo = t_repo + patient.t_lea_repo - patient.t_lea_endo - patient.t_repo_ser
            count_repo += 1
        if patient.flag_phar == 1:
            t_phar = t_phar + patient.t_lea_phar - patient.t_lea_repo - patient.t_phar_ser
            count_phar += 1

    Wq0 = Wq0 + summ0 / count0
    Wq_regi = Wq_regi + t_regi / count_regi

    Wq_inte = Wq_inte + t_inte / count_inte
    Wq_surg = Wq_surg + t_surg / count_surg
    Wq_eyes = Wq_eyes + t_eyes / count_eyes
    Wq_ENT = Wq_ENT + t_ENT / count_ENT
    Wq_orth = Wq_orth + t_orth / count_orth

    Wq_ultr_d.append(t_ultr / count_ultr)
    Wq_bloo_d.append(t_bloo / count_bloo)
    Wq_endo_d.append(t_endo / count_endo)

    Wq_ultr = Wq_ultr + t_ultr / count_ultr
    Wq_bloo = Wq_bloo + t_bloo / count_bloo
    Wq_endo = Wq_endo + t_endo / count_endo
    Wq_repo = Wq_repo + t_repo / count_repo
    Wq_phar = Wq_phar + t_phar / count_phar

    Lq0 = Lq0 + summ0 / count0
    Lq_regi = Lq_regi + t_regi / running_time

    Lq_inte = Lq_inte + t_inte / running_time
    Lq_surg = Lq_surg + t_surg / running_time
    Lq_eyes = Lq_eyes + t_eyes / running_time
    Lq_ENT = Lq_ENT + t_ENT / running_time
    Lq_orth = Lq_orth + t_orth / running_time

    Lq_ultr_d.append(t_ultr / running_time)
    Lq_bloo_d.append(t_bloo / running_time)
    Lq_endo_d.append(t_endo / running_time)

    Lq_ultr = Lq_ultr + t_ultr / running_time
    Lq_bloo = Lq_bloo + t_bloo / running_time
    Lq_endo = Lq_endo + t_endo / running_time
    Lq_repo = Lq_repo + t_repo / running_time
    Lq_phar = Lq_phar + t_phar / running_time



print('---------')
print("------Ws")

for i in range(len(Ws_ultr_d)):
    print('      Ws_ultr= ', Ws_ultr_d[i])
    print('      Ws_bloo= ', Ws_bloo_d[i])
    print('      Ws_endo= ', Ws_endo_d[i])
print("------Wq")
for i in range(len(Ws_ultr_d)):
    print('      Wq_ultr= ', Wq_ultr_d[i])
    print('      Wq_bloo= ', Wq_bloo_d[i])
    print('      Wq_endo= ', Wq_endo_d[i])
print("------Ls")
for i in range(len(Ws_ultr_d)):
    print('      Ls_ultr= ', Ls_ultr_d[i])
    print('      Ls_bloo= ', Ls_bloo_d[i])
    print('      Ls_endo= ', Ls_endo_d[i])
print("------Ls")
for i in range(len(Ws_ultr_d)):
    print('      Lq_ultr= ', Lq_ultr_d[i])
    print('      Lq_bloo= ', Lq_bloo_d[i])
    print('      Lq_endo= ', Lq_endo_d[i])


#diagrams
##################
scope = ultr_desk_size
scope1 = bloo_desk_size
scope2 = endo_desk_size

##################
plt.subplot(221)
ax1=plt.gca()
ax1.xaxis.set_major_locator(MultipleLocator(1))
plt.title('Ws')
plt.xlabel(' Examination Size')
plt.ylabel('Value')
plt.plot(scope,Ws_ultr_d,'r', linewidth=1)
plt.plot(scope1,Ws_bloo_d,'r', linewidth=1,c='g')
plt.plot(scope2,Ws_endo_d,'r', linewidth=1,c='b')

####
plt.subplot(222)
ax2=plt.gca()
ax2.xaxis.set_major_locator(MultipleLocator(1))
plt.title('Wq')
plt.xlabel(' Examination Size')
plt.ylabel('Value')
plt.plot(scope,Wq_ultr_d,'r', linewidth=1)
plt.plot(scope1,Wq_bloo_d,'r', linewidth=1,c='g')
plt.plot(scope2,Wq_endo_d,'r', linewidth=1,c='b')

plt.show()
####
plt.subplot(221)
ax3=plt.gca()
ax3.xaxis.set_major_locator(MultipleLocator(1))
plt.title('Ls')
plt.xlabel(' Examination Size')
plt.ylabel('Value')
plt.plot(scope,Ls_ultr_d,'r', linewidth=1)
plt.plot(scope1,Ls_bloo_d,'r', linewidth=1,c='g')
plt.plot(scope2,Ls_endo_d,'r', linewidth=1,c='b')
####
plt.subplot(222)
ax4=plt.gca()
ax4.xaxis.set_major_locator(MultipleLocator(1))
plt.title('Lq')
plt.xlabel(' Examination Size')
plt.ylabel('Value')
plt.plot(scope,Lq_ultr_d,'r', linewidth=1)
plt.plot(scope1,Lq_bloo_d,'r', linewidth=1,c='g')
plt.plot(scope2,Lq_endo_d,'r', linewidth=1,c='b')
plt.show()
###################




