import zipfile,sys
src,d,out=sys.argv[1:]
zi=zipfile.ZipFile(src)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
  for i in zi.infolist(): z.writestr(i.filename,open(d+'/'+i.filename,'rb').read())
