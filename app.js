import express from 'express'
import cors from 'cors'

import db from './model'
import config from './config'

const PORT = config.development.port || 3000

const app = express()

app.use(cors())
app.use(express.urlencoded({extended: true}))

db.conn.sync({force: false})        // force: true 서버실행 시마다 테이블을 재생성
.then(() => {
    console.log("connect database successfully")
    app.listen(PORT, () => console.log("express is running"))

    db.Complex.findAndCountAll().then(data => {
        console.log('Complex: ' + data.count)
    })
    db.Pyeong.findAndCountAll().then(data => {
        console.log('Pyeong: ' + data.count)
    })

})
.catch(err => {console.log("failed to connect database"); console.log(err)})

