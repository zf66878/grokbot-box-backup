import sys,re,glob
from rapidocr_onnxruntime import RapidOCR
eng=RapidOCR()
for x in ['qm','zm']:
  rows=[]
  for p in range(1,9):
    res,_=eng(f'{x}-{p}.png')
    res=sorted(res,key=lambda r:(r[0][0][1]+r[0][2][1])/2)
    lines=[];cur=[];cy=None
    for b,t,s in res:
      y=(b[0][1]+b[2][1])/2
      if cy is None or abs(y-cy)<15: cur.append((b[0][0],t));cy=y if cy is None else cy
      else: lines.append(cur);cur=[(b[0][0],t)];cy=y
    lines.append(cur)
    for l in lines:
      s=' | '.join(t for _,t in sorted(l))
      print(x,p,s)
