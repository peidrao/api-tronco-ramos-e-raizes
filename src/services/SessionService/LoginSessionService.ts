import '../../config/env'

import { compare } from 'bcryptjs'
import { sign } from 'jsonwebtoken'
import AppError from '../../errors/AppError'
import User from '../../models/User'
import IUsersRepository from '../../repositories/UserRepository/interfaces/IUsersRepository'

interface Request {
  email: string
  password: string
}
interface Response {
  token: string
  user: User
}

export default class LoginSessionService {
  private userRepository: IUsersRepository

  constructor(userRepository: IUsersRepository) {
    this.userRepository = userRepository
  }

  public async execute({ email, password }:Request): Promise<Response> {
    const user = await this.userRepository.findByEmail(email)
    if (!user) {
      throw new AppError('Usuário não existe', 401)
    }

    const passwordCompare = await compare(password, user.password)
    if (!passwordCompare) {
      throw new AppError('Senha inválida', 401)
    }

    const token = sign({}, process.env.APP_SECRET as string, {
      expiresIn: '1d'
    })

    // delete user.password

    return { token, user }
  }
}
