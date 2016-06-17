import os
import sys
#clase principal
class Renderizador(object):
    convertidor=""
    pathoriginal=""
    pathconvertido=""
    #donde se almacenara todo el shell
    lote="cd / "
#constructor
    def __init__(self,pathconvertidor,original,convertido):
        self.convertidor=pathconvertidor
        self.pathoriginal=original
        self.pathconvertido=convertido
        pass
    def iniciarrender(self):
        dir=os.listdir(self.pathoriginal)
        for archivo in dir:
            if (".pdf" in archivo):self.renderizarelemnto(archivo)
        print "lote:"+self.lote
        self. ejecutarlote()
        pass

        #rederinza cada pdf
    def renderizarelemnto(self,archivo):
        self.lote=self.lote+"\n"+"."+self.convertidor+" "+self.pathoriginal+"/"+archivo+"  "+self.pathconvertido+"/"+archivo

    def ejecutarlote(self):
        os.system(self.lote)
        pass

#comprueba si existe ruta de destino y si no la crea
    def existe_convertido(self):

        if not  os.path.exists(self.pathconvertido):
         os.mkdir(self.pathconvertido,0o777)
         if(os.path.exists(self.pathconvertido)):
             return 1
        else:
            return 1
        return 0
#comprueba si existen pdfs que renderizar
    def existen_orginales(self):
        dir=os.listdir(self.pathoriginal)
        for archivo in dir:
            if (".pdf" in archivo):
             return 1
        pass

        return 0


    pass


#verficamos que exista ruta origien y archivo rederizador







originales="originales"
convertidos="convertidos"
convertidor="shrinkpdf.sh"

try:
    ruta=sys.argv[1]

except IndexError:
    print  "No se encontraron argumentos"
    ruta = "/home/daniel/Escritorio/pdfs"

if(os.path.exists(ruta+"/"+convertidor) & os.path.exists(ruta+"/"+originales)) :

#instanciamos objeto
        render=Renderizador(ruta+"/"+convertidor,ruta+"/"+originales,ruta+"/"+convertidos)
        if(render.existen_orginales()>=1):
            if(render.existe_convertido()>=1): render.iniciarrender()


            else:print("IMPOSIBLE CREAR RUTA DESTINO , TIENE PERMISOS?")

        else: print "NO hay archivos que listas"

else:

        print "No existe convertidor"
