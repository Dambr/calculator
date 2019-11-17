from tkinter import *
from math import *

class Window():

	def __init__(self):
		text = ['sin(', 'cos(', '(',  ')'  ,
				  '+' ,   '-' , '*',  '/'  ,
				  '7' ,   '8' , '9',  'pi' ,
				  '4' ,   '5' , '6',  'e'  ,
				  '1' ,   '2' , '3', 'log(',
				  '.' ,   '0' , '=', 'del' ] 
		self.entry = Entry(
			font = ('Verdana', 30),
			width = 18,
			justify = RIGHT,
			relief = FLAT,
			)
		self.entry.place(x = 20, y = 10)
		self.button = [''] * len(text)
		for i in range(len(text)):
			self.button[i] = Button(root,
				font = ('Verdana', 30),
				relief = SOLID,
				width = 3,
				justify = CENTER,
				bg = '#98A1A5',
			)
			self.button[i]['text'] = text[i]
			self.button[i].place(x = 25 + 114 * (i % 4), y = 80 + 70 * (i // 4))
		
		for i in range(0, len(text) - 2):
			self.button[i].bind('<ButtonRelease-1>', lambda i : self.entry.insert('end', str(self.entry.insert('end', self.button[ int(str(i.widget).replace('.!button', '')) - 1 ]['text'])).replace('None', '') )) if i != 0 else self.button[i].bind('<ButtonRelease-1>', lambda i : self.entry.insert('end', str(self.entry.insert('end', self.button[ 0 ]['text'])).replace('None', '') ))

		self.button[len(text) - 2].bind('<ButtonRelease-1>', self.Enter)
		self.button[len(text) - 1].bind('<ButtonRelease-1>', self.Delete)

	def Enter(self, event):
		try:
			x = self.entry.get()
			self.entry.delete(0, 'end')
			x = eval(x)
			self.entry.insert(0, str(x))
		except:
			self.entry.delete(0, 'end')
			self.entry.insert(0, 'Error of input')

	def Delete(self, event):
		self.entry.delete(0, 'end')


root = Tk()
root.title('Калькулятор')
root.wm_geometry('500x500')
root.resizable(width=False, height=False)
window = Window()
root.mainloop()