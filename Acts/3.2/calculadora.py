# JEREMY FARYD CORTES MUÑOZ 1910064

# Importamos los módulos necesarios de la biblioteca tkinter
from tkinter import Button, Tk, Frame,Entry,END

# Crear la ventana principal
ventana = Tk()
ventana.geometry('274x328')		# Establecemos el tamaño de la ventana
ventana.config(bg= "white")		# Establecemos el color de fondo
ventana.iconbitmap(default='C:\\Users\\jemi_\\Documents\\7mo semestre\\calculadora.ico')	# Establecemos el ícono de la ventana
ventana.resizable(0,0)			#hacemos que la ventana no sea redimensionable
ventana.title('Calculadora')	# Establecemos el título de la ventana

# Creamos una clase de botón personalizada con efectos de desplazamiento
class HoverButton(Button):
	def __init__(self, master, **kw):
		Button.__init__(self,master=master,**kw)
		self.defaultBackground = self["background"]
		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self, e):
		self["background"] = self["activebackground"]

	def on_leave(self, e):
		self["background"] = self.defaultBackground

# Iniciamos una variable para realizar un seguimiento de la posición de entrada
i=0

# Función para agregar un dígito u operador al widget de entrada
def obtener(dato):
	global i
	i+=1
	Resultado.insert(i, dato)

# Función para evaluar la expresión en el widget de entrada	
def operacion():
	global i

	ecuacion = Resultado.get()
	if i !=0:		
		try:
			result = str(eval(ecuacion))
			Resultado.delete(0,END)
			Resultado.insert(0,result)
			longitud = len(result)
			i = longitud

		except:
			result = 'ERROR'
			Resultado.delete(0,END)
			Resultado.insert(0,result)
	else:
		pass

# Función para eliminar el último carácter en el widget de entrada
def borrar_uno():
	global i 
	if i==-1:
		pass
	else:
		Resultado.delete(i,last =None)
		i-=1

# Función para borrar todo el contenido del widget de entrada		
def borrar_todo():
	Resultado.delete(0, END)	
	i=0

# Crear un marco dentro de la ventana principal
frame = Frame(ventana, bg ='black', relief = "raised")
frame.grid(column=0, row=0, padx=6, pady=3)

# Crear un widget de entrada para mostrar la entrada y los resultados
Resultado = Entry(frame,bg='#9EF8E8', width=18, relief='groove', font = 'Montserrat 16',justif = 'right')
Resultado.grid(columnspan=4 , row=0, pady=3,padx=1, ipadx=1, ipady=1) 

# Botones para dígitos, operadores y funciones especiales
#fila 1
Button1 = HoverButton(frame, text= "1", borderwidth=2, height=2, width=5, font= ('Comic sens MC',12,'bold'),relief = "raised", activebackground="#515275", bg ='#999AB8',  anchor="center", command=lambda: obtener(1))  
Button1.grid( column= 0 ,row=1, pady=1,padx=3)
Button2 = HoverButton(frame, text= "2", height=2, width=5, font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#515275",bg ='#999AB8', anchor="center",command=lambda: obtener(2))  
Button2.grid(column =1 , row=1, pady=1,padx=1)
Button3 = HoverButton(frame, text= "3", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#515275", bg ='#999AB8', anchor="center",command=lambda: obtener(3))  
Button3.grid(column =2, row=1, pady=1,padx=1)
Button_borrar = HoverButton(frame, text= "⌫", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="red", bg='#cc2823',  anchor="center",command=lambda: borrar_uno())  
Button_borrar.grid(column =3, row=1, pady=2,padx=2)

#fila 2
Button4 = HoverButton(frame, text= "4",height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#515275", bg ='#999AB8', anchor="center",command=lambda: obtener(4))  
Button4.grid( column= 0 ,row=2, pady=1,padx=1)
Button5 = HoverButton(frame, text= "5", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#515275",bg ='#999AB8', anchor="center",command=lambda: obtener(5))  
Button5.grid(column =1 , row=2, pady=1,padx=1)
Button6 = HoverButton(frame, text= "6", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#515275",bg ='#999AB8',  anchor="center",command=lambda: obtener(6))  
Button6.grid(column =2, row=2, pady=1,padx=1)
Button_mas = HoverButton(frame, text= "+", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#999AB8", bg='#494a70',  anchor="center",command=lambda: obtener('+'))  
Button_mas.grid(column =3, row=2, pady=2,padx=2)

#fila 3
Button7 = HoverButton(frame, text= "7",height=2, width=5, font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#515275",bg ='#999AB8',  anchor="center",command=lambda: obtener(7))  
Button7.grid( column= 0 ,row=3, pady=1,padx=1)
Button8 = HoverButton(frame, text= "8", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#515275",bg ='#999AB8', anchor="center",command=lambda: obtener(8))  
Button8.grid(column =1 , row=3, pady=1,padx=1)
Button9 = HoverButton(frame, text= "9", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#515275",bg ='#999AB8',  anchor="center",command=lambda: obtener(9))  
Button9.grid(column =2, row=3, pady=1,padx=1)
Button_menos = HoverButton(frame, text= "-", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#999AB8", bg='#494a70',  anchor="center",command=lambda: obtener('-'))  
Button_menos.grid(column =3, row=3, pady=2,padx=2)

#fila 4
Button0 = HoverButton(frame, text= "0",height=5, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#515275",bg ='#999AB8',  anchor="center",command=lambda: obtener(0))  
Button0.grid( column= 0, rowspan=2, row=4, pady=1,padx=1)
Button_punto = HoverButton(frame, text= ".", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#515275",bg ='#999AB8', anchor="center",command=lambda: obtener('.'))  
Button_punto.grid(column =1 , row=4, pady=1,padx=1)
Button_entre = HoverButton(frame, text= "÷", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#999AB8",bg ='#494a70',  anchor="center",command=lambda: obtener('/'))  
Button_entre.grid(column =2, row=4, pady=1,padx=1)
Button_por = HoverButton(frame, text= "x", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#999AB8", bg='#494a70',  anchor="center",command=lambda: obtener('*'))  
Button_por.grid(column =3, row=4, pady=2,padx=2)

#fila 4
Button_igual = HoverButton(frame, text= "=", height=2, width=12,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#63626e", bg='#d1d5e6', anchor="center",command=lambda: operacion())  
Button_igual.grid(column =1 ,columnspan=2, row=5, pady=1,padx=1)
Button_borrar = HoverButton(frame, text= "C", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2, relief = "raised", activebackground="#999AB8", bg='#494a70', anchor="center",command=lambda: borrar_todo())  
Button_borrar.grid(column =3, row=5, pady=2,padx=2)

# Ejecutamos el bucle principal de eventos
ventana.mainloop()
