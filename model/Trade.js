export default function(connection, DataTypes) {
    const Trade = connection.define('Trade', {
        address: {
            type: DataTypes.STRING(50),
            allowNull: false
        },
        detailAddress: {
            type: DataTypes.STRING(20),
            allowNull: false
        },
        detailAddressMain: DataTypes.STRING(10),
        detailAddressSub: DataTypes.STRING(10),
        complexName: DataTypes.STRING(50),
        supplyArea: {
            type: DataTypes.FLOAT,
            allowNull: false
        },
        contactDate: {
            type: DataTypes.DATE,
            allowNull: false
        },
        price: {
            type: DataTypes.BIGINT,
            allowNull: false
        },
        floor: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
        constructYear: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
        roadAddress: {
            type: DataTypes.STRING(50),
            allowNull: false
        }
    })

    Trade.associate = models => {
        
    }

    return Trade
}