import path from 'path'
import fs from 'fs'
import csv from 'csv-parser'
import iconv from 'iconv-lite'

import db from '../model';


export function insertTradeData() {
    const directoryPath = path.join(path.dirname(require.main.filename), 'tradeData');
    const files = fs.readdirSync(directoryPath)
    let count = 0

    files.forEach(fileName => {
        const filePath = path.join(directoryPath, fileName)
        const trades = []

        fs.createReadStream(filePath)
        .pipe(iconv.decodeStream('euc-kr'))
        .pipe(iconv.encodeStream('utf8'))
        .pipe(csv())
        .on('data', (trade) => trades.push(trade))
        .on('end', async () => {
            for(let trade of trades) {
                try {
                    const result = await storeTradeData(trade)
                    if(!result) continue
                    count++
                    console.log(`trade data is inserted to database! (count: ${count})`)
                } catch(err) {
                    console.log(`failed to insert trade data`)
                    console.log(err)
                    process.exit()
                }
            }
        })
    })

}

async function storeTradeData(tradeData) {
    if(!tradeData['계약년월'] && !tradeData['계약일'] && !tradeData['전용면적(㎡)'] && !tradeData['거래금액(만원)'] && !tradeData['번지']) {
        return false
    }
    let contactDateStr = tradeData['계약년월'] + '-' + (tradeData['계약일'].length==1 ? '0'+tradeData['계약일'] : tradeData['계약일'])
    contactDateStr = contactDateStr.slice(0, 4) + '-' + contactDateStr.slice(4)
    
    const newTrade = {
        address: tradeData['시군구'],
        detailAddress: tradeData['번지'],
        detailAddressMain: tradeData['본번'],
        detailAddressSub: tradeData['부번'],
        complexName: tradeData['단지명'],
        supplyArea: parseFloat(tradeData['전용면적(㎡)']),
        contactDate: new Date(contactDateStr) ,
        price: parseInt(tradeData['거래금액(만원)']),
        floor: parseInt(tradeData['층']),
        constructYear: parseInt(tradeData['건축년도']),
        roadAddress: tradeData['도로명']
    }

    const result = await db.Trade.create(newTrade)

    return result
}