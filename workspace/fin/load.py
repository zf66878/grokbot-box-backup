import pandas as pd
a='有成导出封存/有成2026账套导出_封存_20260906.xlsx'; b='有成导出封存/有成老账套2019-2025导出_封存_20260907.xlsx'
v=pd.concat([pd.read_excel(b,sheet_name='凭证分录').rename(columns={'辅助核算':'aux'}),pd.read_excel(a,sheet_name='凭证分录').rename(columns={'辅助核算(主体/职员等)':'aux'})])
v['d']=pd.to_datetime(v['凭证日期']); v=v[(v.d>='2025-10-01')&(v.d<'2026-09-01')]
v['m']=v.d.dt.strftime('%Y-%m'); v['code']=v['科目编码'].astype(str)
j=pd.concat([pd.read_excel(b,sheet_name='日记账'),pd.read_excel(a,sheet_name='日记账')])
def cat(n):
    for k,c in [('房租','房租'),('物业','物业'),('工资','工资社保'),('社保','工资社保'),('公积金','工资社保'),('员工保险','工资社保'),('课时','课时费'),('水电','水电'),('技术服务','软件订阅/技术服务'),('装修','装修维修(非固定)'),('维修','装修维修(非固定)'),('折旧','折旧(非现金)')]:
        if k in n: return c
    return '其他'
def ent(n):
    return '祁绩' if '滨江民非' in n else ('百佳' if '百佳艺术' in n else ('其他主体' if any(x in n for x in ['维特思','萧山','_滨江']) else '未分主体'))
e=v[v.code.str.match(r'^(5|66)')&~v['摘要'].astype(str).str.contains('结转本期损益')].copy()
e['amt']=e['借方'].fillna(0)-e['贷方'].fillna(0)
e['cat']=e['科目全称'].map(cat); e['ent']=e['科目全称'].map(ent)
