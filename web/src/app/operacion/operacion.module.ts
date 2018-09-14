import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AgmCoreModule, GoogleMapsAPIWrapper } from '@agm/core';
import { SampleModule, material } from '../shared';
import { OperacionRoutes } from './route';

import { ClienteEditComponent, ClienteListComponent } from './cliente/cliente.component';
import { LugarEditComponent, LugarListComponent } from './lugar/lugar.component';
import { TareaComponent } from './tarea/tarea.component';
import { TimelinelistComponent } from './timelinelist/timelinelist.component';
import { CalendarioComponent } from './calendario/calendario.component';
import { BaseComponent } from './base-tarea/base-tarea.component';
import { NotificacionService } from './notificacion.service';
import { ClienteService } from './cliente/cliente.service';
import { LugarService } from './lugar/lugar.service';
import { TipoclienteService } from '../configuracion/tipocliente/tipocliente.service';
import { GrupoService } from '../configuracion/grupo/grupo.service';
import { TareaService } from './tarea/tarea.service';
import { EmpleadoService } from '../usuarios/empleado/empleado.service';


import { TareaListComponent, TareaFormComponent } from './tareas-list/tareas-list.component';
import { ExintervalComponent } from './exinterval/exinterval.component';


@NgModule({
    imports: [
        SampleModule,
        FormsModule,
        CommonModule,
        AgmCoreModule,
        ReactiveFormsModule,
        RouterModule.forChild(OperacionRoutes),
        ...material
    ],
    declarations: [
        ClienteEditComponent,
        ClienteListComponent,
        LugarEditComponent,
        LugarListComponent,
        TareaComponent,
        CalendarioComponent,
        TimelinelistComponent,
        TareaListComponent,
        TareaFormComponent,
        ExintervalComponent,
        BaseComponent
    ],
    providers: [
        ClienteService,
        LugarService,
        TipoclienteService,
        TareaService,
        GrupoService,
        NotificacionService,
        EmpleadoService,
        GoogleMapsAPIWrapper,
    ]
})
export class OperacionModule { }
