import Sequelize from 'sequelize'

const db = {}

export function connectDB(dbConfig) {
    db.conn = new Sequelize(
        dbConfig.dbName, 
        dbConfig.dbUser, 
        dbConfig.dbPwd, 
        {
            host: dbConfig.dbHost,
            dialect: dbConfig.dbEngine
        }
    )
}

export default db