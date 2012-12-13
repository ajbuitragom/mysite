from django.db import models
# La clase de la primera tabla para la base de datos
#que es la de Polls es decir las preguntas que va a 
#contener la encuesta.
class Poll(models.Model):									
	#Primer Campo de la tabla Polls que es la pregunta.
	#Le indica que debe ser un campo de tipo Varchar
	#y tiene una propiedad que es el maximo de tamano que 
	#puede contener el campo.
    question = models.CharField(max_length=200)
    #Segundo campo de la tabla Polls
    #Le indica que es un campo de fecha con el tipo datetime
    #y tiene una propiedad que es el nombre que observara el
    #usuario.
    pub_date = models.DateTimeField('date published')

    #No olvidar que cada una de las tablas que se crea contiene
    #un campo oculto que es la llave primaria (Pk)

    #se define una funcion para que devuelva el valor del campo
    #determinado. En este caso es Question,
    def __unicode__(self):
        #Devuelve el valor del campo question.
        return self.question

#-----------------------------------------------------------------------------------------------------

#La segunda tabla de la base de datos 
# es la de Choice, es decir, las posibles respuestas
#que tiene el usuario para la pregunta que esta en la 
#primera tabla.
class Choice(models.Model):
	#El primer campo de la tabla Choice es un camop de 
	#relacion para con la primera tabla, por eso 
	#el tipo de dato es ForeignKey (FK) e indica que es con 
	#la tabla Poll
    poll = models.ForeignKey(Poll)

    #El segundo campo de la tabla es el de choice, que es donde
    #se le va a indicar cada una de las posibles reespuestas
    #con respecto a la tabla Polls. es de Tipo VarChar con la
    #propiedad de tamano del campo que es maximo 200.
    choice = models.CharField(max_length=200)

    #El tercer y ultimo campo de la tabla es el de voto de 
    #tipo Int que es donde se va a llevar el control de la 
    #cantidad de personas que voten por cada opcion en una 
    #pregunta
    votes = models.IntegerField()

    #se define una funcion para que devuelva el valor del campo
    #determinado. En este caso es choice,
    def __unicode__(self):
        #Devuelve el valor del campo choice.
        return self.choice