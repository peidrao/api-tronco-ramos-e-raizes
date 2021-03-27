import { Column, CreateDateColumn, Entity, JoinColumn, ManyToOne, PrimaryGeneratedColumn, UpdateDateColumn } from 'typeorm'
import User from './User'

@Entity('audios')
export default class Audio {
  @PrimaryGeneratedColumn('uuid')
  id: string

  @Column()
  title: string

  @Column()
  author: string

  @Column()
  audio: string

  @Column()
  user_id: string

  @ManyToOne(() => User, user => user, { eager: true })
  @JoinColumn({ name: 'user_id' })
  User: User

  @CreateDateColumn()
  created_at: string

  @UpdateDateColumn()
  updated_at: string
}
