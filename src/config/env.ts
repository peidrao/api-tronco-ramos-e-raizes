import { resolve } from 'path'
import { config } from 'dotenv'

config({ path: resolve(__dirname, '../../.env') })

/* export default {
  jwt: {
    secret: 'a08931f985f14638e8749114fb17b016',
    expiresIn: '5h'
  }
}
 */
