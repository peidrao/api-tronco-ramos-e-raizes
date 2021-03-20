import { Router } from 'express'

import UserController from '../controllers/UserController'

const userRoutes = Router()
const userController = new UserController()

userRoutes.post('/', userController.create)
userRoutes.get('/', userController.index)
userRoutes.put('/:id', userController.update)
userRoutes.delete('/:id', userController.destroy)

export default userRoutes
