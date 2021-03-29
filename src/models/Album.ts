import { Column, Entity, OneToMany, PrimaryGeneratedColumn } from 'typeorm'
import Image from './Image'

@Entity('albums')
export default class Album {
  @PrimaryGeneratedColumn('uuid')
  id: string

  @Column()
  title: string

  @Column()
  description: string

  @OneToMany(type => Image, image => image.album)
  images: Image[]
}
