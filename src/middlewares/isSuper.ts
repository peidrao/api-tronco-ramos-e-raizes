import { Request, Response, NextFunction } from 'express'
import AppError from '../errors/AppError'

const isSuperUser = (
  request: Request,
  response: Response,
  next: NextFunction
): void => {
  if (request.user.isSuper) {
    return next()
  }
  throw new AppError('Sem autorização', 401)
}

export default isSuperUser
