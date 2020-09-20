import mysql from 'mysql'
import dotenv from 'dotenv'


dotenv.config()

const dbConfig = {
    host: process.env.DB_URL,
    port: process.env.DB_PORT,
    user: process.env.DB_USER,
    password: process.env.DB_PWD,
    database: process.env.DB_NAME
}

const connection = mysql.createConnection(dbConfig)

console.log("connecting to database...")
connection.connect(err => {
    if(err) {
        console.log(err)
        process.exit()
    }
    console.log("connected to database successfully!")
})



connection.end()

