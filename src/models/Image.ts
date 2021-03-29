import { Column, Entity, ManyToOne, PrimaryGeneratedColumn } from 'typeorm'
import Album from './Album'

@Entity('images')
export default class Image {
  @PrimaryGeneratedColumn('uuid')
  id: string

  @Column()
  title: string

  @Column()
  name: string

  @ManyToOne(type => Album, album => album.images)
  album: Album
}
