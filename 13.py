import csv

def writeCSV(filename,data):
    
    
    with open(filename,mode='w') as read_csv:
        
        title =['Name','Address','Age']
        file_write = csv.writer(read_csv,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        file_write.writerow(title)     
        for i in data:            
            file_write.writerow(i)
    
    read_csv.close()

data_list = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
filename = "sample.csv"

writeCSV(filename,data_list)
