import {
  MigrationInterface,
  QueryRunner,
  Table,
  TableColumn,
  TableForeignKey
} from 'typeorm'

export default class CreateVideos1616332030070 implements MigrationInterface {
  /*   private foreignKey = new TableForeignKey({
    name: 'VideosByUsers',
    columnNames: ['user_id'],
    referencedColumnNames: ['id'],
    referencedTableName: 'users',
    onDelete: 'SET NULL',
    onUpdate: 'CASCADE'
  });
 */
  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.createTable(
      new Table({
        name: 'videos',
        columns: [
          {
            name: 'id',
            type: 'varchar',
            generationStrategy: 'uuid',
            isPrimary: true
          },
          {
            name: 'title',
            type: 'varchar'
          },
          {
            name: 'link',
            type: 'varchar',
            isUnique: true
          },
          {
            name: 'description',
            type: 'text'
          },
          /*    {
          name: 'user_id',
          type: 'varchar',
          generationStrategy: 'uuid'
        }, */

          { name: 'created_at', type: 'timestamp', default: 'now()' },
          { name: 'updated_at', type: 'timestamp', default: 'now()' }
        ]
      })
    )

    await queryRunner.addColumn(
      'videos',
      new TableColumn({
        name: 'user_id',
        type: 'varchar',
        generationStrategy: 'uuid'
      })
    )

    await queryRunner.createForeignKey('videos',
      new TableForeignKey({
        name: 'VideoUser',
        columnNames: ['user_id'],
        referencedColumnNames: ['id'],
        referencedTableName: 'users',
        onDelete: 'CASCADE'
        // onUpdate: 'SET NULL'
      })
    )
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.dropForeignKey('videos', 'VideoUser')
    await queryRunner.dropColumn('videos', 'user_id')
    await queryRunner.dropTable('videos')
  }
}
