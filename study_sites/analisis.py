import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import copy
import os

def shallow(df2):
    filtered_df2 = df2[df2['depth'].isin([-1, -3, -5])]
    return filtered_df2

def compara(A,labelA,B,labelB,inicio,fin):

    fig= plt.subplots(figsize=(8, 10))
    plt.subplot(3, 1, 1)
    plt.plot(A.loc[A.depth == -1,'linear_appres_cal'][inicio:fin],'*',color='red',label=labelA)
    plt.plot(B.loc[B.depth == -1,'linear_appres_cal'][inicio:fin],'*',color='blue', label=labelB)
    plt.xlabel('Data number')
    plt.ylabel('Linear resistivity [Ohm*m]')
    plt.title('z=-1')
    plt.legend()
    
    plt.subplot(3, 1, 2)
    plt.plot(A.loc[A.depth == -3,'linear_appres_cal'][inicio:fin],'*',color='red',label=labelA)
    plt.plot(B.loc[B.depth == -3,'linear_appres_cal'][inicio:fin],'*',color='blue', label=labelB)
    plt.xlabel('Data number')
    plt.ylabel('Linear resistivity [Ohm*m]')
    plt.title('z=-3')
    plt.legend()
    
    plt.subplot(3, 1, 3)
    plt.plot(A.loc[A.depth == -5,'linear_appres_cal'][inicio:fin],'*',color='red',label=labelA)
    plt.plot(B.loc[B.depth == -5,'linear_appres_cal'][inicio:fin],'*',color='blue', label=labelB)
    plt.xlabel('Data number')
    plt.ylabel('Linear resistivity [Ohm*m]')
    plt.title('z=-5')
    plt.legend()
    
    plt.tight_layout()

    plt.show()
    
def region_salada(data):
    easting_condition = (data['easting'] > 500) & (data['easting'] < 700)
    northing_condition = (data['northing'] > 500) & (data['northing'] < 800)
    depth_condition = data['depth'] == -3
    # Apply the filter
    filtered_data = data[easting_condition & northing_condition & depth_condition]
    return filtered_data 
    
def restas_cocientes(A, B, labelA, labelB,overall_title):
   
    fig, axs = plt.subplots(4, 2, figsize=(8, 10))
    fig.tight_layout(pad=3.0)

    # Set common x-axis limits for diferencia histograms
    diferencia_xlim = (min(A.diferencia.min(), B.diferencia.min()), max(A.diferencia.max(), B.diferencia.max()))

    # Plot diferencia for A
    axs[0, 0].plot(A.diferencia, '.', color='lightblue', label='resta')
    axs[0, 0].set_title('diferencia ' + labelA)
    axs[0, 0].set_xlabel('Data number')
    axs[0, 0].set_ylabel('Linear resistivity [Ohm*m]')

    # Histogram for diferencia in A
    axs[0, 1].hist(A.diferencia)
    axs[0, 1].set_title('Histogram')
    axs[0, 1].set_xlabel('Value')
    axs[0, 1].set_ylabel('Frequency')
    axs[0, 1].set_xlim(diferencia_xlim)

    # Plot diferencia for B
    axs[1, 0].plot(B.diferencia, '.', color='black', label='resta')
    axs[1, 0].set_title('diferencia ' + labelB)
    axs[1, 0].set_xlabel('Data number')
    axs[1, 0].set_ylabel('Linear resistivity [Ohm*m]')

    # Histogram for diferencia in B
    axs[1, 1].hist(B.diferencia)
    axs[1, 1].set_title('Histogram')
    axs[1, 1].set_xlabel('Value')
    axs[1, 1].set_ylabel('Frequency')
    axs[1, 1].set_xlim(diferencia_xlim)

    # Set common x-axis limits for cociente histograms
    cociente_xlim = (min(A.cociente.min(), B.cociente.min()), max(A.cociente.max(), B.cociente.max()))

    # Plot cociente for A
    axs[2, 0].plot(A.cociente, '.', color='lightblue', label='cociente')
    axs[2, 0].set_title('cociente ' + labelA)
    axs[2, 0].set_xlabel('Data number')
    axs[2, 0].set_ylabel('Linear resistivity [Ohm*m]')


    # Histogram for cociente in A
    axs[2, 1].hist(A.cociente)
    axs[2, 1].set_title('Histogram')
    axs[2, 1].set_xlabel('Value')
    axs[2, 1].set_ylabel('Frequency')
    axs[2, 1].set_xlim(cociente_xlim)

    # Plot cociente for B
    axs[3, 0].plot(B.cociente, '.', color='black', label='cociente')
    axs[3, 0].set_title('cociente ' + labelB)
    axs[3, 0].set_xlabel('Data number')
    axs[3, 0].set_ylabel('Linear resistivity [Ohm*m]')
    
    # Histogram for cociente in B
    axs[3, 1].hist(B.cociente)
    axs[3, 1].set_title('Histogram')
    axs[3, 1].set_xlabel('Value')
    axs[3, 1].set_ylabel('Frequency')
    axs[3, 1].set_xlim(cociente_xlim)
    fig.suptitle(overall_title)
    plt.tight_layout()
    plt.show()
    


def filter_based_rectangulo_min_max(df):

    filtered_df = df[~((df['diferencia'] > -0.0493631041) & (df['diferencia'] < 0.1255040585)) & 
                 ~((df['cociente'] > 0.8689604293) & (df['cociente'] < 1.6218100974))]
    return filtered_df



# First Models
# model_7399 = pd.read_csv('to_voxler_7399.csv') #smoothest b=0.1
# model_6945 = pd.read_csv('to_voxler_6945.csv') #medium b=0.01
# model_9403 = pd.read_csv('to_voxler_9403.csv') #rough b=0.001

# model_compared_7399_6945=model_7399
# model_compared_6945_9403=model_6945

# model_compared_7399_6945['diff']= model_7399['linear_appres_cal']-model_6945['linear_appres_cal']
# model_compared_7399_6945= model_compared_7399_6945.drop(columns=['log_appres_cal','linear_appres_cal'])
# model_compared_7399_6945.to_csv('compared_7399_6945.csv')

# model_compared_6945_9403['diff']= model_6945['linear_appres_cal']-model_9403['linear_appres_cal']
# model_compared_6945_9403= model_compared_6945_9403.drop(columns=['log_appres_cal','linear_appres_cal'])
# model_compared_6945_9403.to_csv('compared_6945_9403.csv')

# model_7399.head()
# model_6945.head()
# model_9403.head()


# ##  Parra

# # Comparar sin constricciones vs constricciones en puros ojos
# model_compared_12410_12422=model_12443.copy()
# model_compared_12410_12422['diff']= model_12410['linear_appres_cal']-model_12422['linear_appres_cal']
# model_compared_12410_12422['cociente']= (model_12410['linear_appres_cal']/model_12422['linear_appres_cal'])*100
# model_compared_12410_12422= model_compared_12410_12422.drop(columns=['log_appres_cal','linear_appres_cal'])
# model_compared_12410_12422.to_csv('/home/m/Documents/cluster_resultados/perl5/ptm_intel/ptm_tt/compared_12410_12422.csv')

# #Comparar sin constricciones vs constricciones en mar y ojos
# model_compared_12410_12443=model_12443.copy()
# model_compared_12410_12443['diff']= model_12410['linear_appres_cal']-model_12422['linear_appres_cal']
# model_compared_12410_12443['cociente']= (model_12410['linear_appres_cal']/model_12422['linear_appres_cal'])*100
# model_compared_12410_12443= model_compared_12410_12443.drop(columns=['log_appres_cal','linear_appres_cal'])
# model_compared_12410_12443.to_csv('/home/m/Documents/cluster_resultados/perl5/ptm_intel/ptm_tt/compared_12410_12443.csv')

# #Comparar constricciones en ojos y mar vs solo en ojos
# model_compared_12443_12422=model_12443.copy()
# model_compared_12443_12422['diff']= model_12410['linear_appres_cal']-model_12422['linear_appres_cal']
# model_compared_12443_12422['cociente']= (model_12410['linear_appres_cal']/model_12422['linear_appres_cal'])*100
# model_compared_12443_12422= model_compared_12443_12422.drop(columns=['log_appres_cal','linear_appres_cal'])
# model_compared_12443_12422.to_csv('/home/m/Documents/cluster_resultados/perl5/ptm_intel/ptm_tt/compared_12443_12422.csv')

# #Comparar sin constricciones vs constricciones en puro mar
# model_compared_12410_12516=model_12410.copy()
# model_compared_12410_12516['diff']= model_12410['linear_appres_cal']-model_12516['linear_appres_cal']
# model_compared_12410_12516['cociente']= (model_12410['linear_appres_cal']/model_12516['linear_appres_cal'])
# model_compared_12410_12516= model_compared_12410_12516.drop(columns=['log_appres_cal','linear_appres_cal'])
# #model_compared_12410_12516.to_csv('/home/m/Documents/cluster_resultados/perl5/ptm_intel/ptm_tt/compared_12410_12516.csv')

# #  Comparar sin constricciones vs constricciones en puro mar, beta =0.5
# model_compared_12601_12602=model_12601.copy()
# model_compared_12601_12602['diff']= model_12601['linear_appres_cal']-model_12602['linear_appres_cal']
# model_compared_12601_12602['cociente']= (model_12601['linear_appres_cal']/model_12602['linear_appres_cal'])
# model_compared_12601_12602 = model_compared_12601_12602.drop(columns=['log_appres_cal','linear_appres_cal'])
# #model_compared_12601_12602.to_csv('/home/m/Documents/cluster_resultados/perl5/ptm_intel/ptm_tt/compared_12601_12602.csv')

## New_sea threshold
## Sección alejada de los ojos de agua que tiene los valores de resistividad más característicos de "agua salada" en el modelo libre. Comparé cuatro valores sin constricciones con 4 betas diferentes

# ## Sin constricciones
# model_12410 = pd.read_csv('/home/m/Documents/cluster_resultados/perl5/ptm_intel/ptm_tt/ptm_tt_1/output/to_voxler_marcluster1.dat_12410.csv') 
# model_12601 = pd.read_csv('/home/m/Documents/cluster_resultados/perl5/ptm_intel/ptm_tt/ptm_tt_1_0.5/to_voxler_marcluster1.dat_12601.csv')
# model_12641 = pd.read_csv('/home/m/Documents/cluster_resultados/perl5/ptm_intel/ptm_tt/ptm_tt_1_0.01/to_voxler_marcluster1.dat_12641.csv')
# model_12642 = pd.read_csv('/home/m/Documents/cluster_resultados/perl5/ptm_intel/ptm_tt/ptm_tt_1_0.001/to_voxler_marcluster1.dat_12642.csv')

# def region_salada(data):
#     easting_condition = (data['easting'] > 500) & (data['easting'] < 700)
#     northing_condition = (data['northing'] > 500) & (data['northing'] < 800)
#     depth_condition = data['depth'] == -3
#     # Apply the filter
#     filtered_data = data[easting_condition & northing_condition & depth_condition]
#     return filtered_data 
# model_0_1   = region_salada(model_12410)
# model_0_5   = region_salada(model_12601)
# model_0_01  = region_salada(model_12641)
# model_0_001 = region_salada(model_12642)

# # Calculate quartiles

# def quartile_intervals(data,name):
#     q1 = np.percentile(data, 25)
#     q2 = np.percentile(data, 50)
#     q3 = np.percentile(data, 75)

#     # Calculate standard deviation
#     std = np.std(data)

#     # Calculate intervals
#     interval1 = [q2 - std, q2 + std]
#     start = round(interval1[0],3)
#     end =   round(interval1[1],3)
#     log_start = round(np.log10(start),3)
#     log_end = round(np.log10(end),3)
#     # Print quartile values and intervals
#     print(name)
#     print("Q1:", q1)
#     print("Q2:", q2)
#     print("Q3:", q3)
#     print('std=',std)
#     print("Interval (1 std deviation):", "(",start,end,")")
#     print("Interval log (1 std deviations):", "(",log_start,log_end,")")

# def plot_region_salada(model_0_1,model_0_5,model_0_01,model_0_001):

#     fig= plt.subplots(figsize=(8, 10))

#     plt.subplot(4, 2, 1)
#     plt.plot(model_0_1.linear_appres_cal,'*',color='red',label='sin constricciones')
#     plt.title('b=0.1')
    
#     #plt.legend()
    
#     plt.subplot(4, 2, 2)
#     plt.hist(model_0_1.linear_appres_cal)
#     plt.title('Histogram')
#     plt.xlabel('Value')
#     plt.ylabel('Frequency')
#     quartile_intervals(model_0_1.linear_appres_cal,'model_0_1')
    
#     plt.subplot(4, 2, 3)
#     plt.plot(model_0_5.linear_appres_cal,'*',color='red',label='sin constricciones')
#     plt.title('b=0.5')
#     #plt.legend()
    
#     plt.subplot(4, 2, 4)
#     plt.hist(model_0_5.linear_appres_cal)
#     plt.title('Histogram')
#     plt.xlabel('Value')
#     plt.ylabel('Frequency')
#     quartile_intervals(model_0_5.linear_appres_cal,'model_0_5')
    
#     plt.subplot(4, 2, 5)
#     plt.plot(model_0_01.linear_appres_cal,'*',color='red',label='sin constricciones')
#     plt.title('b=0.01')
#     #plt.legend()
    
#     plt.subplot(4, 2, 6)
#     plt.hist(model_0_01.linear_appres_cal)
#     plt.title('Histogram')
#     plt.xlabel('Value')
#     plt.ylabel('Frequency')
 
#     plt.subplot(4, 2, 7)
#     plt.plot(model_0_001.linear_appres_cal,'*',color='red',label='sin constricciones')
#     plt.title('b=0.001')
#     #plt.legend()
#     plt.tight_layout()
    
#     plt.subplot(4, 2, 8)
#     plt.hist(model_0_001.linear_appres_cal)
#     plt.title('Histogram')
#     plt.xlabel('Value')
#     plt.ylabel('Frequency')

#     plt.show()

#plot_region_salada(model_0_1,model_0_5,model_0_01,model_0_001)