import mysql from 'mysql'


const DISTRICT_TABLE = "district"

// option = {
//      columns: []  
// }
function getDistrictInfo(connection, option=null) {
    let columns = "*"
    if(option) {
        columns = option.columns.join(', ')
    }

    const query = `SELECT ${columns} FROM ${DISTRICT_TABLE}`

    return new Promise((resolve, reject) => {
        connection.query(query, (err, result, fields) => {
            if(err) reject(err)
            resolve(result)
        })
    })
}

export { getDistrictInfo }