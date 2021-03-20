import { getRepository, Repository } from 'typeorm'
import CreateUserDTO from '../../dtos/CreateUserDTO'
import User from '../../models/User'
import IUsersRepository from './interfaces/IUsersRepository'

export default class UserRepository implements IUsersRepository {
  private ormRepository: Repository<User>;

  constructor() {
    this.ormRepository = getRepository(User)
  }

  public async findByName(name: string): Promise<User | undefined> {
    const userName = await this.ormRepository.findOne({ where: { name } })
    return userName
  }

  public async findById(id: string): Promise<User | undefined> {
    const userId = await this.ormRepository.findOne({ where: { id } })
    return userId
  }

  public async findByEmail(email: string): Promise<User | undefined> {
    const userEmail = await this.ormRepository.findOne({ where: { email } })
    return userEmail
  }

  public async findAll(): Promise<User[]> {
    const users = await this.ormRepository.find()
    return users
  }

  public async create({ name, email, password }: CreateUserDTO): Promise<User> {
    const user = await this.ormRepository.create({ name, email, password })
    await this.ormRepository.save(user)
    return user
  }

  public save(user: User): Promise<User> {
    return this.ormRepository.save(user)
  }

  public async delete(id: string): Promise<void> {
    this.ormRepository.delete(id)
  }
}
