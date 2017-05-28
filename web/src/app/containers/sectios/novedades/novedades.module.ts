import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { NovedadesRoutes } from './novedades.route';

@NgModule({
    imports: [
        RouterModule.forChild(NovedadesRoutes),
        CommonModule
    ],
    declarations: [],
    providers: []
})
export class NovedadesModule { }
