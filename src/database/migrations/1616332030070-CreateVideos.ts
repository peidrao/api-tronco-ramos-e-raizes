import { MigrationInterface, QueryRunner, Table } from 'typeorm'

export default class CreateVideos1616332030070 implements MigrationInterface {
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
            name: 'user_id',
            type: 'varchar',
            generationStrategy: 'uuid'
          },

          {
            name: 'title',
            type: 'varchar'
          },
          {
            name: 'link',
            type: 'varchar'
          },
          {
            name: 'description',
            type: 'text'
          },
          { name: 'created_at', type: 'timestamp', default: 'now()' },
          { name: 'updated_at', type: 'timestamp', default: 'now()' }
        ],
        foreignKeys: [
          {
            name: 'VideosByUsers',
            columnNames: ['user_id'],
            referencedColumnNames: ['id'],
            referencedTableName: 'users',
            onDelete: 'SET NULL',
            onUpdate: 'CASCADE'
          }
        ]
      })
    )
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.dropTable('videos')
  }
}
