import db from './model'

// force: true 서버실행 시마다 테이블을 재생성
db.conn.sync({force: false})
.then(() => console.log("connect database successfully"))
.catch(err => {console.log("failed to connect database"); console.log(err)})

import { insertComplexPyeongFromJSON } from './dbController/insertData'
insertComplexPyeongFromJSON()