import { MigrationInterface, QueryRunner, Table, TableForeignKey } from 'typeorm'

export default class CreateDocument1616629452128 implements MigrationInterface {
  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.createTable(
      new Table({
        name: 'documents',
        columns: [
          {
            name: 'id',
            type: 'varchar',
            isPrimary: true,
            generationStrategy: 'uuid'
          },
          {
            name: 'document',
            type: 'varchar'
          },
          {
            name: 'title',
            type: 'varchar',
            isUnique: true
          },
          {
            name: 'author',
            type: 'varchar'
          },
          {
            name: 'user_id',
            type: 'varchar',
            isPrimary: true,
            generationStrategy: 'uuid'
          },
          {
            name: 'created_at',
            type: 'timestamp',
            default: 'now()'
          },
          {
            name: 'updated_at',
            type: 'timestamp',
            default: 'now()'
          }
        ]
      })
    )
    await queryRunner.createForeignKey('documents',
      new TableForeignKey({
        name: 'DocumentByUser',
        columnNames: ['user_id'],
        referencedTableName: 'users',
        referencedColumnNames: ['id']
      })
    )
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.dropForeignKey('documents', 'DocumentByUser')
    await queryRunner.dropTable('documents')
  }
}
