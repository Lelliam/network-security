let $sql = require('./sql');
let MysqlPool = require('./mysql_pool');

let mysqlPool = new MysqlPool();
let pool = mysqlPool.getPool();

module.exports = {
    query: function (sql,res) {
        pool.getConnection(function(err, connection) {
            connection.query(sql, function(err, result) {
                if(err){
                    console.log(err);
                }
                res(result);
                connection.release();
            });
        });
    }
};

