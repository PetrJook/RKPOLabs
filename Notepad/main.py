from tkinter import Tk, Frame, Text, Scrollbar, Menu, filedialog, END

class TkApp(Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title('Блокнот')
        self.geometry('600x650')
        self.f_text = Frame(self)
        self.f_text.pack(fill='both', expand = 1)
        self.text_field = Text(self.f_text, bg = 'grey', fg = 'black', 
                               padx = 10, pady = 10, wrap='word',
                               insertbackground = 'black',
                               selectbackground = 'blue',
                               spacing3 = 15,
                               width = 30,
                               font = 'Arial 11 bold')
        self.text_field.pack(expand = 1, fill='both', side = 'left')

        self.scroll = Scrollbar(self.f_text, command = self.text_field.yview)
        self.scroll.pack(side = 'left', fill = 'y')
        self.text_field.config(yscrollcommand=self.scroll.set)

        self.main_menu = Menu(self)


        self.file_menu = Menu(self.main_menu, tearoff = 0)
        self.file_menu.add_command(label = 'Открыть', command = self.open_file)
        self.file_menu.add_command(label = 'Сохранить', command = self.save_file)

        self.main_menu.add_cascade(label='Файл', menu= self.file_menu)

        self.config(menu=self.main_menu)
    
    def open_file(self):
        file_path = filedialog.askopenfilename(title = 'Выбор файла', filetypes = (('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
        if file_path:
            self.text_field.delete('1.0', END)
            self.text_field.insert('1.0', open(file_path, encoding= 'utf-8').read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(filetypes = (('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
        if (not file_path.endswith('.txt')):
            file_path += '.txt'
        f = open(file_path, 'w', encoding = 'utf-8')
        text = self.text_field.get('1.0', END)
        f.write(text)
        f.close()
        

App = TkApp()
App.mainloop()