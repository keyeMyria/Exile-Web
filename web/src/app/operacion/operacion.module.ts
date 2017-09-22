import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AgmCoreModule, GoogleMapsAPIWrapper } from '@agm/core';
import { SampleModule } from 'componentex';
import { OperacionRoutes } from './route';
import { MaterialModule } from '@angular/material';

import { ClienteEditComponent, ClienteListComponent } from './cliente/cliente.component';
import { LugarEditComponent, LugarListComponent } from './lugar/lugar.component';
import { TareaComponent } from './tarea/tarea.component';
import { NotificacionService } from './notificacion.service';

import { ClienteService } from './cliente/cliente.service';
import { LugarService } from './lugar/lugar.service';
import { TipoclienteService } from '../configuracion/tipocliente/tipocliente.service';
import { TareaService } from './tarea/tarea.service';
import { CalendarioComponent } from './calendario/calendario.component';
import { TimelinelistComponent } from './timelinelist/timelinelist.component';
import { TareaListComponent } from './tareas-list/tareas-list.component';

@NgModule({
    imports: [
        FormsModule,
        CommonModule,
        SampleModule,
        AgmCoreModule,
        MaterialModule,
        ReactiveFormsModule,
        RouterModule.forChild(OperacionRoutes)
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
    ],
    providers: [
        ClienteService,
        LugarService,
        TipoclienteService,
        TareaService,
        NotificacionService,
        GoogleMapsAPIWrapper
    ]
})
export class OperacionModule { }
