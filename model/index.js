import Sequelize from 'sequelize'

import config from '../config'

const db = {}

const dbConfig = config.development
db.conn = new Sequelize(
    dbConfig.dbName, 
    dbConfig.dbUser, 
    dbConfig.dbPwd, 
    {
        host: dbConfig.dbHost,
        dialect: dbConfig.dbEngine
    }
)

export default db