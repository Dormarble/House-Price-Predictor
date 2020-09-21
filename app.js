import config from './config'
import db, { connectDB } from './connection'
import { Complex } from './model/Complex'
import { Pyeong } from './model/Pyeong'

connectDB(config.development)
const connection = db.conn

// force: true 서버실행 시마다 테이블을 재생성
connection.sync({force: false})
.then(() => console.log("connect database successfully"))