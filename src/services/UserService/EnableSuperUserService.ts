import AppError from '../../errors/AppError'
import User from '../../models/User'
import IUsersRepository from '../../repositories/UserRepository/interfaces/IUsersRepository'

interface Request {
  id: string
}

export default class EnableSuperUserService {
  private userRepository: IUsersRepository;

  constructor(userRepository: IUsersRepository) {
    this.userRepository = userRepository
  }

  public async execute({ id }: Request): Promise<User> {
    const user = await this.userRepository.findById(id)

    if (!user) {
      throw new AppError('Usuário não encontrado!', 404)
    }

    user.isSuper = !user.isSuper

    await this.userRepository.save(user)

    return user
  }
}
