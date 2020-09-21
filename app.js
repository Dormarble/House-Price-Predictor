import db from './model'

const connection = db.conn

// force: true 서버실행 시마다 테이블을 재생성
connection.sync({force: false})
.then(() => console.log("connect database successfully"))