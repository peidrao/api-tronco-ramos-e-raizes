# Museu TRR

```
❯ yarn typeorm migration:run
yarn run v1.22.10
$ ts-node-dev ./node_modules/typeorm/cli.js migration:run
[INFO] 10:25:24 ts-node-dev ver. 1.1.6 (using ts-node ver. 9.1.1, typescript ver. 3.9.6)
query: SELECT * FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA` = 'db' AND `TABLE_NAME` = 'migrations'
query: SELECT * FROM `db`.`migrations` `migrations`  ORDER BY `id` DESC
1 migrations are already loaded in the database.
2 migrations were found in the source code.
CreateUsers1616180471505 is the last executed migration. It was executed on Fri Mar 19 2021 16:01:11 GMT-0300 (Brasilia Standard Time).
1 migrations are new migrations that needs to be executed.
query: START TRANSACTION
query: CREATE TABLE `videos` (`id` varchar(36) NOT NULL, `user_id` varchar(36) NOT NULL, `title` varchar(255) NOT NULL, `link` varchar(255) NOT NULL, `description` text NOT NULL, `created_at` timestamp NOT NULL DEFAULT now(), `updated_at` timestamp NOT NULL DEFAULT now(), CONSTRAINT `VideosByUsers` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE CASCADE, PRIMARY KEY (`id`)) ENGINE=InnoDB
query failed: CREATE TABLE `videos` (`id` varchar(36) NOT NULL, `user_id` varchar(36) NOT NULL, `title` varchar(255) NOT NULL, `link` varchar(255) NOT NULL, `description` text NOT NULL, `created_at` timestamp NOT NULL DEFAULT now(), `updated_at` timestamp NOT NULL DEFAULT now(), CONSTRAINT `VideosByUsers` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE CASCADE, PRIMARY KEY (`id`)) ENGINE=InnoDB
error: Error: ER_CANNOT_ADD_FOREIGN: Cannot add foreign key constraint
    at Query.Sequence._packetToError (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/protocol/sequences/Sequence.js:47:14)
    at Query.ErrorPacket (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/protocol/sequences/Query.js:79:18)
    at Protocol._parsePacket (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/protocol/Protocol.js:291:23)
    at Parser._parsePacket (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/protocol/Parser.js:433:10)
    at Parser.write (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/protocol/Parser.js:43:10)
    at Protocol.write (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/protocol/Protocol.js:38:16)
    at Socket.<anonymous> (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/Connection.js:88:28)
    at Socket.<anonymous> (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/Connection.js:526:10)
    at Socket.emit (node:events:369:20)
    at addChunk (node:internal/streams/readable:313:12)
    --------------------
    at Protocol._enqueue (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/protocol/Protocol.js:144:48)
    at PoolConnection.query (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/Connection.js:198:25)
    at MysqlQueryRunner.<anonymous> (/home/peidrao/Repos/museu-trr-api/src/driver/mysql/MysqlQueryRunner.ts:182:36)
    at step (/home/peidrao/Repos/museu-trr-api/node_modules/tslib/tslib.js:141:27)
    at Object.next (/home/peidrao/Repos/museu-trr-api/node_modules/tslib/tslib.js:122:57)
    at fulfilled (/home/peidrao/Repos/museu-trr-api/node_modules/tslib/tslib.js:112:62)
    at processTicksAndRejections (node:internal/process/task_queues:94:5) {
  code: 'ER_CANNOT_ADD_FOREIGN',
  errno: 1215,
  sqlMessage: 'Cannot add foreign key constraint',
  sqlState: 'HY000',
  index: 0,
  sql: 'CREATE TABLE `videos` (`id` varchar(36) NOT NULL, `user_id` varchar(36) NOT NULL, `title` varchar(255) NOT NULL, `link` varchar(255) NOT NULL, `description` text NOT NULL, `created_at` timestamp NOT NULL DEFAULT now(), `updated_at` timestamp NOT NULL DEFAULT now(), CONSTRAINT `VideosByUsers` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE CASCADE, PRIMARY KEY (`id`)) ENGINE=InnoDB'
}
query: ROLLBACK
Error during migration run:
QueryFailedError: ER_CANNOT_ADD_FOREIGN: Cannot add foreign key constraint
    at new QueryFailedError (/home/peidrao/Repos/museu-trr-api/src/error/QueryFailedError.ts:9:9)
    at Query.<anonymous> (/home/peidrao/Repos/museu-trr-api/src/driver/mysql/MysqlQueryRunner.ts:193:37)
    at Query.<anonymous> (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/Connection.js:526:10)
    at Query._callback (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/Connection.js:488:16)
    at Query.Sequence.end (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/protocol/sequences/Sequence.js:83:24)
    at Query.ErrorPacket (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/protocol/sequences/Query.js:92:8)
    at Protocol._parsePacket (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/protocol/Protocol.js:291:23)
    at Parser._parsePacket (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/protocol/Parser.js:433:10)
    at Parser.write (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/protocol/Parser.js:43:10)
    at Protocol.write (/home/peidrao/Repos/museu-trr-api/node_modules/mysql/lib/protocol/Protocol.js:38:16) {
  code: 'ER_CANNOT_ADD_FOREIGN',
  errno: 1215,
  sqlMessage: 'Cannot add foreign key constraint',
  sqlState: 'HY000',
  index: 0,
  sql: 'CREATE TABLE `videos` (`id` varchar(36) NOT NULL, `user_id` varchar(36) NOT NULL, `title` varchar(255) NOT NULL, `link` varchar(255) NOT NULL, `description` text NOT NULL, `created_at` timestamp NOT NULL DEFAULT now(), `updated_at` timestamp NOT NULL DEFAULT now(), CONSTRAINT `VideosByUsers` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE CASCADE, PRIMARY KEY (`id`)) ENGINE=InnoDB',
  query: 'CREATE TABLE `videos` (`id` varchar(36) NOT NULL, `user_id` varchar(36) NOT NULL, `title` varchar(255) NOT NULL, `link` varchar(255) NOT NULL, `description` text NOT NULL, `created_at` timestamp NOT NULL DEFAULT now(), `updated_at` timestamp NOT NULL DEFAULT now(), CONSTRAINT `VideosByUsers` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE CASCADE, PRIMARY KEY (`id`)) ENGINE=InnoDB',
  parameters: []
}
error Command failed with exit code 1.
info Visit https://yarnpkg.com/en/docs/cli/run for documentation about this command.

```
