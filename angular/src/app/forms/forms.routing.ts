import { Routes } from '@angular/router';

import { ExtendedFormsComponent } from './extendedforms/extendedforms.component';
import { RegularFormsComponent } from './regularforms/regularforms.component';
import { WizardComponent } from './wizard/wizard.component';




export const FormsRoutes: Routes = [
    {
      path: '',
      children: [ {
        path: 'regular',
        component: RegularFormsComponent
    }]},{
    path: '',
    children: [ {
      path: 'extended',
      component: ExtendedFormsComponent
    }]
    },{
        path: '',
        children: [ {
            path: 'wizard',
            component: WizardComponent
        }]
    }
];
