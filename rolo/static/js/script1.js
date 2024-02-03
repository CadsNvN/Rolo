// Initialization for ES Users tw elements
import {
  Collapse,
  Dropdown,
  initTE,
} from "tw-elements";

initTE({ Collapse, Dropdown });

// Initialization for ES Users
import {
  Datepicker,
  Input,
  initTE,
} from "tw-elements";

initTE({ Datepicker, Input });

// for tailwind config
tailwind.config = {
    theme: {
        extend: {
            colors: {
                clifford: '#da373d',
                    }
                }
            }
}
