import {
  Column,
  CreateDateColumn,
  Entity,
  JoinColumn,
  ManyToOne,
  PrimaryGeneratedColumn,
  UpdateDateColumn
} from 'typeorm'
import User from './User'

@Entity('videos')
export default class Video {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column()
  title: string;

  @Column()
  description: string;

  @Column()
  link: string

  @Column()
  user_id: string;

  @ManyToOne(() => User, user => user, { eager: true })
  @JoinColumn({ name: 'user_id' })
  user: User

  @CreateDateColumn()
  created_at: Date;

  @UpdateDateColumn()
  updated_at: Date;
}
