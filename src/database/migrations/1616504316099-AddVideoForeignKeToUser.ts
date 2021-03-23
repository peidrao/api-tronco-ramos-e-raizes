import { MigrationInterface, QueryRunner, TableForeignKey } from 'typeorm'

export default class AddVideoForeignKeToUser1616504316099 implements MigrationInterface {
  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.createForeignKey(
      'videos',
      new TableForeignKey({
        name: 'VideoByUser',
        columnNames: ['user_id'],
        referencedColumnNames: ['id'],
        referencedTableName: 'users',
        onDelete: 'CASCADE'
        // onUpdate: 'CASCADE'
      })
    )
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.dropForeignKey('videos', 'VideoByUser')
  }
}
