import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';

import { FormsRoutes } from './forms.routing';

import { ExtendedFormsComponent } from './extendedforms/extendedforms.component';
import { RegularFormsComponent } from './regularforms/regularforms.component';
import { WizardComponent } from './wizard/wizard.component';


@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild(FormsRoutes)
  ],
  declarations: [
      ExtendedFormsComponent,
      RegularFormsComponent,
      WizardComponent
  ]
})

export class FormsModule {}
