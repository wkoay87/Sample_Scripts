AGM_SQL = '''
SELECT DISTINCT AA.AGMT_NUM, att.arrg_type_desc,ws.subj_desc  FROM all_agreements aa
join desg_interests di on aa.arrg_key = di.arrg_key
join all_agreements aa2 on aa.arrg_key = aa2.arrg_prnt_key
join desg_interests di2 on aa2.arrg_key = di2.arrg_key 
join arrangement_types att on aa.arrg_type_code = att.arrg_type_code
join workspace_subject ws on aa.subj_code = ws.subj_code
where aa.arrg_dscr = 'AGM' and aa2.arrg_dscr <> 'AGM'  AND ARRG_STAT_CODE = 'A'
and not exists (SELECT 0 FROM DESG_INTERESTS DI3 JOIN QCTRL_ACQUISITION_CODES QC ON DI3.PRTP_KEY = QC.PRTP_KEY WHERE QC.ACQ_CD = 'TLW' AND AA.ARRG_KEY = DI3.ARRG_KEY)
AND SUBJ_CODE  NOT IN ('MAG') order by 1,2
'''

ARE_SQL = r'''
SELECT distinct AA.AGMT_NUM,AA.SUBS_NUM,ATT.ARRG_TYPE_DESC, ws.subj_desc FROM all_agreements aA
join desg_interests di on aa.arrg_key = di.arrg_key
join all_agreements aa2 on aa.arrg_key = aa2.arrg_prnt_key
join desg_interests di2 on aa2.arrg_key = di2.arrg_key 
join arrangement_types att on aa.arrg_type_code = att.arrg_type_code
join workspace_subject ws on aa.subj_code = ws.subj_code
where aa.arrg_dscr = 'ARE' and aa2.arrg_dscr IN ('DEP')  AND SUBJ_CODE  NOT IN ('MAG') AND ARRG_STAT_CODE = 'A'
AND NOT EXISTS (SELECT 0 FROM DESG_INTERESTS DI2 JOIN QCTRL_ACQUISITION_CODES QC ON DI2.PRTP_KEY = QC.PRTP_KEY WHERE QC.ACQ_CD = 'TLW' AND AA.ARRG_KEY = DI2.ARRG_KEY)
ORDER BY 1,2 
'''

DND_SQL = r"""
    SELECT DISTINCT
  A.AGMT_NUM,
  R.DOC_ID,
  CASE WHEN to_char(AL.UPDT_DATE,'YYYY-MM-DD') = to_char(R.LOG_DT,'YYYY-MM-DD') THEN 'AGREEMENT' ELSE 'DATE & DOC' END What_Modified,
  CASE WHEN to_char(AL.UPDT_DATE,'YYYY-MM-DD') = to_char(R.LOG_DT,'YYYY-MM-DD') THEN TO_CHAR(AL.UPDT_DATE,'MM-DD-YYYY') ELSE TO_CHAR(SDL.UPDT_DATE,'MM-DD-YYYY') END When_Modified,
  CASE WHEN to_char(AL.UPDT_DATE,'YYYY-MM-DD') = to_char(R.LOG_DT,'YYYY-MM-DD') THEN AL.UPDT_OPER ELSE SDL.UPDT_OPER END Who_Modified
FROM QTRAN_DOCMGMT_DOC_RESET R
LEFT OUTER JOIN DOC_HEADER DH ON
RTRIM(R.DOC_ID) = DH.DOC_PATH
LEFT OUTER JOIN DOC_STIP_DATE_RLTN DXREF ON
DH.DOC_KEY = DXREF.DOC_KEY
LEFT OUTER JOIN STIPULATION_DATE SD ON
DXREF.STIP_KEY = SD.STIP_KEY
LEFT OUTER JOIN ALL_AGREEMENTS A ON
SD.ARRG_KEY = A.ARRG_KEY
LEFT OUTER JOIN ALL_AGREEMENTS_LOG AL ON
A.ARRG_KEY = AL.ARRG_KEY
LEFT OUTER JOIN STIPULATION_DATE_LOG SDL ON
SD.STIP_KEY = SDL.STIP_KEY
WHERE R.LOG_DT BETWEEN SYSDATE - 8 AND SYSDATE
AND TO_CHAR(R.LOG_DT,'YYYY-MM-DD') < TO_CHAR(SYSDATE,'YYYY-MM-DD')
AND (TO_CHAR(R.LOG_DT,'YYYY-MM-DD') = TO_CHAR(SDL.UPDT_DATE,'YYYY-MM-DD') OR
    TO_CHAR(R.LOG_DT,'YYYY-MM-DD') = TO_CHAR(AL.UPDT_DATE,'YYYY-MM-DD'))
AND CASE WHEN to_char(AL.UPDT_DATE,'YYYY-MM-DD') = to_char(R.LOG_DT,'YYYY-MM-DD') THEN AL.UPDT_OPER ELSE SDL.UPDT_OPER END <> 'BSEC\QPECUSER'
ORDER BY WHEN_MODIFIED,A.AGMT_NUM, DOC_ID, WHO_MODIFIED
 """


HARTZ_KEA_SQL = r"""
    SELECT 
    GP.PROP_NO    PROP_NO,
    GP.PROP_NM    PROP_NAME,
    GP.ACQ_NO    ACQ_NO,
    ST.ALT_ST_CD   STATE,
    GC.CNTY_DESCR   CNTY,
    GW.WELL_STAT_DESCR  COMPLETION_STATUS,
    PW.API_WELL_NO    API_NO,
    DD.BA_NO    BA_NO,
    CASE WHEN DD.INT_TYPE_CD = 'IO' THEN 'OR'
      WHEN DD.INT_TYPE_CD IN ('IR','RI','NR') THEN 'RI'
      WHEN DD.INT_TYPE_CD = 'WI' AND DD.DO_TYPE_CD = 'JIB' THEN 'GWI'
      WHEN DD.INT_TYPE_CD = 'WI' AND DD.DO_TYPE_CD <> 'JIB' THEN 'WI'
    ELSE DD.INT_TYPE_CD
    END INT_TYPE,
    DD.NRI_DEC PCT_INT,
    GPA.DEV_YR  DEV_YR,
    PFP.FLD_NM  FIELD_NAME,
    PR.RESVR_NM RESVR_NM,
    /*CASE WHEN PR.RESVR_NM IS NOT NULL THEN PR.RESVR_NM
      WHEN PT.PLAY_TREND_DESCR IS NOT NULL THEN UPPER(PT.PLAY_TREND_DESCR)
     ELSE 'N/A'
    END RESVR_DESCR,*/
    GB.BA_NM1 OPERATOR,
    CONVERT(VARCHAR(10),PWC.EFF_DT_FROM,101) AS [MM/DD/YYYY] 
    --PW.UPDT_DT,
    --PWC.EFF_DT_FROM
    FROM GONL_PROP  GP
    JOIN GCDE_ST ST ON GP.ST_CD = ST.ST_CD 
    JOIN GCDE_CNTY GC ON GP.CNTY_CD = GC.CNTY_CD AND ST.ST_CD = GC.ST_CD
    JOIN PONL_WELL PW ON GP.PROP_NO = PW.WELL_NO
    JOIN PONL_WELL_COMPL PWCL ON PW.WELL_NO = PWCL.WELL_NO 
    JOIN PONL_WELL_COMPL_EFF_DT PWC ON PW.WELL_NO = PWC.WELL_NO 
    JOIN GCDE_WELL_STAT GW ON PWC.WELL_STAT_CD = GW.WELL_STAT_CD AND GW.PRODUCING_FL = 'Y'
    JOIN (SELECT PROP_NO,BA_NO, INT_TYPE_CD, NRI_DEC,DO_TYPE_CD FROM DONL_DO_DETAIL D1 WHERE  BA_NO NOT IN ('999999') AND INT_TYPE_CD <> 'IO' 
       UNION
       SELECT PROP_NO,BA_NO, INT_TYPE_CD, NRI_DEC,DO_TYPE_CD FROM DONL_DO_DETAIL D2 WHERE BA_NO NOT IN ('999999') AND INT_TYPE_CD = 'IO' 
       AND EXISTS (SELECT 0 AS TIER FROM DONL_DO_DETAIL D3 WHERE D2.PROP_NO = D3.PROP_NO 
       GROUP BY D3.PROP_NO HAVING D2.TIER = MAX(D3.TIER))) DD ON DD.PROP_NO = GP.PROP_NO AND INT_TYPE_CD <> 'DI'
    JOIN GONL_PROP_ADDL GPA ON GP.PROP_NO = GPA.PROP_NO
    JOIN PONL_FLD PFP ON PWCL.FLD_NO = PFP.FLD_NO
    LEFT OUTER JOIN PONL_RESVR PR ON PWCL.RESVR_NO = PR.RESVR_NO
    /*LEFT OUTER JOIN GCDE_PLAY_TREND PT ON GPA.PLAY_TREND_CD = PT.PLAY_TREND_CD*/
    --JOIN GCDE_PLAY_TREND GPT ON GPA.PLAY_TREND_CD = GPT.PLAY_TREND_CD
    JOIN GONL_PROP_EFF_DT GPE ON GP.PROP_NO = GPE.PROP_NO
    JOIN GONL_BA GB ON GPE.BA_NO = GB.BA_NO
    --JOIN (SELECT WELL_NO, PWC2.WELL_STAT_CD, MIN(EFF_DT_FROM) EFF_DT_FROM FROM PONL_WELL_COMPL_EFF_DT PWC2  GROUP BY PWC2.WELL_NO,PWC2.WELL_STAT_CD) WT ON PW.WELL_NO = WT.WELL_NO AND PWC.WELL_STAT_CD = WT.WELL_STAT_CD
    WHERE GP.PROP_STAT_CD = 'A' 
    AND NOT EXISTS (SELECT 0 FROM [BSM_ROLLUP].[dbo].[ROLLUP_PROP_XREF] OLD_PROP WHERE GP.PROP_NO = OLD_PROP.FROM_PROP) --This is only required for April well master
    AND DD.BA_NO IN ('034096')
    AND PWC.EFF_DT_FROM BETWEEN
 """


KEA_SQL = """
    SELECT 
    GP.PROP_NO    PROP_NO,
    GP.PROP_NM    PROP_NAME,
    GP.ACQ_NO    ACQ_NO,
    ST.ALT_ST_CD   STATE,
    GC.CNTY_DESCR   CNTY,
    GW.WELL_STAT_DESCR  COMPLETION_STATUS,
    PW.API_WELL_NO    API_NO,
    DD.BA_NO    BA_NO,
    CASE WHEN DD.INT_TYPE_CD = 'IO' THEN 'OR'
      WHEN DD.INT_TYPE_CD IN ('IR','RI','NR') THEN 'RI'
      WHEN DD.INT_TYPE_CD = 'WI' AND DD.DO_TYPE_CD = 'JIB' THEN 'GWI'
      WHEN DD.INT_TYPE_CD = 'WI' AND DD.DO_TYPE_CD <> 'JIB' THEN 'WI'
    ELSE DD.INT_TYPE_CD
    END INT_TYPE,
    DD.NRI_DEC PCT_INT,
    GPA.DEV_YR  DEV_YR,
    PFP.FLD_NM  FIELD_NAME,
    PR.RESVR_NM RESVR_NM,
    /*CASE WHEN PR.RESVR_NM IS NOT NULL THEN PR.RESVR_NM
      WHEN PT.PLAY_TREND_DESCR IS NOT NULL THEN UPPER(PT.PLAY_TREND_DESCR)
     ELSE 'N/A'
    END RESVR_DESCR,*/
    GB.BA_NM1 OPERATOR,
    CONVERT(VARCHAR(10),PWC.EFF_DT_FROM,101) AS [MM/DD/YYYY] 
    --PW.UPDT_DT,
    --PWC.EFF_DT_FROM
    FROM GONL_PROP  GP
    JOIN GCDE_ST ST ON GP.ST_CD = ST.ST_CD 
    JOIN GCDE_CNTY GC ON GP.CNTY_CD = GC.CNTY_CD AND ST.ST_CD = GC.ST_CD
    JOIN PONL_WELL PW ON GP.PROP_NO = PW.WELL_NO
    JOIN PONL_WELL_COMPL PWCL ON PW.WELL_NO = PWCL.WELL_NO 
    JOIN PONL_WELL_COMPL_EFF_DT PWC ON PW.WELL_NO = PWC.WELL_NO 
    JOIN GCDE_WELL_STAT GW ON PWC.WELL_STAT_CD = GW.WELL_STAT_CD AND GW.PRODUCING_FL = 'Y'
    JOIN (SELECT PROP_NO,BA_NO, INT_TYPE_CD, NRI_DEC,DO_TYPE_CD FROM DONL_DO_DETAIL D1 WHERE  BA_NO NOT IN ('999999') AND INT_TYPE_CD <> 'IO' 
       UNION
       SELECT PROP_NO,BA_NO, INT_TYPE_CD, NRI_DEC,DO_TYPE_CD FROM DONL_DO_DETAIL D2 WHERE BA_NO NOT IN ('999999') AND INT_TYPE_CD = 'IO' 
       AND EXISTS (SELECT 0 AS TIER FROM DONL_DO_DETAIL D3 WHERE D2.PROP_NO = D3.PROP_NO 
       GROUP BY D3.PROP_NO HAVING D2.TIER = MAX(D3.TIER))) DD ON DD.PROP_NO = GP.PROP_NO AND INT_TYPE_CD <> 'DI'
    JOIN GONL_PROP_ADDL GPA ON GP.PROP_NO = GPA.PROP_NO
    JOIN PONL_FLD PFP ON PWCL.FLD_NO = PFP.FLD_NO
    LEFT OUTER JOIN PONL_RESVR PR ON PWCL.RESVR_NO = PR.RESVR_NO
    /*LEFT OUTER JOIN GCDE_PLAY_TREND PT ON GPA.PLAY_TREND_CD = PT.PLAY_TREND_CD*/
    --JOIN GCDE_PLAY_TREND GPT ON GPA.PLAY_TREND_CD = GPT.PLAY_TREND_CD
    JOIN GONL_PROP_EFF_DT GPE ON GP.PROP_NO = GPE.PROP_NO
    JOIN GONL_BA GB ON GPE.BA_NO = GB.BA_NO
    --JOIN (SELECT WELL_NO, PWC2.WELL_STAT_CD, MIN(EFF_DT_FROM) EFF_DT_FROM FROM PONL_WELL_COMPL_EFF_DT PWC2  GROUP BY PWC2.WELL_NO,PWC2.WELL_STAT_CD) WT ON PW.WELL_NO = WT.WELL_NO AND PWC.WELL_STAT_CD = WT.WELL_STAT_CD
    WHERE GP.PROP_STAT_CD = 'A' 
    AND NOT EXISTS (SELECT 0 FROM [BSM_ROLLUP].[dbo].[ROLLUP_PROP_XREF] OLD_PROP WHERE GP.PROP_NO = OLD_PROP.FROM_PROP) --This is only required for April well master
    AND DD.BA_NO IN ('000002','000020','000035','000036','000101','000102','034096','000040')
    AND PWC.EFF_DT_FROM BETWEEN
 """

