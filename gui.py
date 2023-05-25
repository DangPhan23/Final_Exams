import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
import numpy as np
#load the trained model to classify sign
from keras.models import load_model
model = load_model('traffic_classifier.h5', compile=False)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#dictionary to label all traffic signs class.
classes = {1:'Tốc độ giới hạn (20km/h)',
           2:'Tốc độ giới hạn (30km/h)',
           3:'Tốc độ giới hạn (50km/h)',
           4:'Tốc độ giới hạn (60km/h)',
           5:'Tốc độ giới hạn (70km/h)',
           6:'Tốc độ giới hạn (80km/h)',
           7:'Hạn chế tốc độ tối đa (80km/h)',
           8:'Tốc độ giới hạn (100km/h)',
           9:'Tốc độ giới hạn (120km/h)',
           10:'Cấm vượt',
           11:'Cấm xe tải vượt',
           12:'Quyền ưu tiên tại giao lộ',
           13:'Đường ưu tiên',
           14:'Giao nhau với đường ưu tiên',
           15:'Stop',
           16:'Đường Cấm',
           17:'Cấm xe tải',
           18:'Cấm đi ngược chiều',
           19:'Nguy Hiểm',
           20:'Khúc cua nguy hiểm bên trái',
           21:'Khúc cua nguy hiểm bên phải',
           22:'Đường cong đôi',
           23:'Con đường gập ghềnh',
           24:'Đường trơn trượt',
           25:'Đường hẹp bên phải',
           26:'Công Trường',
           27:'Tín hiệu giao thông',
           28:'Người đi bộ',
           29:'Trẻ em qua đường',
           30:'Xe đạp qua đường',
           31:'Coi chừng băng/tuyết',
           32:'Động vật hoang dã băng qua',
           33:'Tốc độ kết thúc + giới hạn vượt qua',
           34:'Chỉ được rẽ phải',
           35:'Chỉ được rẽ trái',
           36:'Chỉ đi thẳng',
           37:'Đi thẳng hoặc phải',
           38:'Đi thẳng hoặc trái',
           39:'Đi bên phải',
           40:'Đo bên trái',
           41:'Bắt buộc đi vòng xuyến',
           42:'Kết thúc cấm vượt',
           43:'Kết thúc cấm xe tải vượt' }
#initialise GUI
top=tk.Tk()
top.geometry('1000x600')
top.title('Phân loại biển báo giao thông')
top.configure(background='#fbfcf7')
label=Label(top,background='#fbfcf7', font=('arial',15,'bold'))
sign_image = Label(top)
def classify(file_path):
   global label_packed
   image = Image.open(file_path)
   image = image.resize((30,30))
   image = numpy.expand_dims(image, axis=0)
   image = numpy.array(image)
   predict_x = model.predict([image])[0]
   pred = np.argmax(predict_x, axis=-1)
   sign = classes[pred+1]
   print(sign)
   label.configure(foreground='#011638', text=sign)
def show_classify_button(file_path):
   classify_b=Button(top,text="Dự Đoán",command=lambda: classify(file_path),padx=10,pady=5)
   classify_b.configure(background='#cf0404', foreground='white',font=('arial',10,'bold'))
   classify_b.place(relx=0.79,rely=0.46)
def upload_image():
    try:
       file_path=filedialog.askopenfilename()
       uploaded=Image.open(file_path)
       uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
       im=ImageTk.PhotoImage(uploaded)
       sign_image.configure(image=im)
       sign_image.image=im
       label.configure(text='')
       show_classify_button(file_path)
    except:
       pass
upload=Button(top,text="Chọn Ảnh",command=upload_image,padx=10,pady=5)
upload.configure(background='#cf0404', foreground='white',font=('arial',15,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Phân loại biển báo giao thông",pady=20, font=('arial',20,'bold'))
heading.configure(background='#cf0404',foreground='#364156')
heading.pack()
top.mainloop()