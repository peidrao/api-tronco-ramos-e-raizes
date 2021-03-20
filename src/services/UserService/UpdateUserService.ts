import { hash } from 'bcryptjs'
import AppError from '../../errors/AppError'
import User from '../../models/User'
import IUsersRepository from '../../repositories/UserRepository/interfaces/IUsersRepository'
import UserRepository from '../../repositories/UserRepository/UserRepository'

interface IRequest {
  id: string
  name: string;
  email: string;
  password: string;
}

export default class UpdateUserService {
  private userRepository: IUsersRepository;

  constructor(userRepository: UserRepository) {
    this.userRepository = userRepository
  }

  public async execute({ id, name, email, password }: IRequest): Promise<User> {
    const user = await this.userRepository.findById(id)

    if (!user) {
      throw new AppError('Usuário não encontrado!', 400)
    }

    if (email !== user.email) {
      const verifyUserEmail = this.userRepository.findByEmail(email)
      if (verifyUserEmail) {
        throw new AppError('E-email já está sendo usado', 400)
      }
    }

    const newPassword = await hash(password, 8)
    user.name = name
    user.email = email
    user.password = newPassword

    await this.userRepository.save(user)

    return user
  }
}
