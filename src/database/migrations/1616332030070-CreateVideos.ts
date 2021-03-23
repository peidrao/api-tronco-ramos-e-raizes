import {
  MigrationInterface,
  QueryRunner,
  Table
} from 'typeorm'

export default class CreateVideos1616332030070 implements MigrationInterface {
  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.createTable(
      new Table({
        name: 'videos',
        columns: [
          {
            name: 'id',
            type: 'varchar',
            isPrimary: true,
            generationStrategy: 'uuid'
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
          {
            name: 'user_id',
            type: 'varchar',
            isPrimary: true,
            generationStrategy: 'uuid'
          },

          { name: 'created_at', type: 'timestamp', default: 'now()' },
          { name: 'updated_at', type: 'timestamp', default: 'now()' }
        ]
      })
    )
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.dropTable('videos')
  }
}
