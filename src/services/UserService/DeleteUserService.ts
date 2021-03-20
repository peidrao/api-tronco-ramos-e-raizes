
import AppError from '../../errors/AppError'

import IUsersRepository from '../../repositories/UserRepository/interfaces/IUsersRepository'
import UserRepository from '../../repositories/UserRepository/UserRepository'

export default class DeleteUserService {
  private userRepository: IUsersRepository;

  constructor(userRepository: UserRepository) {
    this.userRepository = userRepository
  }

  public async execute(id: string): Promise<void> {
    const user = await this.userRepository.findById(id)

    if (!user) {
      throw new AppError('Usuário não existe!', 400)
    }

    await this.userRepository.delete(id)
  }
}
