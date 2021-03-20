import CreateUserDTO from '../../../dtos/CreateUserDTO'
import User from '../../../models/User'

export default interface IUsersRepository {
  findByName(name: string): Promise<User | undefined>;
  findByEmail(email: string): Promise<User | undefined>;
  findById(id: string): Promise<User | undefined>;
  findAll(): Promise<User[]>;
  create(user: CreateUserDTO): Promise<User>;
  delete(id: string): Promise<void>;
  save(user: User): Promise<User>;
}
