import { Request, Response } from 'express'

export default class ImageController {
  public async upload(request: Request, response: Response): Promise<Response> {
    const file = request.file.filename
    return response.json({ file })
  }
}
