import { Router } from 'express'

import UserController from '../controllers/UserController'
import authenticate from '../middlewares/auth'
import isSuper from '../middlewares/isSuper'

const userRoutes = Router()
const userController = new UserController()

userRoutes.use(authenticate)

userRoutes.post('/', isSuper, userController.create)

userRoutes.get('/', userController.index)
userRoutes.put('/:id', isSuper, userController.update)
userRoutes.delete('/:id', isSuper, userController.destroy)
userRoutes.patch('/:id', isSuper, userController.enableIsSuper)

export default userRoutes
