import mysql from 'mysql'
import dotenv from 'dotenv'

import insertComplex from './dataInjector/insertComplexInfo'

dotenv.config()


const dbConfig = {
    host: process.env.DB_URL,
    port: process.env.DB_PORT,
    user: process.env.DB_USER,
    password: process.env.DB_PWD,
    database: process.env.DB_NAME
}

const connection = mysql.createConnection(dbConfig)

connection.connect()

insertComplex(connection)


connection.end()