import { Column, CreateDateColumn, Entity, JoinColumn, ManyToOne, OneToMany, PrimaryGeneratedColumn, UpdateDateColumn } from 'typeorm'
import Image from './Image'
import User from './User'

@Entity('albums')
export default class Album {
  @PrimaryGeneratedColumn('uuid')
  id: string

  @Column()
  title: string

  @Column()
  description: string

  @OneToMany(() => Image, image => image.album)
  @JoinColumn({ name: 'image_id' })
  images: Image[]

  @ManyToOne(() => User)
  @JoinColumn({ name: 'user_id' })
  user_id: User

  @CreateDateColumn()
  created_at: Date;

  @UpdateDateColumn()
  updated_at: Date;
}
