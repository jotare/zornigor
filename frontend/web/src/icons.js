// Reference: https://fontawesome.com/docs/web/use-with/vue/add-icons

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
// fas could be imported and added directly but we'll be adding thousands of
// icons, making the bundle larger for no reason
import {
  faPlus,
} from '@fortawesome/free-solid-svg-icons'


function setup_icons(app) {
  library.add(faPlus);

  app.component("font-awesome-icon", FontAwesomeIcon);
}

export default setup_icons;
