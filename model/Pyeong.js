export default function(connection, DataTypes) {
    const Pyeong = connection.define('Pyeong', {
        complexNo: {
            type: DataTypes.STRING(10),
            allowNull: false
        },
        pyeongNo: {
            type: DataTypes.STRING(2),
            allowNull: false
        },
        supplyArea: {
            type: DataTypes.FLOAT,
            allowNull: false
        },
        pyeongName: {
            type: DataTypes.STRING(10),
            allowNull: false
        },
        supplyPyeong: DataTypes.FLOAT,
        pyeongName2: DataTypes.STRING(10),
        exclusiveArea: DataTypes.FLOAT,
        exclusivePyeong: DataTypes.FLOAT,
        householdCountByPyeong: DataTypes.INTEGER,
        realEstateTypeCode: {
            type: DataTypes.STRING(5),
            allowNull: false
        },
        exclusiveRate: DataTypes.FLOAT,
        entranceType: DataTypes.STRING(10),

        //landPriceMaxByPtp
        minPrice: DataTypes.BIGINT,
        maxPrice: DataTypes.BIGINT,

        //landPriceMaxByPtp.landPriceTax
        propertyTotalTax: DataTypes.INTEGER,
        propertyTax: DataTypes.INTEGER,
        localEduTax: DataTypes.INTEGER,
        cityAreaTax: DataTypes.INTEGER,
        realEstateTotalTax: DataTypes.INTEGER,
        decisionTax: DataTypes.INTEGER,
        ruralSpecialTax: DataTypes.INTEGER,

        roomCnt: DataTypes.INTEGER,
        bathroomCnt: DataTypes.INTEGER
    },
    {
        timestamps: true,
        underscored: false
    })

    Pyeong.associate = models => {
        Pyeong.belongsTo(models.Complex, {
            foreignKey: 'complexNo'
        })
    }

    return Pyeong
}