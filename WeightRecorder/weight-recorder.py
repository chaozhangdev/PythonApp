# This is a record for weight of chao and qi
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd  

class month:
    def __init__(self, name, day, chao, qi):
        self.name = "May"
        self.day = day
        self.chao = chao
        self.qi = qi

def show(m, who, start, end, month, name):
    plt.plot(m.day[start:end],who[start:end], color='b')
    plt.ylabel("Weight / kg")
    plt.xlabel("Days")
    plt.title(name + ' - Weight - ' + month + " , 2019")
    plt.show()

def show_total(var, name):
    plt.plot(var, color='r')
    plt.title(name + ' - Weight - 2019')
    plt.ylabel("Weight / kg")
    plt.xlabel("Days")
    plt.show()

# 2019 May
may = month('May', np.arange(32), np.zeros(32), np.zeros(32))
may.chao[18] = 93.5 ; may.qi[18] = 67.1
may.chao[19] = 93.1 ; may.qi[19] = 66.8
may.chao[20] = 92.4 ; may.qi[20] = 66.9
may.chao[21] = 92.5 ; may.qi[21] = 66.9
may.chao[22] = 92.5 ; may.qi[22] = 66.8
may.chao[23] = 92.0 ; may.qi[23] = 66.4
may.chao[24] = 91.9 ; may.qi[24] = 66.1
may.chao[25] = 92.0 ; may.qi[25] = 66.15
may.chao[26] = 91.5 ; may.qi[26] = 66.2
may.chao[27] = 90.3 ; may.qi[27] = 66.3

# 2019 June
june = month('June', np.arange(32), np.zeros(32), np.zeros(32))
june.chao[1] = 92.2 ; june.qi[1] = 66
june.chao[2] = 92.3 ; june.qi[2] = 66.5 ########
june.chao[3] = 92.5 ; june.qi[3] = 67 ########
june.chao[4] = 92.7 ; june.qi[4] = 67.5 ########
june.chao[5] = 92.8 ; june.qi[5] = 68
june.chao[6] = 92.9 ; june.qi[6] = 68 ########
june.chao[7] = 93 ; june.qi[7] = 68
june.chao[8] = 94.5 ; june.qi[8] = 68
june.chao[9] = 94 ; june.qi[9] = 67.7 ########
june.chao[10] = 93.6 ; june.qi[10] = 67.3
june.chao[11] = 92.5 ; june.qi[11] = 67
june.chao[12] = 92.3 ; june.qi[12] = 66.6
june.chao[13] = 91.9 ; june.qi[13] = 66.8
june.chao[14] = 92.2 ; june.qi[14] = 66.8 ########
june.chao[15] = 92.5 ; june.qi[15] = 66.8
june.chao[16] = 92.3 ; june.qi[16] = 66.4
june.chao[17] = 92.2 ; june.qi[17] = 67
june.chao[18] = 92.0 ; june.qi[18] = 66.7
june.chao[19] = 92.0 ; june.qi[19] = 67.3

if __name__ == "__main__":

    # show(may, may.chao, 18, 28, "May", "Chao")
    # show(may, may.qi, 18, 28, "May", "Qi")   
    show(june, june.chao, 1, 20, "June", "Chao")
    show(june, june.qi, 1, 20, "June", "Qi")
    # chao_total = np.append(may.chao[18:27],june.chao[1:19])
    # qi_total = np.append(may.qi[18:27],june.qi[1:19])
    # show_total(chao_total, "Chao")
    # show_total(qi_total, "Qi")





