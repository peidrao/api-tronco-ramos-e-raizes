import { MigrationInterface, QueryRunner, Table, TableForeignKey } from 'typeorm'

export default class CreateAudio1616802322819 implements MigrationInterface {
  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.createTable(new Table({
      name: 'audios',
      columns: [
        { name: 'id', type: 'varchar', isPrimary: true, generationStrategy: 'uuid' },
        { name: 'title', type: 'varchar' },
        { name: 'author', type: 'varchar' },
        { name: 'audio', type: 'varchar', isUnique: true },
        { name: 'user_id', type: 'varchar', isPrimary: true, generationStrategy: 'uuid' },
        { name: 'created_at', type: 'timestamp', default: 'now()' },
        { name: 'updated_at', type: 'timestamp', default: 'now()' }
      ]
    }))

    await queryRunner.createForeignKey('audios',
      new TableForeignKey({
        name: 'UserByAudio',
        columnNames: ['user_id'],
        referencedTableName: 'users',
        referencedColumnNames: ['id']
        // onDelete: 'CASCADE'
      }))
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.dropForeignKey('audios', 'UserByAudio')
    await queryRunner.dropTable('audios')
  }
}
