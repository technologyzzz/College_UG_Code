# read file txt

file_biodata = open("C:/CODE/code-college/alg&pemr_1/pa_ahmad_hidayat/biodata.txt",'r')

biodata = file_biodata.readlines()
print (biodata) #pembacaan seluruh baris

print (biodata[0]) #pembacaan per index
print (biodata[1])

biodata_read = file_biodata.read()
print(biodata_read) #pembacaan seluruh data

file_biodata.close()

# write file txt
teks = 'Ini sebuah teks\n'
teks_list = ['apel','mangga','anggur']

f = open("C:/CODE/code-college/alg&pemr_1/pa_ahmad_hidayat/teks.txt",'w')
f.write(teks)
f.writelines(teks_list)

f.close()


# read file xlsx

import pandas as pd 

# load the xlsx file
excel_data = pd.read_excel('sales.xlsx')
# read the values of the file in the dataframe
data = pd.DataFrame(excel_data, colmns=['Sales Date', 'Sales Person', 'Amount'])
#
print('The Content of file is :\n', data)
                    
# write file txt

import pandas as pd 

csv_data = pd.read_csv('Sales.csv')
print(csv_data)

#head() utk membaca per index
