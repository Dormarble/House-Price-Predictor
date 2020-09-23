import path from 'path'
import fs from 'fs'

import db from '../model'

export function insertComplexPyeongFromJSON() {
    const directoryPath = path.join(path.dirname(require.main.filename), 'dataJSON');
    const files = fs.readdirSync(directoryPath)
    let count = 0

    files.forEach(fileName => {
        const filePath = path.join(directoryPath, fileName)
        const JSONdata = JSON.parse(fs.readFileSync(filePath))

        storeJSONdata(JSONdata)
        .then(complexNo => {
            count++
            console.log(`complex#${complexNo} is inserted to database! (count: ${count})`)
        })
        .catch(err => {
            console.log(`failed to insert complex & pyeong`)
            console.log(err)
            process.exit()
        })
    })
}

async function storeJSONdata({complexPyeongDetailList, complexDetail}) {
    await storeComplex(complexDetail)
    for(let pyeongDetail of complexPyeongDetailList) {
        await storePyeong(pyeongDetail, complexDetail.complexNo)
    }
    return complexDetail.complexNo
}

async function storeComplex(complexDetail) {
    const newComplex = {
        complexNo: complexDetail.complexNo,
        complexName: complexDetail.complexName,
        cortarNo: complexDetail.cortarNo,
        realEstateTypeCode: complexDetail.realEstateTypeCode,
        realEstateTypeName: complexDetail.realEstateTypeName,
        detailAddress: complexDetail.detailAddress,
        roadAddress: complexDetail.roadAddress,
        latitude: complexDetail.latitude,
        longitude: complexDetail.longitude,
        totalHouseholdCount: complexDetail.totalHouseholdCount,
        totalLeaseHouseholdCount: complexDetail.totalLeaseHouseholdCount,
        permanentLeaseHouseholdCount: complexDetail.permanentLeaseHouseholdCount,
        nationLeaseHouseholdCount: complexDetail.nationLeaseHouseholdCount,
        civilLeaseHouseholdCount: complexDetail.civilLeaseHouseholdCount,
        publicLeaseHouseholdCount: complexDetail.publicLeaseHouseholdCount,
        longTermLeaseHouseholdCount: complexDetail.longTermLeaseHouseholdCount,
        etcLeaseHouseholdCount: complexDetail.etcLeaseHouseholdCount,
        highFloor: complexDetail.highFloor,
        lowFloor: complexDetail.lowFloor,
        completionYear: complexDetail.completionYearMonth ? complexDetail.completionYearMonth.slice(0, 4) : null,
        completionMonth: complexDetail.completionYearMonth ? complexDetail.completionYearMonth.slice(4) : null,
        totalDongCount: complexDetail.totalDongCount,
        maxSupplyArea: complexDetail.maxSupplyArea,
        minSupplyArea: complexDetail.minSupplyArea,
        dealCount: complexDetail.dealCount,
        rentCount: complexDetail.rentCount,
        leaseCount: complexDetail.leaseCount,
        shortTermRentCount: complexDetail.shortTermRentCount,
        isBookmarked: complexDetail.isBookmarked=="true",
        batlRatio: parseInt(complexDetail.batlRatio),
        btlRatio: parseInt(complexDetail.btlRatio),
        parkingCountByHousehold: complexDetail.parkingCountByHousehold,
        constructionCompanyName: complexDetail.constructionCompanyName,
        heatMethodTypeCode: complexDetail.heatMethodTypeCode,
        heatFuelTypeCode: complexDetail.heatFuelTypeCode,
        pyoengNames: complexDetail.pyoengNames,
        address: complexDetail.address,
        roadAddressPrefix: complexDetail.roadAddressPrefix
    }

    const result = await db.Complex.create(newComplex)

    return result
}

async function storePyeong(pyeongDetail, cmplxNo) {
    const newPyeong = {
        complexNo: cmplxNo,
        pyeongNo: pyeongDetail.pyeongNo,
        supplyArea: pyeongDetail.supplyAreaDouble,
        pyeongName: pyeongDetail.pyeongName,
        supplyPyeong: parseFloat(pyeongDetail.supplyPyeong),
        pyeongName2: pyeongDetail.pyeongName2,
        exclusiveArea: parseFloat(pyeongDetail.exclusiveArea),
        exclusivePyeong: parseFloat(pyeongDetail.exclusivePyeong),
        householdCountByPyeong: parseInt(pyeongDetail.householdCountByPyeong),
        realEstateTypeCode: pyeongDetail.realEstateTypeCode,
        exclusiveRate: parseFloat(pyeongDetail.exclusiveRate),
        entranceType: pyeongDetail.entranceType,
        minPrice: parseInt(pyeongDetail.landPriceMaxByPtp ? pyeongDetail.landPriceMaxByPtp.minPrice : null),
        maxPrice: parseInt(pyeongDetail.landPriceMaxByPtp ? pyeongDetail.landPriceMaxByPtp.maxPrice : null),
        propertyTotalTax: pyeongDetail.landPriceMaxByPtp ? pyeongDetail.landPriceMaxByPtp.landPriceTax.propertyTotalTax : null,
        propertyTax: pyeongDetail.landPriceMaxByPtp ? pyeongDetail.landPriceMaxByPtp.landPriceTax.propertyTax : null,
        localEduTax: pyeongDetail.landPriceMaxByPtp ? pyeongDetail.landPriceMaxByPtp.landPriceTax.localEduTax : null,
        cityAreaTax: pyeongDetail.landPriceMaxByPtp ? pyeongDetail.landPriceMaxByPtp.landPriceTax.cityAreaTax : null,
        realEstateTotalTax: pyeongDetail.landPriceMaxByPtp ? pyeongDetail.landPriceMaxByPtp.landPriceTax.realEstateTotalTax : null,
        decisionTax: pyeongDetail.landPriceMaxByPtp ? pyeongDetail.landPriceMaxByPtp.landPriceTax.decisionTax : null,
        ruralSpecialTax: pyeongDetail.landPriceMaxByPtp ? pyeongDetail.landPriceMaxByPtp.landPriceTax.ruralSpecialTax : null,
        roomCnt: pyeongDetail.roomCnt,
        bathroomCnt: pyeongDetail.bathroomCnt
    }
    const result = await db.Pyeong.create(newPyeong)

    return result
}
