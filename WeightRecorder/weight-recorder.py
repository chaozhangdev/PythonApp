# This is a record for weight of chao and qi
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

class month:
    def __init__(self, name, chao, qi):
        self.name = name
        self.chao = chao
        self.qi = qi

def show(var, m_name, name):
    plt.plot(var, color='r')
    plt.title('2019  '+ m_name + ' - ' + name + "'s Weight")
    plt.ylabel("Weight / kg")
    plt.xlabel("Days")
 

def show_total(var, name):
    plt.plot(var, color='blue')
    plt.title('2019 ' + name + "'s Weight - Total")
    plt.ylabel("Weight / kg")
    plt.xlabel("Days")


if __name__ == "__main__":

    # weight record 
    may = month('May',  np.zeros(32), np.zeros(32))
    may.chao = [93.5, 93.1, 93.1, 92.5, 92.5, 92.0, 91.9, 92.0, 91.5, 90.3 ]
    may.qi = [67.1, 66.8, 66.9, 66.9, 66.8, 66.4, 66.1, 66.15, 66.2, 66.3]

    june = month('June',  np.zeros(32), np.zeros(32))
    june.chao = [92.2, 92.8, 93, 94.5, 93.6, 92.5, 92.3, 91.9, 92.5, 92.3, 92.2, 92.0, 92.0, 
    92.0, 91, 91.1, 91.2, 91.7, 91.8, 91.2, 90.8, 90.9]
    june.qi = [66, 68, 68, 68, 67.3, 67, 66.6, 66.8, 66.8, 66.4, 67, 66.7, 67.3, 66.6, 66.5, 66.7, 66.6, 66.6, 66.2]

    july = month('July',  np.zeros(32), np.zeros(32))
    july.chao = [90.3, 89.5, 90.2, 90.8, 91, 90.5, 90.2, 90.0, 89.8, 89.2, 90.5, 90.0, 89.8, 89.7, 90.2, 89.3, 89.4, 89.9, 89.5, 90.0, 90.0, 89.9, 90.0, 90.3]
    july.qi = [65.9, 65.8, 66.1, 66.5, 66.2, 66.2, 65.6, 65.6, 65.5, 65.2, 65.4, 65.6, 65.9, 66.5, 65.5, 65.6, 64.7, 64.6, 64.9, 64.4, 64.9, 65.4]

    chao_total = np.concatenate((may.chao, june.chao, july.chao), axis=0)
    qi_total = np.concatenate((may.qi, june.qi, july.qi), axis=0)

    # weight display
    plt.subplot(211)
    show_total(chao_total, "Chao")
    plt.subplots_adjust(wspace=0.6, hspace=0.6)
    plt.subplot(234)
    show(may.chao, may.name, "Chao")
    plt.subplot(235)
    show(june.chao, june.name, "Chao")
    plt.subplot(236)
    show(july.chao, july.name, "Chao")
    plt.show()

    plt.subplot(211)
    show_total(qi_total, "Qi")
    plt.subplots_adjust(wspace=0.6, hspace=0.6)
    plt.subplot(234)
    show(may.qi, may.name, "Qi")
    plt.subplot(235)
    show(june.qi, june.name, "Qi")
    plt.subplot(236)
    show(july.qi, july.name, "Qi")

    plt.show()

