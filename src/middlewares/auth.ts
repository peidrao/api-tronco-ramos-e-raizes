import { NextFunction, Request, Response } from 'express'
import { verify } from 'jsonwebtoken'
import AppError from '../errors/AppError'

interface TokenPayload {
  iat: number;
  exp: number;
  sub: string;
  isSuper: boolean;
}

const authenticate = (
  request: Request,
  response: Response,
  next: NextFunction
): void => {
  const authHeader = request.headers.authorization

  if (!authHeader) {
    throw new AppError('Sem token JWT', 401)
  }

  const [, token] = authHeader.split(' ')

  try {
    const decoded = verify(token, String(process.env.APP_SECRET)) as TokenPayload

    const { sub, isSuper } = decoded

    request.user = {
      id: sub,
      isSuper
    }

    return next()
  } catch {
    throw new AppError('Token JWt é inválido', 401)
  }
}

export default authenticate
