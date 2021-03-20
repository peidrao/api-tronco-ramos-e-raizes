import { NextFunction, Request, Response } from 'express'
import { verify } from 'jsonwebtoken'
import AppError from '../errors/AppError'

const authenticate = (
  request: Request,
  response: Response,
  next: NextFunction
): Promise<any> | void => {
  const authHeader = request.headers.authorization

  if (!authHeader) {
    throw new AppError('Sem token JWT', 401)
  }

  const [, token] = authHeader.split(' ')

  try {
    verify(token, String(process.env.APP_SECRET))
    next()
  } catch {
    throw new AppError('Token JWt é inválido', 401)
  }
}

export default authenticate
