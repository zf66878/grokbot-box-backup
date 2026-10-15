/usr/bin/python3 - <<'PYEOF'
L=[["2023-04", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2023年文件/23年工资表/4月工资表/月度课时明细计算_0_202304M.xlsx"], ["2023-05", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2023年文件/23年工资表/5月工资表/月度课时明细计算_0_202305M.xlsx"], ["2023-06", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2023年文件/23年工资表/6月工资表/月度课时明细计算_0_202306王.xlsx"], ["2023-07", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2023年文件/23年工资表/7月工资表/月度课时明细计算_0_202307M.xlsx"], ["2023-08", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2023年文件/23年工资表/8月工资表/月度课时明细计算_0_202308M.xlsx"], ["2023-09", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2023年文件/23年工资表/9月工资表/月度课时明细计算_0_202309M.xlsx"], ["2023-10", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2023年文件/23年工资表/10月工资表/月度课时明细计算_0_202310M.xlsx"], ["2023-11", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2023年文件/23年工资表/11月工资表/月度课时明细计算_0_202311M.xlsx"], ["2023-12", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2023年文件/23年工资表/12月工资表/月度课时明细计算_0_202312M.xlsx"], ["2024-01", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2024年文件/2024工资表/1月工资表/月度课时明细计算_0_202401M.xlsx"], ["2024-02", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2024年文件/2024工资表/2月工资表/月度课时明细计算_0_202402M.xlsx"], ["2024-03", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2024年文件/2024工资表/3月工资表/月度课时明细计算_0_202403M.xlsx"], ["2024-04", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2024年文件/2024工资表/4月工资表/月度课时明细计算_0_202404M.xlsx"], ["2024-05", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2024年文件/2024工资表/5月工资表/月度课时明细计算_0_202405M.xlsx"], ["2024-06", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2024年文件/2024工资表/6月工资表/月度课时明细计算_0_202406M.xlsx"], ["2024-07", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2024年文件/2024工资表/7月工资表/月度课时明细计算_0_202407M.xlsx"], ["2024-08", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2024年文件/2024工资表/8月工资表/月度课时明细计算_0_202408M.xlsx"], ["2024-09", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2024年文件/2024工资表/9月工资表/月度课时明细计算_0_202409M2.xlsx"], ["2024-10", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2024年文件/2024工资表/10月工资表/月度课时明细计算_0_202410M.xlsx"], ["2024-11", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2024年文件/2024工资表/11月工资表/月度课时明细计算_0_202411M.xlsx"], ["2024-12", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2024年文件/2024工资表/12月工资表/月度课时明细计算_0_202412M.xlsx"], ["2025-01", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2025年文件/2025工资表/1月工资表/月度课时明细计算_0_202501M.xlsx"], ["2025-02", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2025年文件/2025工资表/2月工资表/月度课时明细计算_0_202502M.xlsx"], ["2025-03", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2025年文件/2025工资表/3月工资表/月度课时明细计算_0_202503M.xlsx"], ["2025-04", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2025年文件/2025工资表/4月工资表/月度课时明细计算_0_202504M.xlsx"], ["2025-05", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2025年文件/2025工资表/5月工资表/月度课时明细计算_0_202505M.xlsx"], ["2025-06", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2025年文件/2025工资表/6月工资表/月度课时明细计算_0_202506M.xlsx"], ["2025-07", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2025年文件/2025工资表/7月工资表/月度课时明细计算_0_202507M.xlsx"], ["2025-08", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2025年文件/2025工资表/8月工资表/月度课时明细计算_0_202508M.xlsx"], ["2025-09", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2025年文件/2025工资表/9月工资表/月度课时明细计算_0_202509M.xlsx"], ["2025-10", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2025年文件/2025工资表/10月工资表/月度课时明细计算_0_202510M.xlsx"], ["2025-11", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2025年文件/2025工资表/11月工资表/月度课时明细计算_0_202511M.xlsx"], ["2025-12", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/10_历年原始档案/2025年文件/2025工资表/12月工资表/月度课时明细计算_0_202512M.xlsx"], ["2026-01", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/0财务计算/2026文件/2026工资表/1月工资表/月度课时明细计算_0_202601M.xlsx"], ["2026-02", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/0财务计算/2026文件/2026工资表/2月工资表/月度课时明细计算_0_202602M.xlsx"], ["2026-03", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/0财务计算/2026文件/2026工资表/3月工资表/月度课时明细计算_0_202603M.xlsx"], ["2026-04", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/0财务计算/2026文件/2026工资表/4月工资表/月度课时明细计算_0_202604M.xlsx"], ["2026-05", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/0财务计算/2026文件/2026工资表/5月工资表/月度课时明细计算_0_202605M.xlsx"], ["2026-06", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/0财务计算/2026文件/2026工资表/6月工资表/月度课时明细计算_0_202606M.xlsx"], ["2026-07", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/0财务计算/2026文件/2026工资表/7月工资表/7月工资表最终版/月度课时明细计算_0_202607M.xlsx"], ["2026-08", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/0财务计算/2026文件/2026工资表/8月工资表/8月工资表(财务定稿)/月度课时明细计算_0_202608M.xlsx"], ["2026-09", "/Users/zhengfeng/Documents/D盘文件/1财务完整资料/0财务计算/2026文件/2026工资表/2026年9月工资计算/智能薪酬复核/月度课时明细计算_补课AB最终重算_202609M.xlsx"]]

import zipfile,re,json,sys
import xml.etree.ElementTree as ET
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def col(c):
  n=0
  for ch in re.match(r'[A-Z]+',c).group(0): n=n*26+ord(ch)-64
  return n-1
out=[]
for m,p in L:
  try:
    z=zipfile.ZipFile(p)
    ss=[]
    if 'xl/sharedStrings.xml' in z.namelist():
      for si in ET.fromstring(z.read('xl/sharedStrings.xml')).iter('{%s}si'%NS['m']):
        ss.append(''.join(t.text or '' for t in si.iter('{%s}t'%NS['m'])))
    wb=ET.fromstring(z.read('xl/workbook.xml'))
    rels=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
    rid=[s.get('{%s}id'%NS['r']) for s in wb.iter('{%s}sheet'%NS['m']) if s.get('name')=='智能薪酬'][0]
    tgt=[r.get('Target') for r in rels if r.get('Id')==rid][0].lstrip('/')
    if not tgt.startswith('xl/'): tgt='xl/'+tgt
    sh=ET.fromstring(z.read(tgt))
    rows=[]
    for row in sh.iter('{%s}row'%NS['m']):
      d={}
      for c in row.iter('{%s}c'%NS['m']):
        v=c.find('m:v',NS); t=c.get('t')
        if t=='inlineStr':
          val=''.join(x.text or '' for x in c.iter('{%s}t'%NS['m']))
        elif v is None: continue
        elif t=='s': val=ss[int(v.text)]
        else:
          val=v.text
          if t not in ('str','b','e'):
            try: val=float(val)
            except: pass
        d[col(c.get('r'))]=val
      rows.append(d)
    h=rows[0]; H={v:k for k,v in h.items()}
    need=['上课老师姓名','班级','年级','上课时间','备注','学生课时','老师课时','所属年级','总计','合计','课时基数','递增基数','实到人数','数量','比例']
    for r in rows[1:]:
      rem=str(r.get(H.get('备注'),'') or '')
      if '补课' not in rem and '补课' not in str(r.get(H.get('班级'),'')): continue
      out.append({'月份':m,**{k:r.get(H[k]) for k in need if k in H}})
    print('OK',m,len(rows),file=sys.stderr)
  except Exception as e:
    print('ERR',m,repr(e),file=sys.stderr)
print(json.dumps(out,ensure_ascii=False))
PYEOF
