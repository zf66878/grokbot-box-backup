import json,datetime as dt,pandas as pd,collections
d=json.load(open('/home/box/.cursor/projects/workspace/agent-tools/1a836176-fe97-48f3-bb79-bf7d4d77854e.txt'))
print('total',d['total'],len(d['items']))
tz=dt.timezone(dt.timedelta(hours=8));rows=[];iss=[]
for it in d['items']:
    f=it['fields'];n=f.get('名称');n=''.join(x.get('text','') for x in n) if isinstance(n,list) else n
    t=f.get('创建时间');a=f.get('金额')
    if a is None: iss.append(('缺金额',n,it['record_id']))
    if t is None: iss.append(('缺日期',n,it['record_id']))
    if a is not None and not isinstance(a,(int,float)): iss.append(('金額非數字',n,a))
    rows.append(dict(id=it['record_id'],名称=n,金额=a,付款账户=f.get('付款账户'),费用周期=f.get('费用周期'),经办人=f.get('经办人'),
      月份=dt.datetime.fromtimestamp(t/1000,tz).strftime('%Y-%m') if t else None,日期=dt.datetime.fromtimestamp(t/1000,tz).strftime('%Y-%m-%d') if t else None))
df=pd.DataFrame(rows);df['金额']=pd.to_numeric(df['金额'],errors='coerce')
print(iss);print(df['费用周期'].value_counts(dropna=False));print(df['付款账户'].value_counts(dropna=False))
print(df[df.金额<=0][['名称','金额','日期']])
cur=df[df.名称.fillna('').str.contains(r'USD|\$|美元|美金|HKD|NTD|台币|日元',regex=True)];print(cur[['名称','金额']])
dup=df[df.duplicated(['名称','金额','日期'],keep=False)];print('dups',dup[['名称','金额','日期']])
v=df.dropna(subset=['月份'])
tot=v.groupby('月份').金额.agg(['sum','count']).rename(columns={'sum':'總額','count':'筆數'})
cyc=v.pivot_table(index='月份',columns='费用周期',values='金额',aggfunc='sum',fill_value=0)
acc=v.pivot_table(index='月份',columns='付款账户',values='金额',aggfunc='sum',fill_value=0)
top=v.sort_values('金额',ascending=False).groupby('月份').head(5).sort_values(['月份','金额'],ascending=[True,False])[['月份','日期','名称','金额','费用周期','付款账户']]
pd.set_option('display.width',250);pd.set_option('display.max_rows',500);pd.set_option('display.max_columns',50)
print(tot);print(cyc.round(2));print(acc.round(2));print(top.to_string())
# baseline: distinct recurring items (latest occurrence by name)
r=df[df.费用周期.isin(['月费','年费'])].sort_values('日期').drop_duplicates('名称',keep='last')
print(r[['名称','金额','费用周期','日期']].to_string())
# monthly mean baseline: 月费 avg per month + 年费 total/12 over span
mon=v[v.费用周期=='月费'].groupby('月份').金额.sum();yr=v[v.费用周期=='年费']
print('avg monthly 月费',mon.mean(),'months',len(mon),'年费 total',yr.金额.sum(),'span months',v.月份.nunique())
with pd.ExcelWriter('expense_summary.xlsx') as w:
    tot.to_excel(w,sheet_name='每月總額');cyc.to_excel(w,sheet_name='依費用週期');acc.to_excel(w,sheet_name='依付款帳戶');top.to_excel(w,sheet_name='每月Top5',index=False)
    r.to_excel(w,sheet_name='訂閱項目',index=False);df.to_excel(w,sheet_name='原始資料',index=False);pd.DataFrame({'項目':['9月月费合计','年费总额/12','估計每月固定基線'],'金額':[45097.80,round(52948.25/12,2),round(45097.80+52948.25/12,2)]}).to_excel(w,sheet_name='固定基線',index=False)
