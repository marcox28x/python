import sys
import os
import py_compile

def timelimit(timeout, func, args=(), kwargs={}):
    import threading
    class FuncThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = None
        def run(self):
            self.result = func(*args, **kwargs)
    it = FuncThread()
    it.start()
    it.join(timeout)
    if it.is_alive():
        return "\nIl tuo programma sta eseguendo un ciclo infinito.\nPer ucciderlo non basta premere invio\n devi chiudere la finesta con il mouse"
    else:
        return it.result
  
f=open("config.txt","r", encoding="UTF8")
for i in range(6):
    s=f.readline().strip()
if s != "NoHelperModules":
    exec("import " + s)
for i in range(2):
    s=f.readline().strip()
try:    
    print("Compilo ",s)
    py_compile.compile(s,doraise=True)
except py_compile.PyCompileError:
    tb=sys.exc_info()[2]
    tbb=tb.tb_next
    tbbb=tbb.tb_next
    print("Si è verificato un errore di compilazione")
    #print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    tb=sys.exc_info()[2]
    h=input("Premere invio per terminare...")
    sys.exit()
try:
    exec("import "+s[0:len(s)-3])
    metodoStu=s[0:len(s)-3]
    s=f.readline().strip()
    s=f.readline().strip()
    metodoStu+="."+s
    while s[0]!="(":
        s=f.readline().strip()
    i=1
    errori=0
    while len(s)>0:
        coppiaInputRisultato = s.strip().split("-->") #FL COPIA INPUT RISULTATO
        print("========================")
        #print(metodoStu[6:]+coppiaInputRisultato[0]) #ELIMINATO SA
        print(metodoStu.split(".")[1]+coppiaInputRisultato[0])            
        print("========================")
        #exec("doc="+metodoDoc+s) #ELIMINATO FL
        exec("doc="+coppiaInputRisultato[1]) #FL RISULTATO GIUSTO
        print("Il risultato giusto:")
        print(doc,"\n***********")    
        parametri=coppiaInputRisultato[0][1:-1].split("),")
        parametri[0]=parametri[0]+")";
        #print(parametri[0]+","+parametri[1])
        nomeFile= metodoStu.split(".")[0]
        nomeMetodo= metodoStu.split(".")[1]
        #print(nomeFile+" "+nomeMetodo)
        commandp1="p1="+nomeFile+"."+parametri[0]
        commandp2="p2="+nomeFile+"."+parametri[1]
        command="stu=timelimit(3,p1.piuForte,[p2])"
        exec(commandp1)
        exec(commandp2)
        exec(command)
        #print(commandp1)
        #print(commandp2)
        #print(command)

        if(stu is None):
            print("Il tuo risultato:",stu,"\n***********")
        else:
            print("Il tuo risultato:")
            print(stu,"\n***********")
        if stu==doc:
            print("Il tuo risultato è giusto!")
        else:
           print("Il tuo risultato è sbagliato!")
           errori=errori+1
        print("--------------------------------------------")   
        s=f.readline().strip()
        i=i+1
    if errori>0:
        print("ATTENZIONE !!!! Il tuo metodo ha fallito ",errori, " volte")
    else:
        print("CONGRATULAZIONI!!! Il tuo programma ha superato tutti i test")
    
except BaseException:
    tb=sys.exc_info()[2]
    tbb=tb.tb_next
    tbbb=tbb.tb_next
    print("Durante l'esecuzione del tuo codice")
    print("si è verificato un errore alla linea:", tbbb.tb_lineno)
    #print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    tb=sys.exc_info()[2]
    
h=input("Premere invio per terminare...")     
