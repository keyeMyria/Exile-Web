import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { DateValueAccessorModule } from 'angular-date-value-accessor';
import { ReportesListComponent, EditReporteComponent } from './reportes/reportes.component';
import { SampleModule } from '../shared';
import { ReportesService } from './reportes/reportes.service';
import { NovedadesRoutes } from './route';
import { TipoReporteService } from '../configuracion/tiporeporte/tiporeporte.service';
import { ClienteService } from '../operacion/cliente/cliente.service';
import { LugarService } from '../operacion/lugar/lugar.service';
import { AgmCoreModule, GoogleMapsAPIWrapper } from '@agm/core';

@NgModule({
    imports: [
        CommonModule,
        SampleModule,
        FormsModule,
        ReactiveFormsModule,
        AgmCoreModule,
        DateValueAccessorModule,
        RouterModule.forChild(NovedadesRoutes)
    ],
    declarations: [ReportesListComponent, EditReporteComponent],
    providers: [
        ReportesService,
        TipoReporteService,
        ClienteService,
        LugarService,
        GoogleMapsAPIWrapper
    ]
})
export class NovedadesModule { }
