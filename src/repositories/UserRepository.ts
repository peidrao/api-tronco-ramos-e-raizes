import { getRepository, Repository } from 'typeorm'
import CreateUserDTO from '../dtos/CreateUserDTO'
import User from '../models/User'
import IUsersRepository from './IUsersRepository'

export default class UserRepository implements IUsersRepository {
  private ormRepository: Repository<User>

  constructor () {
    this.ormRepository = getRepository(User)
  }

  public async findByName (name: string): Promise<User | undefined> {
    const user = await this.ormRepository.findOne({ where: name })
    return user
  }

  public async create ({ name, email, password }: CreateUserDTO): Promise<User> {
    const user = await this.ormRepository.create({ name, email, password })
    await this.ormRepository.save(user)
    return user
  }

  public save (user: User): Promise<User> {
    return this.ormRepository.save(user)
  }
}
