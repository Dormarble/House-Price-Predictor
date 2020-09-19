import xlsx from 'xlsx'

export default function(connection) {
    const districtFile = xlsx.readFile(__dirname + '../dataFiles/districtInfo.xls')
    const districtSheet = districtFile.Sheets[districtFile.SheetNames[0]]
    const districtData = xlsx.utils.sheet_to_json(districtSheet, { defval : "" })

    let sql = "INSERT INTO address (CITY, GU, ADMIN_DISTRICT_NM, ADMIN_DONG, CORTAR_DONG, ADMIN_DISTRICT_ID, ADMIN_IN_CODE, CORTAR_CODE) VALUES "

    for(let row of districtData) {
        const CITY = row['행정구역분류와 행정기관 및 법정동코드 연계표(2010.12.31기준)']
        const GU = row.__EMPTY
        const ADMIN_DISTRICT_NM = row.__EMPTY_1
        const ADMIN_DONG = row.__EMPTY_2
        const CORTAR_DONG = row.__EMPTY_3
        const ADMIN_DISTRICT_ID = row.__EMPTY_4
        const ADMIN_IN_CODE = row.__EMPTY_5
        const CORTAR_CODE = row.__EMPTY_6
        if(!(GU && ADMIN_DISTRICT_NM && ADMIN_DONG && CORTAR_DONG && ADMIN_DISTRICT_ID && ADMIN_IN_CODE)) continue
        const query = sql + `("${CITY}", "${GU}", "${ADMIN_DISTRICT_NM}", "${ADMIN_DONG}", "${CORTAR_DONG}", ${ADMIN_DISTRICT_ID}, ${ADMIN_IN_CODE}, ${CORTAR_CODE})`

        connection.query(query, (err, result, fields) => {
            if(err) console.dir(err)
            console.log(result)
        })
    }
}