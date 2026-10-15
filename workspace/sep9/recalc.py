import uno,subprocess,time,os
from com.sun.star.beans import PropertyValue
p=subprocess.Popen(['soffice','--headless','--invisible','--accept=socket,host=localhost,port=2002;urp;'])
time.sleep(4)
ctx=uno.getComponentContext()
r=ctx.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver",ctx)
c=r.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
desk=c.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop",c)
pv=PropertyValue();pv.Name="Hidden";pv.Value=True
doc=desk.loadComponentFromURL("file://"+os.path.abspath('stage1.xlsx'),"_blank",0,(pv,))
doc.calculateAll()
f=PropertyValue();f.Name="FilterName";f.Value="Calc MS Excel 2007 XML"
doc.storeToURL("file://"+os.path.abspath('lo/recalc.xlsx'),(f,))
doc.close(True);p.terminate()
