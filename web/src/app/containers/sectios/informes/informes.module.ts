import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { InformesRoutes } from './informes.route';

@NgModule({
    imports: [
        CommonModule,
        RouterModule.forChild(InformesRoutes)
    ],
    declarations: [],
    providers: []
})
export class InformesModule { }
