import pandas as pd
import tkinter as tk
from tkinter import filedialog
import xlsxwriter


def processFile():
    historicalYears = 8
    raw_path = filedialog.askopenfilename()
    df = pd.read_csv(filepath_or_buffer=raw_path)
    df.drop(['open', 'high','low','close','Volume','Volume MA'], axis=1, inplace=True)
    count = 0
    for i in df['time']:
        i = i[0:10]
        df.iloc[count, 0] = i
        count = count +1
    df.set_index(df['time'])
    print(df.shape)
    for i in range(df.shape[0]-historicalYears):
        df.drop([df.index[0]], inplace = True) 
        
    df2 = df.transpose()
    new_path = filedialog.askopenfilename()
    
    
    with pd.ExcelWriter(new_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:  # pylint: disable=abstract-class-instantiated
        df2.to_excel(writer, sheet_name='DF')

window = tk.Tk()
window.title("etc")
window.geometry('350x200')
label = tk.Label(text = "1st Selecton to choose raw Data" +"\n" +"2nd Selection to Choose The file to add Data to")
button2 = tk.Button(text="Add Raw Data", command = processFile)
label.pack()
button2.pack()
window.mainloop()