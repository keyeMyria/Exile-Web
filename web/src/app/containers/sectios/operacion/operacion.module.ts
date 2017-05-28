import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { OperacionRoutes } from './operacion.route';

@NgModule({
    imports: [
        RouterModule.forChild(OperacionRoutes),
        CommonModule
    ],
    declarations: [],
    providers: []
})
export class OperacionModule { }
