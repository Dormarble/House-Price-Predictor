import Sequelize from 'sequelize'

import config from '../config'
import defineComplex from './Complex'
import definePyeong from './Pyeong'
import defineTrade from './Trade'

const db = {}

const dbConfig = config.development
const connection = new Sequelize(
    dbConfig.dbName, 
    dbConfig.dbUser, 
    dbConfig.dbPwd, 
    {
        host: dbConfig.dbHost,
        dialect: dbConfig.dbEngine,
        logging: false
    }
)
db.conn = connection
db.Complex = defineComplex(connection, Sequelize)
db.Pyeong = definePyeong(connection, Sequelize)
db.Trade = defineTrade(connection, Sequelize)


db.Complex.associate(db)
db.Pyeong.associate(db)
db.Trade.associate(db)

export default db