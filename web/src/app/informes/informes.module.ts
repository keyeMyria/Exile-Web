import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { InformesRoutes } from './informes.route';
import { EstadisticasComponent } from './estadisticas/estadisticas.component';
import { ExportacionComponent } from './exportacion/exportacion.component';

@NgModule({
    imports: [
        CommonModule,
        RouterModule.forChild(InformesRoutes)
    ],
    declarations: [EstadisticasComponent, ExportacionComponent],
    providers: []
})
export class InformesModule { }
