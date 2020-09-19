import fs from "fs"
import { getDistrictInfo } from "../databaseInterface/databaseInterface"

export default async function(connection) {
    const complexInfoFile = __dirname + '/../dataFiles/complexInfo.json'

    const districtInfo = await getDistrictInfo(connection, {columns: ["ID", "NAME"]})
    console.log(districtInfo)
    const {DESCRIPTION, DATA} = JSON.parse(fs.readFileSync(complexInfoFile))

    const sql = `
        INSERT INTO complex (APT_CODE, APT_NM, CODEAPTNM, APTADDR, DOROJUSO, 
                            ADRES_CITY, ADRES_GU, ADRES_DONG, ADRES_RMNDR, 
                            ADRES_DORO, ADRES_DORO_RMNDR, TELNO, HSHLDR_TY, 
                            GNRL_MANAGECT_MANAGE_STLE, CRRDPR_TY, HEAT_MTHD, 
                            ALL_DONG_CO, ALL_HSHLD_CO, CO_WO, CO_EX, USE_INSPCT_DE, 
                            TOTAR, PRIVAREA, MANAGECT_LEVY_AR, KAPTMPAREA60, 
                            KAPTMPAREA85, KAPTMPAREA135, KAPTMPAREA136, API_UPDATE_DATE, 
                            EXPENSCTMANAGESTLE, HSHLD_ELCTY_CNTRCT_MTH, BU_AR, 
                            CNT_PA, GUBUN, USE_CONFM_DE)    
        VALUES
    `
    for(let row of DATA) {
        const APT_CODE = row.apt_code
        const APT_NM = row.apt_nm
        const CODEAPTNM = row.codeaptnm
        const APTADDR = row.kaptaddr
        const DOROJUSO = row.dorojuso
        const ADRES_CITY = row.adres_city
        const ADRES_GU = row.adres_gu
        const ADRES_DONG = row.adres_dong
        const ADRES_RMNDR = row.adres_rmndr
        const ADRES_DORO = row.adres_doro
        const ADRES_DORO_RMNDR = row.adres_doro_rmndr
        const TELNO = row.telno
        const HSHLDR_TY = row.hshldr_ty
        const GNRL_MANAGECT_MANAGE_STLE = row.gnrl_managect_manage_stle
        const CRRDPR_TY = row.crrdpr_ty
        const HEAT_MTHD = row.heat_mthd
        const ALL_DONG_CO = row.all_dong_co
        const ALL_HSHLD_CO = row.all_hshld_co
        const CO_WO = row.co_wo
        const CO_EX = row.co_ex
        const USE_INSPCT_DE = row.use_inspct_de
        const TOTAR = row.totar
        const PRIVAREA = row.privarea
        const MANAGECT_LEVY_AR = row.managect_levy_ar
        const KAPTMPAREA60 = row.kaptmparea60
        const KAPTMPAREA85 = row.kaptmparea85
        const KAPTMPAREA135 = row.kaptmparea135
        const KAPTMPAREA136 = row.kaptmparea136
        const API_UPDATE_DATE = new Date(row.api_update_date)
        const EXPENSCTMANAGESTLE = row.expensctmanagestle
        const HSHLD_ELCTY_CNTRCT_MTH = row.hshld_elcty_cntrct_mth
        const BU_AR = row.bu_ar
        const CNT_PA = row.cnt_pa
        const GUBUN = row.gubun
        const USE_CONFM_DE = new Date(row.use_confm_de)

        const query = `
                ("${APT_CODE}", "${APT_NM}", ${CODEAPTNM}, "${APTADDR}", "${DOROJUSO}", 
                ${ADRES_CITY}, ${ADRES_GU}, ${ADRES_DONG}, "${ADRES_RMNDR}", 
                "${ADRES_DORO}", "${ADRES_DORO_RMNDR}", "${TELNO}", ${HSHLDR_TY}, 
                ${GNRL_MANAGECT_MANAGE_STLE}, ${CRRDPR_TY}, ${HEAT_MTHD}, 
                ${ALL_DONG_CO}, ${ALL_HSHLD_CO}, "${CO_WO}", "${CO_EX}", ${USE_INSPCT_DE}, 
                ${TOTAR}, ${PRIVAREA}, ${MANAGECT_LEVY_AR}, ${KAPTMPAREA60}, 
                ${KAPTMPAREA85}, ${KAPTMPAREA135}, ${KAPTMPAREA136}, ${API_UPDATE_DATE}, 
                ${EXPENSCTMANAGESTLE}, ${HSHLD_ELCTY_CNTRCT_MTH}, ${BU_AR}, 
                ${CNT_PA}, ${GUBUN}, ${USE_CONFM_DE}) 
            `
    }
}