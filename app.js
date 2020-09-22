import express from 'express'

import db from './model'
import config from './config'

const PORT = config.development.port || 3000

const app = express()

// force: true 서버실행 시마다 테이블을 재생성
db.conn.sync({force: false})
.then(() => {
    console.log("connect database successfully")
    app.listen(PORT, () => console.log("express is running"))
})
.catch(err => {console.log("failed to connect database"); console.log(err)})

db.Complex.findAndCountAll().then(data => {
    console.log('Complex: ' + data.count)
})
db.Pyeong.findAndCountAll().then(data => {
    console.log('Pyeong: ' + data.count)
})